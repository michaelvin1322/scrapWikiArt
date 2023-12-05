
# WikiArt Scraper

This repository contains scrapers developed for 
[wikiart.org](https://www.wikiart.org/). The scraper is a part of the 
project [Art Guide](https://github.com/aguschin/art-guide) undertaken in 
[Practicing DS Skills in ML 
Competitions](https://harbour.space/data-science/courses/practicing-ds-skills-in-ml-competitions-alexander-guschin-875) and [Building ML-powered Applications](https://harbour.space/data-science/courses/building-ml-powered-application-alexander-guschin-960) 
classes. 

For our project, we required comprehensive metadata about art pieces, such 
as genres, styles, and other descriptors which were not present in other 
datasets I found. Thus, these scrapers are 
designed to extract all tabular information about Art Pieces, Artists, Art Movements, Schools and Styles.   
present on the website.

## Overview

The project consists of 5 crawlers:

1. **wikiart spider**: This crawler extracts comprehensive details and images of various art pieces from the WikiArt website.
2. **wikiart artists spider**: This crawler specializes in gathering information about artists.
3. **wikiart styles spider**: This crawler is focused on collecting extensive information about different art styles.
4. **wikiart movements spider**: This crawler delves into the world of art movements.
5. **wikiart schools spider**: This crawler concentrates on gathering comprehensive data about art schools.

**Scraped Information for Artworks:**
- URL
- Title
- Original Title
- Author
- Author Link
- Date
- Styles
- Series
- Series Link
- Genre
- Genre Link
- Media
- Location
- Dimensions
- Description
- Wiki Description
- Wiki Link
- Tags
- Image URLs
- Images

**Scraped Information about Artists:**
- URL
- Name
- Original Name
- Birth Date
- Birthplace
- Death Date
- Death Place
- Active Years
- Nationality
- Art Movements
- Painting School
- Genres
- Fields
- Influenced On
- Influenced By
- Teachers
- Pupils
- Art Institutions
- Friends And Coworkers
- Description
- Wiki Description
- Wikipedia Link

**Scraped Information for Art Styles:**
- Name
- Link
- Description

**Scraped Information for Art Movements:**
- Name
- Link
- Description

**Scraped Information for Art Schools:**
- Name
- Link
- Description

The main objective is to extract detailed data about art pieces and artists from the website, providing valuable datasets for data science and machine learning endeavors.

*Scraping of 191265 images took **~14 hours** on a MacBook Pro (Retina, 
15-inch, Mid 2015, 2,2 GHz Quad-Core Intel Core i7). Scraping of 3521 
artists took **less than 10 
minutes***

## Prerequisites

- Python 3.x
- Scrapy

## Installation

1. Clone this repository:
`git clone https://github.com/michaelvin1322/scrapWikiArt`

2. Navigate to the repository and install the required packages:

`cd wikiart-scraper`\
`pip install -r requirements.txt`

## Usage

### Art Pieces Crawler

To start the `ArtPiecesCrawler`, run the following:

`scrapy runspider -o data/data.csv -t csv ScrapWikiArt/wikiart.py`

This will extract details and images of art pieces and save them in your preferred output format.

### Artists Crawler

To initiate the `ArtistsCrawler`, execute:

`scrapy runspider -o data/artists.csv -t csv ScrapWikiArt/wikiart_artist.py`

This will gather detailed information about artists and save them similarly.

### Styles Crawler

To run the `StylesCrawler`, execute:

`scrapy runspider -o data/styles.csv -t csv ScrapWikiArt/wikiart_style.py`

### Movements Crawler

To run the `MovementsCrawler`, execute:

`scrapy runspider -o data/movements.csv -t csv ScrapWikiArt/wikiart_movement.py`

### Schools Crawler

To run the `SchoolsCrawler`, execute:

`scrapy runspider -o data/schools.csv -t csv ScrapWikiArt/spiders/wikiart_school.py`

### DuckDuckGo Crawler

To run the 

`scrapy runspider -o data/data_update_v1.csv -t csv -a input_file=data/data.csv ScrapWikiArt/spiders/duck_duck_go.py`

## Output

### Art Pieces Crawler

By default, images will be downloaded into the `data/img` directory and 
data will be saved in `data/data.csv`. 

Images folder may be changed in `settings.py` by changing path in 
`IMAGES_STORE`.

### Artists Crawler

By default, data will be saved in `data/artists.csv`.

### Styles Crawler

By default, data will be saved in `data/styles.csv`.

### Movements Crawler

By default, data will be saved in `data/movements.csv`.

### Schools Crawler

By default, data will be saved in `data/schools.csv`.