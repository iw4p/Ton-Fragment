from ton_fragment.numbers.number import Number
import unittest

class TestGetNumberResult(unittest.TestCase):
    def test_price_high_to_low_auction_numbers(self):
        example_number = '8888888'
        phone_number = Number(example_number)
        self.assertIsInstance(phone_number.data, dict, "Result is not a type of list")

if __name__ == '__main__':
    unittest.main()
