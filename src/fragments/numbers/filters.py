from enum import Enum
class Filters(Enum):
    """ Filters model
    """
    ON_AUCTION = 'auction'
    SOLD = 'sold'
    SALE = 'sale'
    def __repr__(self):
        return self.value
