from ton_fragment.numbers.bid import Bid
class BidHistory:
    """ BidHistory model
    """
    def __init__(self, bid_history: [Bid]):
        self.__bid_history = bid_history
    
    def __str__(self):
      return self.__bid_history

    def __repr__(self):
      return self.__bid_history