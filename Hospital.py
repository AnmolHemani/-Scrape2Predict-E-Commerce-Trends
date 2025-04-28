from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

if not os.path.exists('data_hospital'):
    os.makedirs('data_hospital')

driver = webdriver.Chrome()
query = "doctors"
file = 0
for i in range(1,13): 
    driver.get(f"https://www.practo.com/bangalore/{query}?page={i}")
    elems = driver.find_elements(By.CLASS_NAME, "listing-doctor-card")
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data_hospital/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
    time.sleep(2)
driver.close()