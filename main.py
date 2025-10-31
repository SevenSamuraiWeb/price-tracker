
import requests
from bs4 import BeautifulSoup
import smtplib
import toml


def fetch_price(url,headers):
    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # fetches the title using class identifier
        p_title_element = soup.find(attrs={"class": "VU-ZEz"})
        p_title = p_title_element.get_text(strip=True) if p_title_element else "Title not found"

        # fetches the price using class identifier
        p_price_element = soup.find(attrs={"class": "Nx9bqj CxhGGd"})
        p_price = p_price_element.get_text(strip=True) if p_price_element else "Price not found"

        p_price=p_price.replace(",","")
        p_price=p_price.replace("₹","")
        final_price=float(p_price)
        return p_title,final_price
    else:
        raise Exception(f"Failed to retrieve page, status code {response.status_code}")



def send_mail(url, product_name, user_email):
    secrets = toml.load("secrets.toml")
    src_email = secrets["email"]
    passwd = secrets["password"]

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user=src_email, password=passwd)

    subject = "Hey! The price just dropped"
    body = f"Product: {product_name}\n\nFlipkart link: {url}"
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        from_addr=src_email,
        to_addrs=user_email,
        msg=message
    )
    server.quit()




