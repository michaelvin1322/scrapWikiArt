import requests
import json
import os
import argparse
import pandas as pd
from urllib.parse import urlparse


servers = pd.read_csv(os.getenv('PROXY_LIST'))
MAX_TRIES = 5


def is_wikipedia_url(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return domain.endswith('wikipedia.org')
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def get_proxy():
    valid_servers = servers[servers['Works']]
    if valid_servers.empty:
        return None, None

    server = valid_servers.sample(1).iloc[0]
    proxy = {
        'http': f"http://{os.getenv('PROXY_USER')}:{os.environ.get('PROXY_PASSWORD')}@{server['Server address']}:8080",
    }
    return server.name, proxy


def make_request(query: str):
    for _ in range(MAX_TRIES):
        proxy_ind, proxies = get_proxy()
        if proxies is None:
            print("No working proxies available.")
            return None

        try:
            r = requests.get(
                'http://api.duckduckgo.com/',
                params={'q': query, 'format': 'json'},
                proxies=proxies,
                timeout=3
            )

            if r.status_code == 200:
                try:
                    r_json = r.json()
                    if r_json.get('Abstract') and r_json.get('AbstractURL'):
                        return r_json['Abstract'], r_json['AbstractURL']
                except json.decoder.JSONDecodeError:
                    print("JSONDecodeError: Invalid JSON response.")
            else:
                print(f"Request failed with status code {r.status_code}")
                servers.at[proxy_ind, 'Works'] = False

        except (requests.exceptions.Timeout, requests.exceptions.ProxyError):
            print("Request timed out.")
            servers.at[proxy_ind, 'Works'] = False
        except Exception as e:
            print(f"An error occurred: {e}")
    return None


def main(input_file, output_file):
    # TODO: отфильтровать очевидные нерелевантные названия
    # OK считать сколько раз возвращается ссылка
    # TODO: попробовать использовать ламу для валидации результата

    df = pd.read_csv(input_file, low_memory=False, index_col='URL')
    df_empty = df[df["Description"].isna() & df["WikiDescription"].isna()]

    url_counter = {}
    results = []
    # .sample(100, random_state=42)
    for index, (title, author, date) in df_empty[['Title', 'Author', 'Date']].iterrows():
        response = make_request(f"{title}")
        abstract, url = None, None
        if response:
            abstract, url = response

        if abstract and url in url_counter:
            url_counter[url] += 1
        if abstract and url not in url_counter:
            url_counter[url] = 1

        if abstract:
            results.append((index, title, author, date, url, abstract))
            print(f"{title}, {author}, {date}\nlink: {url}\nabstract: {abstract}")
            print('-' * 80)

    for index, title, author, date, url, abstract in results:
        if url_counter[url] == 1 and is_wikipedia_url(url):
            df[index, "WikiLink"] = url
            df[index, "WikiDescription"] = abstract

    df.to_csv(output_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some URLs.")
    parser.add_argument('input_file', type=str, help='Input CSV file path')
    parser.add_argument('output_file', type=str, help='Output CSV file path')

    args = parser.parse_args()

    main(args.input_file, args.output_file)