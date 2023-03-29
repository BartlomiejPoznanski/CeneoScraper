import requests
from bs4 import BeautifulSoup
# product_code = input("Podaj kod produktu: ")
product_code = "97384644"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response = requests.get(url)

print(response.text)
