from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .helpers import options
import pandas as pd


class scraper:
    def __init__(self, name, url, elements, browser_options=options):
        self.name = name
        self.url = url
        self.elements = elements
        self.links = self.get_links_file()
        self.driver = ChromeDriverManager().install()
        self.browser = webdriver.Chrome(self.driver, options=browser_options)
        self.data = []
        self.dataframe = self.get_data_file()

    def get_links(self):
        pass

    def get_data(self):
        pass

    def get_links_file(self):
        try:
            print('Trying to read links from file')
            with open('/app/data/' + self.name + '_links.txt') as f:
                return f.readlines()
        except:
            print('Could not read links from file')
            return []

    def get_data_file(self):
        try:
            print('Trying to read data from file')
            return pd.read_excel('/app/data/' + self.name + '_data.xlsx')
        except:
            print('Could not read data from file')
            return pd.DataFrame({'A': []})

    def save_links(self, filename):
        try:
            with open(filename + '.txt', 'w') as f:
                for link in self.links:
                    f.write(link + '\n')
        except:
            print('Please run in docker (See README.md)')

    def save_data(self, filename):
        try:
            self.dataframe.to_excel(filename + '.xlsx', index=False)
        except:
            print('Please run in docker (See README.md)')

    def clean_data(self):
        pass

    def run(self):
        if not self.links:
            self.get_links()
            self.save_links('/app/data/' + self.name + '_links')
        if self.dataframe.empty:
            self.get_data()
        self.clean_data()
        self.save_data('/app/data/' + self.name + '_data')
