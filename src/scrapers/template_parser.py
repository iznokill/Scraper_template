from src.utilities.scraper import scraper

# website link
url = ''

# css , XPATH, or ID of the elements to scrape
elements = {}


class TemplateScraper(scraper):
    def get_links(self):
        pass

    def get_data(self):
        pass

    def clean_data(self):
        pass


scraper = TemplateScraper('cession_pme', url, elements)
scraper.run()
