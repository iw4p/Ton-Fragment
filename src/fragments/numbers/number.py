try:
    from ..helpers.server import get_html_content_from_page, find_all, find
    from .information import Information
    from .bid_history import BidHistory
    from .ownership_history import OwnershipHistory
except ImportError:
    from ..helpers.server import get_html_content_from_page, find_all, find
    from information import Information
    from bid_history import BidHistory
    from ownership_history import OwnershipHistory


class Number:
    """ Number model
    """
    def __init__(self, number: str):
        self.number = number
        self.information: Information
        self.number_element = ''
        self.status_element = ''
        self.ends_in_element = ''
        self.highest_bid_element = ''
        self.bid_step_element = ''
        self.minimum_bid_element = ''

    def fetch_data(self):
        fetched_data = get_html_content_from_page(ROUTE='/number/' + self.number)
        elements = find_all(fetched_data, "div", "table-cell-value tm-value icon-before icon-ton")
        
        self.highest_bid_element = elements[0].text.strip()
        self.bid_step_element = elements[1].text.strip()
        self.minimum_bid_element = elements[2].text.strip()
        
        elements = find_all(fetched_data, "section", "tm-section tm-auction-section")
        
        for element in elements:
            self.status_element = find(element, "span", "tm-section-header-status tm-status-avail")
            self.ends_in_element = element.time.attrs['datetime']
        
        self.information = Information(status=self.status_element, ends_in=self.ends_in_element, highest_bid=self.highest_bid_element, bid_step=self.bid_step_element, minimum_bid=self.minimum_bid_element)
        
        return self.information

    def __repr__(self):
        return self.information
