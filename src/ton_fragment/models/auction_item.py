class AuctionItem:
    """ AuctionItem model
    """
    def __init__(self, title, price_in_usd, price_in_ton, end_time_human_readable, end_time):
        self.title = title
        self.price_in_usd = price_in_usd
        self.price_in_ton = price_in_ton
        self.end_time_human_readable = end_time_human_readable
        self.end_time = end_time

    @property
    def show_data(self):
        return {
        "title": self.title,
        "price_in_usd": self.price_in_usd,
        "price_in_ton": self.price_in_ton,
        "end_time_human_readable": self.end_time_human_readable,
        "end_time": self.end_time,
        }