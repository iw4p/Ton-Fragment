try:
    from ..helpers.server import get_html_content_from_page, find_all, find
    from .information import Information
    from .bid_history import BidHistory
    from .bid import Bid
    from .ownership_history import OwnershipHistory
except ImportError:
    from ..helpers.server import get_html_content_from_page, find_all, find
    from information import Information
    from bid_history import BidHistory
    from bid import Bid
    from ownership_history import OwnershipHistory


class Number:
    """ Number model
    """
    def __init__(self, number: str):
        self.__number = number
        self.__information: Information
        self.__status_element = ''
        self.__ends_in_element = ''
        self.__highest_bid_element = ''
        self.__bid_step_element = ''
        self.__minimum_bid_element = ''
        self.__price_element = ''
        self.__date_element = ''
        self.__from_element = ''
        self.__bid_history: BidHistory = [Bid]

    def number(self):
        if self.__status_element != '':
            return self.__number
        else:
            self.info()
            return self.__number

    def status(self):
        if self.__status_element != '':
            return self.__status_element
        else:
            self.info()
            return self.__status_element

    def ends_in(self):
        if self.__status_element != '':
            return self.__ends_in_element
        else:
            self.info()
            return self.__ends_in_element

    def info(self):
        fetched_data = get_html_content_from_page(ROUTE='/number/' + self.__number)
        elements = find_all(fetched_data, "div", "table-cell-value tm-value icon-before icon-ton")
        
        self.__highest_bid_element = elements[0].text.strip()
        self.__bid_step_element = elements[1].text.strip()
        self.__minimum_bid_element = elements[2].text.strip()
        
        elements = find_all(fetched_data, "section", "tm-section tm-auction-section")
        
        for element in elements:
            self.__status_element = find(element, "span", "tm-section-header-status tm-status-avail")
            self.__ends_in_element = element.time.attrs['datetime']
        
        self.__information = Information(status=self.__status_element, ends_in=self.__ends_in_element, highest_bid=self.__highest_bid_element, bid_step=self.__bid_step_element, minimum_bid=self.__minimum_bid_element)
        
        return self.__information

    def bid_history(self):
        fetched_data = get_html_content_from_page(ROUTE='/number/' + self.__number)
        print(fetched_data)
        fetched_data = fetched_data.tbody
        # fetched_data = find_all(fetched_data, "div", "tm-table-wrap")
        # fetched_data = find_all(fetched_data, "tr", "")
        # elements = find_all(fetched_data, "div", "table-cell-value tm-value icon-before icon-ton")
        # for element in elements: #skip the first three elements [Highest bid ,Bid step, Minimum bid]
            # self.__price_element = element

            # self.__price_element = find(element, "div", "table-cell-value tm-value icon-before icon-ton")
            # print(self.__price_element)
            # self.__date_element = find(element, "span", "wide-only")
            # self.__from_element = find(element, "a", "tm-wallet")
            # print(self.__price_element)
            # bid = Bid(self.__price_element, self.__date_element, self.__from_element)
            # print(f'bid: {bid}')
            # self.__bid_history.append(bid)

        elements = find_all(fetched_data, "div", "tm-datetime")
        for element in elements:
            self.__price_element = find(element, "span", "wide-only")
            # print(element)
        return self.__bid_history
        # def get_status(self):
        #     return self.__status

        # def get_ends_in(self):
        #     return self.__ends_in

        # def get_highest_bid(self):
        #     return self.__highest_bid

        # def get_bid_step(self):
        #     return self.__bid_step

        # def get_minimum_bid(self):
        #     return self.__minimum_bids

    # def __repr__(self):
    #     return self.__information
