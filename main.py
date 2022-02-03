import smtplib

from bs4 import BeautifulSoup
import requests
import os

email_pass = os.environ.get("EMAIL_PASS")
my_email = os.environ.get("EMAIL_ADDR")

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "PHPSESSID=8mepqprupj2qqvjtmnohhhf3v2; _ga=GA1.2.443508061.1643832570; _gid=GA1.2.1131766731.1643832570",
    "Host": "www.amazon.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"
}
product_url = "https://www.amazon.com/dp/B09KPT6TVQ/ref=sspa_dk_detail_2?pd_rd_i=B09KPT6TVQ&pd_rd_w=xJRvJ&pf_rd_p=9fd3ea7c-b77c-42ac-b43b-c872d3f37c38&pd_rd_wg=8JE30&pf_rd_r=4J9WZDSNM6KXF4NN2P54&pd_rd_r=297de94c-1b92-4b8c-8790-0051b43473f7&s=home-garden&smid=A1I9XDHTC0Z8BL&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExU0M3RlVJWkRMNDZYJmVuY3J5cHRlZElkPUEwNjU2MTc3TDNITzBVNTRZODdRJmVuY3J5cHRlZEFkSWQ9QTAwMTA1NDcyQzM4UEs2WjVWWjJXJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"

site = requests.get(product_url, headers=headers)
soup = BeautifulSoup(site.text, "html.parser")

original_price = 27.99
price = float(soup.find(class_="a-offscreen", name="span").get_text()[1:])
product_name = soup.find(class_="a-size-large product-title-word-break", id="productTitle").get_text()[8:-8]

to_email = "kiransettyks@gmail.com"

if original_price > price:
    with smtplib.SMTP("smtp.gmail.com") as email:
        email.starttls()
        email.login(user=my_email, password=email_pass)
        email.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Price Drop on Amazon product\n\nThe price of '{product_name}' has dropped from ${original_price:.2f} to ${price:.2f}. Buy now!\nLink: {product_url}")

