from ton_fragment.helpers.scraper import Scraper
from ton_fragment.models.auction_item import AuctionItem
from ton_fragment.models.sold_item import SoldItem
from ton_fragment.models.sale_item import SaleItem

class Numbers:
    """ Numbers model
    """
    filters = ['auction', 'sold', 'sale']
    sorts = ['listed', 'ending']

    def __init__(self, _filter: filters, sort: sorts = None):

        if _filter not in Numbers.filters:
            self.filter = Numbers.filters[0]
        else:
            self.filter = _filter

        if sort is None:
            self.sort = Numbers.sorts[0]
        elif sort not in Numbers.sorts:
            raise SystemExit(f'{sort} is not a valid option for sort.\nUse one of these options: {Numbers.sorts}')
        else:
            self.sort = sort

        self.scraper: Scraper = Scraper()
        self.route = '/numbers?sort=' + self.sort + '&filter=' + self.filter
        self.result = []
        self.fetch()

    def __fetch_auction(self):
        fetched_data = self.scraper.get_html_content_from_page(ROUTE=self.route)
        elements = self.scraper.find_all(fetched_data, "tr", "tm-row-selectable")
        result = []
        for element in elements:
            title_element = self.scraper.find(element, "div", "table-cell-value tm-value")
            price_in_usd_element = self.scraper.find(element, "div", "table-cell-desc wide-only")
            price_in_ton_element = self.scraper.find(element, "div", "table-cell-value tm-value icon-before icon-ton")
            end_time_human_readable_element = self.scraper.find(element, "div", "tm-timer")
            end_time_element = element.time.attrs['datetime']
            auction_item = AuctionItem(title_element, price_in_usd_element, price_in_ton_element, end_time_human_readable_element, end_time_element)
            result.append(auction_item.show_data)
        return result

    def __fetch_sold(self):
        fetched_data = self.scraper.get_html_content_from_page(ROUTE=self.route)
        elements = self.scraper.find_all(fetched_data, "tr", "tm-row-selectable")
        result = []
        for element in elements:
            title_element = self.scraper.find(element, "div", "table-cell-value tm-value")
            status_element = self.scraper.find(element, "div", "table-cell-value tm-value tm-status-unavail")
            price_in_ton_element = self.scraper.find(element, "div", "table-cell-value tm-value icon-before icon-ton")
            end_time_element = element.time.attrs['datetime']
            sold_item = SoldItem(title_element, status_element, price_in_ton_element, end_time_element)
            result.append(sold_item.show_data)
        return result

    def __fetch_sale(self):
        fetched_data = self.scraper.get_html_content_from_page(ROUTE=self.route)
        elements = self.scraper.find_all(fetched_data, "tr", "tm-row-selectable")
        result = []
        for element in elements:
            title_element = self.scraper.find(element, "div", "table-cell-value tm-value")
            status_element = self.scraper.find(element, "div", "table-cell-value tm-value tm-status-avail")
            price_in_ton_element = self.scraper.find(element, "div", "table-cell-value tm-value icon-before icon-ton")
            end_time_element = element.time.attrs['datetime']
            sale_item = SaleItem(title_element, status_element, price_in_ton_element, end_time_element)
            result.append(sale_item.show_data)
        return result

    def fetch(self):
        if self.filter == 'auction':
            self.result = self.__fetch_auction()
        elif self.filter == 'sold':
            self.result = self.__fetch_sold()
        else:
            self.result = self.__fetch_sale()
