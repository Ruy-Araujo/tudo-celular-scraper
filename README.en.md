[![en](https://img.shields.io/badge/traduzir-PT--BR-yellowgreen?style=for-the-badge&logo=googletranslate&logoColor=4285F4)](/README.md)

# Tudo Celular Scraper

A scraper for extracting cell phone information from the website tudocelular.com, written in Python, which extracts data such as brand, model, price, and saves it in JSON files.

## How to Use

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Ruy-Araujo/
    ```

2. Install the dependencies:

    ```bash
    cd tudo_celular
    pip install -r requirements.txt
    ```

3. Run the scraper:

    ```bash
    scrapy crawl tudo_celular -o tudo_celular.json
    ```

The scraper will extract data from the available cell phones on the tudocelular.com website and save it in a JSON file in the project directory.

## Technical Details

The scraper uses the [Scrapy](https://scrapy.org/) framework to parse the HTML of the cell phone technical specification and description pages, extracting information such as brand, model, release year, etc.

The raw data is available [here](data/)

## Contributing

If you would like to contribute to this project, feel free to open an issue or submit a pull request.
