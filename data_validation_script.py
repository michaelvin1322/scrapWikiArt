from huggingface_hub import hf_hub_download
from llama_cpp import Llama
import pandas as pd
from tqdm import tqdm


def generate_prompt_meta(df_type):

    def inner(row_dict):
        prompt = f"Review the following information about a {df_type}:\n"

        for key, value in row_dict.items():
            if key.lower() in ['url', 'image_urls']:
                continue
            prompt += f"{key}: {value}\n"

        prompt += f"""
        And its DuckDuckGo-sourced description:"
        WikiDescription: {row_dict.get('WikiDescription', '[No Wiki Description]')} 
        
        Is the WikiDescription accurate and relevant to this {df_type}? Answer with 'Yes' or 'No' only."""

        return prompt.strip()
    return inner


def process_model_response(response):
    if response.strip().lower() == 'yes':
        return True
    elif response.strip().lower() == 'no':
        return False
    else:
        # Handle unexpected responses
        return None


if __name__ == '__main__':
    model_path = hf_hub_download(repo_id="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
                                 filename="mistral-7b-instruct-v0.1.Q8_0.gguf")

    model = Llama(
        model_path=model_path,
        # n_gpu_layers=-1,
        n_gqa=8,
        n_ctx=8192,
    )

    tmp = [
        ('data_update.csv', generate_prompt_meta("painting"), 'data_validated.csv'),
        ('artist_update.csv', generate_prompt_meta("artist"), 'artist_validated.csv'),
        ('movements_update.csv', generate_prompt_meta("art movement"), 'movement_validated.csv'),
        ('schools_update.csv', generate_prompt_meta("art school"), 'school_validated.csv'),
        ('styles_update.csv', generate_prompt_meta("art school"), 'styles_validated.csv'),
    ]

    for input_file, generate_prompt, output_file in tmp:

        df = pd.read_csv('./data/' + input_file, low_memory=False, index_col='Link')

        processed_count = 0

        for index, row in tqdm(df.iterrows(), total=df.shape[0]):
            prompt = generate_prompt(row.to_dict())
            response = model(prompt)['choices'][0]['text']
            processed_response = process_model_response(response)
            df.at[index, 'ValidatedRaw'] = response
            df.at[index, 'Validated'] = processed_response

            processed_count += 1
            if processed_count % 100 == 0:
                print(f"Processed {processed_count} records")
        df.to_csv('./data/' + output_file)
