import requests # to send request to the amazon webpage
from bs4 import BeautifulSoup # for Web scrapping
import lxml

url = "https://www.amazon.in/Apple-iPad-Air-10-9-inch-Wi-Fi-64GB/dp/B08J6MVVBN/ref=sr_1_1_sspa?dchild=1&keywords=ipad&qid=1630143752&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNlRWMFUxNDlOUUZHJmVuY3J5cHRlZElkPUEwMTIyNTI5M0kyWktZMTJIT0VENSZlbmNyeXB0ZWRBZElkPUEwNzUzNTM3MVlNMkIxNUYyTlRSViZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU"

def get_link_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
        "Accept-Language": "en",
    }
    # r is Response Variable for http
    r = requests.get(url, headers=headers)
    # object of the Beautiful Soup
    soup = BeautifulSoup(r.text, "lxml")
    # print(soup.prettify()) prettify use for the get All the data of the web Contain

    # name Contain Name of the product
    name = soup.select_one(selector="#productTitle").getText()  # getText is used for the just get name of the product
    name = name.strip()  # strip used for remove wide Spaces
    #priceblock_ourprice
    # price Contain Price of the product
   #price = soup.select_one(selector="a-price-whole").getText() # getText is used for the just get price of the product
    price = soup.find("span", class_="a-price-whole").getText()
    price = price[1:]  # Slicing of the string to remove Rs. sign
    price = float(price.replace(',', ''))  # remove Comma from the string

    return name,price

# Method call
print(get_link_data(url))