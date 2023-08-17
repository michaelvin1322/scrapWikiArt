
# WikiArt Scraper

This repository contains scrapers developed for 
[wikiart.org](https://www.wikiart.org/). The scraper is a part of the 
project [Art Guide](https://github.com/aguschin/art-guide) undertaken in 
the "Practicing DS Skills in ML Competitions" 
class. The main objective is to extract detailed data about art pieces and artists from the website, providing valuable datasets for data science and machine learning endeavors.

## Overview

The project consists of two main crawlers:

1. `WikiArtSpider`: Extracts details and an image of art pieces.
2. `WikiArtArtistSpider`: Gathers detailed information about artists.

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

`scrapy runspider -o data/data.csv -t csv wikiart.py`

This will extract details and images of art pieces and save them in your preferred output format.

### Artists Crawler

To initiate the `ArtistsCrawler`, execute:

`scrapy runspider -o data/artists.csv -t csv wikiart_artist.py`

This will gather detailed information about artists and save them similarly.

## Output

### Art Pieces Crawler

By default, images will be downloaded into the `data/img` directory and 
data will be saved in `data/data.csv`. 

Images folder may be changed in `settings.py` by changing path in 
`IMAGES_STORE`.

### Artists Crawler

By default, data will be saved in `data/artists.csv`.

