from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

if not os.path.exists('data'):
    os.makedirs('data')

driver = webdriver.Chrome()
query = "Laptop"
file = 0
for i in range(1,20): 
    driver.get(f"https://www.amazon.co.uk/s?k={query}&page={i}&crid=YGWNDRXXCGUT&sprefix=lap%2Caps%2C838&ref=nb_sb_ss_ts-doa-p_4_3")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
    time.sleep(2)
driver.close()
