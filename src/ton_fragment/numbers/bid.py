class Bid:
    """ Bid model
    """
    def __init__(self, price: str, date: str, _from: str):
        self.__price = price
        self.__date = date
        self.__from = _from
    
    @property
    def price(self):
        return self.__price

    @property
    def date(self):
        return self.__date

    @property
    def _from(self):
        return self.__from

    @price.setter
    def price(self, price):
        self.__price = price
    
    @date.setter
    def date(self, date):
        self.__date = date

    @_from.setter
    def price(self, _from):
        self.__from = _from

    def __str__(self):
      return f'price: {self.__bid_history}, date: {self.__date}, from: {self.__from}'

    def __repr__(self):
      return f'price: {self.__bid_history}, date: {self.__date}, from: {self.__from}'