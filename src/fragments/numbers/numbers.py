try:
    from ..helpers.server import get_html_content_from_page, find_all, find
except ImportError:
    from .helpers.server import get_html_content_from_page, find_all, find

class Numbers:
    """ Numbers model
    """

    filters = ['auction', 'sold', 'sale']
    sorts = ['', 'listed', 'ending']

    def __init__(self, _filter: filters, sort: sorts):

        if _filter not in Numbers.filters:
            self.filter = Numbers.filters[0]
        else:
            self.filter = _filter

        if sort not in Numbers.sorts:
            self.sort = Numbers.sort[0]
        else:
            self.sort = sort

        self.route = '?sort=' + self.sort + '&filter=' + self.filter

    def __fetch_auction(self):
        fetched_data = get_html_content_from_page(ROUTE='/numbers' + self.route)
        elements = find_all(fetched_data, "tr", "tm-row-selectable")
        result_array = []
        for element in elements:
            title_element = find(element, "div", "table-cell-value tm-value")
            price_in_usd_element = find(element, "div", "table-cell-desc wide-only")
            price_in_ton_element = find(element, "div", "table-cell-value tm-value icon-before icon-ton")
            end_time_human_readable_element = find(element, "div", "tm-timer")
            end_time_element = element.time.attrs['datetime']
            element1 = {
                "title": title_element,
                "price_in_usd": price_in_usd_element,
                "price_in_ton": price_in_ton_element,
                "end_time_human_readable": end_time_human_readable_element,
                "end_time": end_time_element,
            }
            result_array.append(element1)
        return result_array

    def __fetch_sold(self):
        fetched_data = get_html_content_from_page(ROUTE='/numbers' + self.route)
        elements = find_all(fetched_data, "tr", "tm-row-selectable")
        result_array = []
        for element in elements:
            title_element = find(element, "div", "table-cell-value tm-value")
            status_element = find(element, "div", "table-cell-value tm-value tm-status-unavail")
            price_in_ton_element = find(element, "div", "table-cell-value tm-value icon-before icon-ton")
            end_time_element = element.time.attrs['datetime']
            element1 = {
                "title": title_element,
                "status": status_element,
                "price_in_ton": price_in_ton_element,
                "end_time": end_time_element,
            }
            result_array.append(element1)
        return result_array

    def __fetch_sale(self):
        fetched_data = get_html_content_from_page(ROUTE='/numbers' + self.route)
        elements = find_all(fetched_data, "tr", "tm-row-selectable")
        result_array = []
        for element in elements:
            title_element = find(element, "div", "table-cell-value tm-value")
            status_element = find(element, "div", "table-cell-value tm-value tm-status-avail")
            price_in_ton_element = find(element, "div", "table-cell-value tm-value icon-before icon-ton")
            end_time_element = element.time.attrs['datetime']
            element1 = {
                "title": title_element,
                "status": status_element,
                "price_in_ton": price_in_ton_element,
                "end_time": end_time_element,
            }
            result_array.append(element1)
        return result_array

    def fetch_all(self):
        if self.filter == 'auction':
            return self.__fetch_auction()
        elif self.filter == 'sold':
            return self.__fetch_sold()
        else:
            return self.__fetch_sale()