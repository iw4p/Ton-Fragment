from ton_fragment.numbers.numbers import Numbers

x = (Numbers("auction", ""))
y = (Numbers("auction", "listed"))
z = (Numbers("auction", "ending"))

print(x.fetch())
print(y.fetch())
print(z.fetch())


x = (Numbers("sold", ""))
y = (Numbers("sold", "listed"))
z = (Numbers("sold", "ending"))

print(x.fetch())
print(y.fetch())
print(z.fetch())


x = (Numbers("sale", ""))
y = (Numbers("sale", "listed"))
z = (Numbers("sale", "ending"))

print(x.fetch())
print(y.fetch())
print(z.fetch())



from ton_fragment.usernames.usernames import Usernames

x = (Usernames("auction", ""))
y = (Usernames("auction", "listed"))
z = (Usernames("auction", "ending"))

print(x.fetch())
print(y.fetch())
print(z.fetch())


x = (Usernames("sold", ""))
y = (Usernames("sold", "listed"))
z = (Usernames("sold", "ending"))

print(x.fetch())
print(y.fetch())
print(z.fetch())


x = (Usernames("sale", ""))
y = (Usernames("sale", "listed"))
z = (Usernames("sale", "ending"))

print(x.fetch())
print(y.fetch())
print(z.fetch())


from ton_fragment.numbers.number import Number
x = Number('8888888')
print(x.information())
print(x.number)
print(x.status)
print(x.ends_in)
