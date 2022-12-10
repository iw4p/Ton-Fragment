class Information:
    """ Information model
    """
    def __init__(self, status: str, ends_in: str, highest_bid: int = 0, bid_step: int = 0, minimum_bid: int = 0):
        self.status = status
        self.ends_in = ends_in
        self.highest_bid = highest_bid
        self.bid_step = bid_step
        self.minimum_bid = minimum_bid

    @property
    def show_data(self):
        return {
            'status': self.status,
            'ends_in': self.ends_in,
            'highest_bid': self.highest_bid,
            'bid_step': self.bid_step,
            'minimum_bid': self.minimum_bid
            }

    # TODO: convert to sth.setter - sth.getter - @property
    def set_status(self, status):
        self.status = status
    
    def set_ends_in(self, ends_in):
        self.ends_in = ends_in
    
    def set_highest_bid(self, highest_bid):
        self.highest_bid = highest_bid
    
    def set_bid_step(self, bid_step):
        self.highest_bid = highest_bid
    
    def set_minimum_bid(self, minimum_bid):
        self.highest_bid = highest_bid
    
    def get_status(self):
        return self.status

    def get_ends_in(self):
        return self.ends_in

    def get_highest_bid(self):
        return self.highest_bid

    def get_bid_step(self):
        return self.bid_step

    def get_minimum_bid(self):
        return self.minimum_bids

    # def __repr__(self):
    #     return f'Status: {self.status}\nEnds in: {self.ends_in}\nHighest Bid: {self.highest_bid}\nBid Step: {self.bid_step}\nMinimum Bid: {self.minimum_bid}'

    # def __str__(self):
    #     return str({'status': self.status, 'ends_in': self.ends_in,'highest_bid': self.highest_bid,'bid_step': self.bid_step, 'minimum_bid': self.minimum_bid})
