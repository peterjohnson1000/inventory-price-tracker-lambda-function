import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    url = "https://www.imastudent.com/sony-zv-e10-mirrorless-camera-with-16-50mm-lens-black"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.find("span", class_="price")
    price_str = price_element.text.strip()
    price_digits = ''.join(filter(str.isdigit, price_str))
    price = int(price_digits)
    
    userPrice = 65000
    
    if userPrice == price:
        result = "User price is equal to scraped price"
    else:
        result = "User price is not equal to scraped price"
    
    return result