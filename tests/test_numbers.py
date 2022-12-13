from ton_fragment.numbers.numbers import Numbers
import unittest


class TestGetNumbersResult(unittest.TestCase):
    def test_price_high_to_low_auction_numbers(self):
        price_high_to_low_auction_numbers = Numbers('auction')
        price_high_to_low_auction_numbers = price_high_to_low_auction_numbers.result
        self.assertIsInstance(price_high_to_low_auction_numbers, list, "Result is not a type of list")

    def test_price_low_to_high_auction_numbers(self):
        price_low_to_high_auction_numbers = Numbers('auction', 'price_asc')
        price_low_to_high_auction_numbers = price_low_to_high_auction_numbers.result
        self.assertIsInstance(price_low_to_high_auction_numbers, list, "Result is not a type of list")

    def test_listed_auction_numbers(self):
        listed_auction_numbers = Numbers('auction', 'listed')
        listed_auction_numbers = listed_auction_numbers.result
        self.assertIsInstance(listed_auction_numbers, list, "Result is not a type of list")

    def test_ending_auction_numbers(self):
        ending_auction_numbers = Numbers('auction', 'ending')
        ending_auction_numbers = ending_auction_numbers.result
        self.assertIsInstance(ending_auction_numbers, list, "Result is not a type of list")




    def test_price_high_to_low_sold_numbers(self):
        price_high_to_low_auction_numbers = Numbers('sold')
        price_high_to_low_auction_numbers = price_high_to_low_auction_numbers.result
        self.assertIsInstance(price_high_to_low_auction_numbers, list, "Result is not a type of list")

    def test_price_low_to_high_sold_numbers(self):
        price_low_to_high_sold_numbers = Numbers('sold', 'price_asc')
        price_low_to_high_sold_numbers = price_low_to_high_sold_numbers.result
        self.assertIsInstance(price_low_to_high_sold_numbers, list, "Result is not a type of list")

    def test_listed_sold_numbers(self):
        listed_sold_numbers = Numbers('sold', 'listed')
        listed_sold_numbers = listed_sold_numbers.result
        self.assertIsInstance(listed_sold_numbers, list, "Result is not a type of list")

    def test_ending_sold_numbers(self):
        ending_sold_numbers = Numbers('sold', 'ending')
        ending_sold_numbers = ending_sold_numbers.result
        self.assertIsInstance(ending_sold_numbers, list, "Result is not a type of list")




    def test_price_high_to_low_sale_numbers(self):
        price_high_to_low_sale_numbers = Numbers('sale')
        price_high_to_low_sale_numbers = price_high_to_low_sale_numbers.result
        self.assertIsInstance(price_high_to_low_sale_numbers, list, "Result is not a type of list")

    def test_price_low_to_high_sale_numbers(self):
        price_low_to_high_sale_numbers = Numbers('sale', 'price_asc')
        price_low_to_high_sale_numbers = price_low_to_high_sale_numbers.result
        self.assertIsInstance(price_low_to_high_sale_numbers, list, "Result is not a type of list")

    def test_listed_sale_numbers(self):
        listed_sale_numbers = Numbers('sale', 'listed')
        listed_sale_numbers = listed_sale_numbers.result
        self.assertIsInstance(listed_sale_numbers, list, "Result is not a type of list")

    def test_ending_sale_numbers(self):
        ending_sale_numbers = Numbers('sale', 'ending')
        ending_sale_numbers = ending_sale_numbers.result
        self.assertIsInstance(ending_sale_numbers, list, "Result is not a type of list")


if __name__ == '__main__':
    unittest.main()
