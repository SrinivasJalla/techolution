# techolution

## Description

This repository contains Python scripts for extracting links from a specific URL and performing web scraping to extract additional data from those links.

### links_extraction.py

This script extracts links from the URL: [https://packaging.python.org/en/latest/guides/section-install/](https://packaging.python.org/en/latest/guides/section-install/) and stores all the URLs into `extracted_links.csv`.

### web_scraping.py

This script reads `extracted_links.csv` and passes the links column values to URLs using a loop. It extracts the heading, subheading, and code from every link and stores the data into CSV files. The files are available in the `downloaded_data` directory.

## Usage

To run the scripts:

1. Make sure you have Python installed on your system.
2. Install the required dependencies by running:
    ```
    pip install requests beautifulsoup4 pandas
    ```
3. Run `links_extraction.py` to extract links and create `extracted_links.csv`.
4. Run `web_scraping.py` to perform web scraping and store the data in CSV files.

## License

This project is licensed under the [MIT License](LICENSE).
