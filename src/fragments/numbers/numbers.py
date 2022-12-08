try:
    from ..helpers.server import get_html_content_from_page, find_all, find
except ImportError:
    from .helpers.server import get_html_content_from_page, find_all, find

class Numbers:
    """ Numbers model
    """
    def __init__(self, status: str, sort: str, count: int):
        self.status = status
        self.sort = sort
        self.count = count

    def fetch_all(self):
        fetched_data = get_html_content_from_page(ROUTE='/numbers')
        elements = find_all(fetched_data, "tr", "tm-row-selectable")
        result_array = []
        for element in elements:
            title_element = find(element, "div", "table-cell-value tm-value")
            price_in_usd_element = find(element, "div", "table-cell-desc wide-only")
            price_in_ton_element = find(element, "div", "table-cell-value tm-value icon-before icon-ton")
            end_time_human_readable_element = find(element, "div", "tm-timer")
            # end_time_element = find(element, "div", "table-cell-desc")
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