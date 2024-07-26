import requests
from bs4 import BeautifulSoup
from lxml import html
from typing import Optional
from requests.exceptions import JSONDecodeError

BASE_URL = 'https://fragment.com/'


class Scraper:
    """ Scraper model
    """
    # get api_token from https://tonconsole.com/ 
    def __init__(self, api_token: Optional[str] = None):

        self.headers = {
            'accept': 'application/json'
        }
        
        if api_token:
            self.headers['Authorization'] = f'Bearer {api_token}'

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
        
    # find number address
    # for example +888 0465 6319
    def find_nuber_address(self, number: str):

        req_number = number.replace(' ', '').replace('+', '')

        element = self.find_all(self.get_html_content_from_page(f'number/{req_number}'), 'a', 'tm-wallet')
        tree = html.fromstring(str(element[0]))
        href_value = tree.xpath('//a[@class="tm-wallet"]/@href')
        addr = str(href_value[0]).replace('https://tonviewer.com/', '')

        el = requests.get(f'https://tonapi.io/v2/accounts/{str(addr)}/nfts?collection='
                          'EQAOQdwdw8kGftJCSFgOErM1mBjYPe4DBPq8-AhF6vr9si5N'
                          '&limit=10&offset=0&indirect_ownership=false',
                          headers=self.headers)

        number_addr = None

        try:
            for i in el.json()['nft_items']:
                if i['metadata']['name'] == number:
                    number_addr = i['address']
                    break
        except (JSONDecodeError, KeyError, Exception):
            pass

        return number_addr
