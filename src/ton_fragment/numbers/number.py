from ton_fragment.helpers.scraper import Scraper
from ton_fragment.numbers.information import Information
from ton_fragment.numbers.bid_history import BidHistory
from ton_fragment.numbers.bid import Bid
from ton_fragment.numbers.ownership_history import OwnershipHistory
class Number:
    """ Number model
    """
    def __init__(self, number: str):
        self.number = number
        self.information: Information
        self.status_element = ''
        self.ends_in_element = ''
        self.highest_bid_element = ''
        self.bid_step_element = ''
        self.minimum_bid_element = ''
        self.price_element = ''
        self.date_element = ''
        self.from_element = ''
        self.bid_history: BidHistory = [Bid]
        self.scraper: Scraper = Scraper()

    @property
    def status(self):
        if self.status_element != '':
            return self.status_element
        else:
            self.information()
            return self.status_element
    @property
    def ends_in(self):
        if self.status_element != '':
            return self.ends_in_element
        else:
            self.information()
            return self.ends_in_element

    @property
    def data(self):
        fetched_data = self.scraper.get_html_content_from_page(ROUTE='/number/' + self.number)
        elements = self.scraper.find_all(fetched_data, "div", "table-cell-value tm-value icon-before icon-ton")

        self.highest_bid_element = elements[0].text.strip()
        self.bid_step_element = elements[1].text.strip()
        self.minimum_bid_element = elements[2].text.strip()
        
        elements = self.scraper.find_all(fetched_data, "section", "tm-section tm-auction-section")
        
        for element in elements:
            self.status_element = self.scraper.find(element, "span", "tm-section-header-status tm-status-avail")
            self.ends_in_element = element.time.attrs['datetime']
        
        self.information = Information(status=self.status_element, ends_in=self.ends_in_element, highest_bid=self.highest_bid_element, bid_step=self.bid_step_element, minimum_bid=self.minimum_bid_element)
        
        return self.information.show_data

    def bid_history(self):
        fetched_data = self.scraper.get_html_content_from_page(ROUTE='/number/' + self.number)
        print(fetched_data)
        fetched_data = fetched_data.tbody
        # fetched_data = self.scraper.find_all(fetched_data, "div", "tm-table-wrap")
        # fetched_data = self.scraper.find_all(fetched_data, "tr", "")
        # elements = self.scraper.find_all(fetched_data, "div", "table-cell-value tm-value icon-before icon-ton")
        # for element in elements: #skip the first three elements [Highest bid ,Bid step, Minimum bid]
            # self.price_element = element

            # self.price_element = self.scraper.find(element, "div", "table-cell-value tm-value icon-before icon-ton")
            # print(self.price_element)
            # self.date_element = self.scraper.find(element, "span", "wide-only")
            # self.from_element = self.scraper.find(element, "a", "tm-wallet")
            # print(self.price_element)
            # bid = Bid(self.price_element, self.date_element, self.from_element)
            # print(f'bid: {bid}')
            # self.bid_history.append(bid)

        elements = self.scraper.find_all(fetched_data, "div", "tm-datetime")
        for element in elements:
            self.price_element = self.scraper.find(element, "span", "wide-only")
            # print(element)
        return self.bid_history
        # def get_status(self):
        #     return self.status

        # def get_ends_in(self):
        #     return self.ends_in

        # def get_highest_bid(self):
        #     return self.highest_bid

        # def get_bid_step(self):
        #     return self.bid_step

        # def get_minimum_bid(self):
        #     return self.minimum_bids

    # def __repr__(self):
    #     return self.information
