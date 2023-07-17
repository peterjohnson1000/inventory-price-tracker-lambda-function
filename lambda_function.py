import requests
from bs4 import BeautifulSoup
import boto3

def lambda_handler(event, context):
    url = "https://www.imastudent.com/sony-zv-e10-mirrorless-camera-with-16-50mm-lens-black"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.find("span", class_="price")
    price_str = price_element.text.strip()
    price_digits = ''.join(filter(str.isdigit, price_str))
    price = int(price_digits)
    
    user_price = 61490
    
    ses_client = boto3.client('ses')

    recipient_email = 'petesview24x7@gmail.com'

    subject = 'Price Match'
    body = 'The user price matches the scraped price.'
    
    if user_price == price:
        # Send the email
        response = ses_client.send_email(
        Source='peterj1298@gmail.com',
        Destination={'ToAddresses': [recipient_email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}}
        }
    )
        
    return price