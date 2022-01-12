# Scraper Template using selenium
<!-- ABOUT THE PROJECT -->
## About The Project

This project is a simple selenium scraper template.

## Usage

- Scrape using a script

  ```sh
    docker build -t <CONTAINER NAME>
   ```
   ```sh
    docker run -it --mount 'type=bind,src=<REPLACE BY YOUR OWN VOLUME>,dst=/app/data/' <CONTAINER NAME>  <SCRAPING SCRIPT>
   ```
