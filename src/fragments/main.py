from fragments.numbers.numbers import Numbers
from fragments.numbers.filters import Filters
x = Numbers("", "ending")
y = x.fetch_all()
print(y)

# from fragments.numbers.number import Number
# x = Number('8888888')
# y = x.information()
# print(x.bid_history())
# print(x.number())
# print(x.status())
# print(x.ends_in())
