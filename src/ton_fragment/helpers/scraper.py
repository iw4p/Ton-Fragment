import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://fragment.com/'

class Scraper:
    """ Scraper model
    """
    def __init__(self):
        pass
    
    def get_html_content_from_page(self, ROUTE: str):
        """ This function ...
        """
        page = requests.get(BASE_URL + ROUTE)
        soup = BeautifulSoup(page.content, "html.parser")

        try:
            return soup
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        if soup is None:
            raise SystemExit('Error: html content not found')

        return soup

    def find_all(self, soup: str, tag: str, class_name: str):
        elements = soup.find_all(tag, class_=class_name)
        return elements

    def find(self, elements, tag: str, class_name: str):
        result = elements.find(tag, class_=class_name).text.strip()
        return result