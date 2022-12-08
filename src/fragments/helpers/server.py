from typing import Tuple, List, Optional, Dict

import requests
from bs4 import BeautifulSoup

try:
    from .models import *
except ImportError:
    from models import *

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://fragment.com/'

def get_html_content_from_page(ROUTE: str):
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

def find_all(soup: str, tag: str, class_name: str):
    elements = soup.find_all(tag, class_=class_name)
    return elements

def find(elements, tag: str, class_name: str):
    # results = []
    # for element in elements:
    result = elements.find(tag, class_=class_name).text.strip()
        # results.append(result)
    return result