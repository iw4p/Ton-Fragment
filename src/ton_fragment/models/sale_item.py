class SaleItem:
    """ SaleItem model
    """
    def __init__(self, title, status, price_in_ton, end_time):
        self.title = title
        self.status = status
        self.price_in_ton = price_in_ton
        self.end_time = end_time

    @property
    def show_data(self):
        return {
        "title": self.title,
        "status": self.status,
        "price_in_ton": self.price_in_ton,
        "end_time": self.end_time,
        }