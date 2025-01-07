import requests
from bs4 import BeautifulSoup
import smtplib


def fetch_price(url,headers):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # fetches the title using class identifier
    p_title = soup.find(
        attrs={"class":"VU-ZEz"}
    ).get_text(strip=True)

    # fetches the price using class identifier
    p_price=soup.find(
        attrs={"class":"Nx9bqj CxhGGd"}
    ).get_text(strip=True)

    p_price=p_price.replace(",","")
    p_price=p_price.replace("₹","")
    final_price=float(p_price)
    return p_title,final_price


def send_mail(url,product_name,user_email):
    src_email = "nihaalvirgincar193@gmail.com"
    passwd = 'wgkvgmwipciasfwc'

    #starts a server connection
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user=src_email,password=passwd)

    subject = "Hey! The price just dropped"
    body = f"Product:{product_name}\n\nFlipkart link:{url}"
    message = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        from_addr=src_email,
        to_addrs=user_email,
        msg=message
    )

    server.quit()




