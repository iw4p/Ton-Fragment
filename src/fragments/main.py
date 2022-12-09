from fragments.numbers.numbers import Numbers
from fragments.numbers.filters import Filters

# x = (Numbers("auction", ""))
# y = (Numbers("auction", "listed"))
# z = (Numbers("auction", "ending"))

# print(x.fetch_all())
# print(y.fetch_all())
# print(z.fetch_all())


# x = (Numbers("sold", ""))
# y = (Numbers("sold", "listed"))
# z = (Numbers("sold", "ending"))

# print(x.fetch_all())
# print(y.fetch_all())
# print(z.fetch_all())


x = (Numbers("sale", ""))
y = (Numbers("sale", "listed"))
z = (Numbers("sale", "ending"))

print(x.fetch_all())
print(y.fetch_all())
print(z.fetch_all())



# from fragments.numbers.number import Number
# x = Number('8888888')
# print(x.information())
# # print(x.bid_history())
# print(x.number)
# print(x.status)
# print(x.ends_in)
