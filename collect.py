from bs4 import BeautifulSoup
import os
import pandas as pd

data = []
for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        # Extracting product title
        title_tag = soup.find("h2")
        title = title_tag.get_text().strip() if title_tag else ""

        # Extracting product link
        link_tag = soup.find("a", class_="a-link-normal s-no-outline")
        product_link = f"https://www.amazon.co.uk{link_tag['href']}" if link_tag and link_tag.get("href") else ""

        # Extracting price
        price_tag = soup.find("span", class_="a-price-whole")
        price = price_tag.get_text().strip() if price_tag else ""
        price_symbol = soup.find("span", class_="a-price-symbol")
        price = f"{price_symbol.get_text().strip()}{price}" if price_symbol and price != "" else price

        # Extracting RRP (Recommended Retail Price)
        rrp_tag = soup.find("span", class_="a-price a-text-price")
        rrp = rrp_tag.find("span", class_="a-offscreen").get_text().strip() if rrp_tag else ""

        # Extracting rating
        rating_tag = soup.find("span", class_="a-icon-alt")
        rating = rating_tag.get_text().strip() if rating_tag else ""

        # Extracting puchase in the past month
        purchases_tag = soup.find("span", class_="a-size-base a-color-secondary", string=lambda text: "bought in past month" in text.lower() if text else False)
        purchases = purchases_tag.get_text().strip() if purchases_tag else ""

        # Extracting delivery information
        delivery_tag = soup.find("span", attrs={"aria-label": lambda x: x and "delivery" in x.lower()})
        delivery = delivery_tag.get_text().strip() if delivery_tag else ""

        # Extracting ASIN
        asin_tag = soup.find("input", attrs={"name": "items[0.base][asin]"})
        asin = asin_tag["value"].strip() if asin_tag else ""

        # Extracting reviews
        reviews_tag = soup.find("a", attrs={"aria-label": lambda x: x and "ratings" in x.lower()})
        reviews = reviews_tag.find("span", class_="a-size-base s-underline-text").get_text().strip() if reviews_tag else ""

        data.append({
        "Title": title,
        "Price": price,
        "RRP": rrp,
        "Rating": rating,
        "Reviews": reviews,
        "Purchases Past Month": purchases,
        "Delivery": delivery,
        "ASIN": asin,
        "Product Link": product_link
    })
        
    except Exception as e:
        print(e)

df = pd.DataFrame(data=data)
df.to_csv("ecommerce_data.csv")