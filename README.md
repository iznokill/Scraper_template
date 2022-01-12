# Scraper Template using selenium
<!-- ABOUT THE PROJECT -->
## About The Project

This project is a simple selenium scraper template.

## Usage

### Scrape using a script

- build the docker container
  ```sh
    docker build -t <CONTAINER NAME>
   ```
- run the script [ You need to mount a volume to the container to save the scraped data ]
   ```sh
    docker run -it --mount 'type=bind,src=<REPLACE BY YOUR OWN VOLUME>,dst=/app/data/' <CONTAINER NAME>  <SCRAPING SCRIPT>
   ```
