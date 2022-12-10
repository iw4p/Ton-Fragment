from ton_fragment.numbers.bid import Bid

from typing import List
class BidHistory:
    """ BidHistory model
    """
    def __init__(self, bid_history: List[Bid]):
        self.__bid_history = bid_history
    
    def __str__(self):
      return self.__bid_history

    def __repr__(self):
      return self.__bid_history