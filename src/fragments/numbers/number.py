class Number:
    """ Number model
    """
    def __init__(self, number: str, status: str, info: Info, bid_history: BidHistory, ownership_history: OwnershipHistory, ends_in: str):
        self.number = number