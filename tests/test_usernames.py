from ton_fragment.usernames.usernames import Usernames
import unittest

class TestGetNumbersResult(unittest.TestCase):
    def test_price_high_to_low_auction_usernames(self):
        price_high_to_low_auction_usernames = Usernames('auction')
        price_high_to_low_auction_usernames = price_high_to_low_auction_usernames.result
        self.assertIsInstance(price_high_to_low_auction_usernames, list, "Result is not a type of list")

    def test_price_low_to_high_auction_usernames(self):
        price_low_to_high_auction_usernames = Usernames('auction', 'price_asc')
        price_low_to_high_auction_usernames = price_low_to_high_auction_usernames.result
        self.assertIsInstance(price_low_to_high_auction_usernames, list, "Result is not a type of list")

    def test_listed_auction_usernames(self):
        listed_auction_usernames = Usernames('auction', 'listed')
        listed_auction_usernames = listed_auction_usernames.result
        self.assertIsInstance(listed_auction_usernames, list, "Result is not a type of list")

    def test_ending_auction_usernames(self):
        ending_auction_usernames = Usernames('auction', 'ending')
        ending_auction_usernames = ending_auction_usernames.result
        self.assertIsInstance(ending_auction_usernames, list, "Result is not a type of list")




    def test_price_high_to_low_sold_usernames(self):
        price_high_to_low_auction_usernames = Usernames('sold')
        price_high_to_low_auction_usernames = price_high_to_low_auction_usernames.result
        self.assertIsInstance(price_high_to_low_auction_usernames, list, "Result is not a type of list")

    def test_price_low_to_high_sold_usernames(self):
        price_low_to_high_sold_usernames = Usernames('sold', 'price_asc')
        price_low_to_high_sold_usernames = price_low_to_high_sold_usernames.result
        self.assertIsInstance(price_low_to_high_sold_usernames, list, "Result is not a type of list")

    def test_listed_sold_usernames(self):
        listed_sold_usernames = Usernames('sold', 'listed')
        listed_sold_usernames = listed_sold_usernames.result
        self.assertIsInstance(listed_sold_usernames, list, "Result is not a type of list")

    def test_ending_sold_usernames(self):
        ending_sold_usernames = Usernames('sold', 'ending')
        ending_sold_usernames = ending_sold_usernames.result
        self.assertIsInstance(ending_sold_usernames, list, "Result is not a type of list")




    def test_price_high_to_low_sale_usernames(self):
        price_high_to_low_sale_usernames = Usernames('sale')
        price_high_to_low_sale_usernames = price_high_to_low_sale_usernames.result
        self.assertIsInstance(price_high_to_low_sale_usernames, list, "Result is not a type of list")

    def test_price_low_to_high_sale_usernames(self):
        price_low_to_high_sale_usernames = Usernames('sale', 'price_asc')
        price_low_to_high_sale_usernames = price_low_to_high_sale_usernames.result
        self.assertIsInstance(price_low_to_high_sale_usernames, list, "Result is not a type of list")

    def test_listed_sale_usernames(self):
        listed_sale_usernames = Usernames('sale', 'listed')
        listed_sale_usernames = listed_sale_usernames.result
        self.assertIsInstance(listed_sale_usernames, list, "Result is not a type of list")

    def test_ending_sale_usernames(self):
        ending_sale_usernames = Usernames('sale', 'ending')
        ending_sale_usernames = ending_sale_usernames.result
        self.assertIsInstance(ending_sale_usernames, list, "Result is not a type of list")


if __name__ == '__main__':
    unittest.main()
