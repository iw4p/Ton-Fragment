# TON Fragment

## UnOfficial Fragment API (buy stars - premium) (Telegram - Ton Coin) Python library

[![Ton-Fragment](https://github.com/iw4p/ton-fragment/raw/master/images/main_page_fragment.jpeg
)](https://pypi.org/project/ton-fragment/)
![Image](https://github.com/user-attachments/assets/9e0e5de7-1aa3-4092-8dd3-28cd6fbc9b92)
[![PyPI version](https://img.shields.io/pypi/v/ton-fragment.svg)](https://pypi.org/project/ton-fragment)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/ton-fragment.svg)](#Installation)
[![Downloads](https://pepy.tech/badge/ton-fragment)](https://pepy.tech/project/ton-fragment)

### Note 1: ⚠️ If you need API for buying stars and telegram premium (We Support Both KYC and no KYC Fragment), contact me on Telegram [@JailBroken](https://t.me/JailBroken). 

# 🌟 Telegram Stars & Premium API – Fast, Secure & Reliable! 🌟  

⚠️ **We Support Both KYC and no KYC Fragment**  

Looking for an API to purchase **Telegram Stars** and **Telegram Premium**? We provide a **trusted and seamless solution** for businesses and individuals.  

## 🔥 Why Choose Us?  
- ✅ **Trusted by 100+ Businesses** – Proven reliability and performance  
- ✅ **Secure & Fast Transactions** – Get your purchases instantly  
- ✅ **24/7 Live Support** – We're always here to assist you  
- ✅ **Easy API Integration** – Automate your purchases with ease  
- ✅ **Regular Updates & News** – Stay informed with our latest services  

## 💰 Fees & Prices  
- **1-Week Free Trial**: Get started with our API **without paying any fee** for the first 7 days.  
- **Stars & Premium Prices**: Same as **Fragment**, sometimes **cheaper for loyal users**.  
- **Negotiable Fees**: Fees start as low as **1% and can go even lower** based on volume and loyalty.  
- **Special Discounts & Cashbacks**: Enjoy **cashbacks on special days** and **discounts for repeat customers**.  

## 📢 Stay Updated  
For the latest news and updates, join our official channel:  
📢 [@Fragment_API_News](https://t.me/Fragment_API_News)  

## 💬 Contact Us  
Need assistance or want to integrate our API?  
📩 Message us on Telegram: [@JailBroken](https://t.me/JailBroken)  

🚀 **Start using the best Telegram Stars & Premium API today!**  



### Note 2: ⚠️ This package is still under develop and needs your contribution. Sometimes maybe you get an error, It's normal and fine; You can open an issue to keep me informed.

### Installation

```sh
$ pip install ton-fragment
```
Also can be found on [pypi](https://pypi.org/project/ton-fragment/)

## Usage
### Available options
For Usernames(x, y) and Numbers(x, y):
x can be one of ['auction', 'sold', 'sale'] and it's required.
y is not required it can be ['listed', 'ending', 'price_asc']. the default is empty which triggerd price high to low function.

### Buy Telegram premium API (We Support Both KYC and no KYC Fragment)
contact me on Telegram [@JailBroken](https://t.me/JailBroken) or [iw4p@protonmail.com](mailto:iw4p@protonmail.com?subject=Ton-Fragment).

### Buy Telegram Stars API (We Support Both KYC and no KYC Fragment)
contact me on Telegram [@JailBroken](https://t.me/JailBroken) or [iw4p@protonmail.com](mailto:iw4p@protonmail.com?subject=Ton-Fragment).


### Usernames
Get All Usernames - Top Auctions - Price high to low:
```python
from ton_fragment.usernames.usernames import Usernames
all_usernames = Usernames('auction')
print(all_usernames.result)
```
Get All Usernames - Top Auctions - Price low to high:
```python
from ton_fragment.usernames.usernames import Usernames
all_usernames = Usernames('auction', 'price_asc')
print(all_usernames.result)
```
Get All Usernames - Top Auctions - sort by recently listed:
```python
from ton_fragment.usernames.usernames import Usernames
all_usernames = Usernames('auction', 'listed')
print(all_usernames.result)
```
Get All Usernames - Top Auctions - sort by ending soon:
```python
from ton_fragment.usernames.usernames import Usernames
all_usernames = Usernames('auction', 'ending')
print(all_usernames.result)
```
### Numbers
Get All Numbers - For Sale:
```python
from ton_fragment.numbers.numbers import Numbers
all_numbers = Numbers('sale')
print(all_numbers.result)
```
Get All Numbers - Sold - sort by recently listed:
```python
from ton_fragment.numbers.numbers import Numbers
all_numbers = Numbers('sold', 'listed')
print(all_numbers.result)
```
Get All Numbers - For Sale - sort by ending soon:
```python
from ton_fragment.numbers.numbers import Numbers
all_numbers = Numbers('sale', 'ending')
print(all_numbers.result)
```
Get a brief information about a number
```python
from ton_fragment.numbers.number import Number
my_number = Number('8888888')
print(my_number.data)
print(my_number.number)
print(my_number.status)
print(my_number.ends_in)
```
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=iw4p/ton-fragment&type=Date)](https://star-history.com/#iw4p/ton-fragment&Date)

### Issues
Feel free to submit issues and enhancement requests or contact me via [vida.page/nima](https://vida.page/nima).

### Contributing
Please refer to each project's style and contribution guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Update the Version** inside __init__.py
 4. **Commit** changes to your own branch
 5. **Push** your work back up to your fork
 6. Submit a **Pull request** so that we can review your changes
