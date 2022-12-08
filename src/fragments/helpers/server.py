from typing import Tuple, List, Optional, Dict

import requests
from bs4 import BeautifulSoup

try:
    from .models import *
except ImportError:
    from models import *

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.fragment.com'

def get_html_content_from_page():
    """ This function ...
    """
    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    try:
        return soup
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    if soup is None:
        raise SystemExit('Error: html content not found')

    return soup