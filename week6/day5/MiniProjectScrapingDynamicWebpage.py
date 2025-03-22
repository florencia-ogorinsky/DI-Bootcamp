from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import pandas as pd
import time

chromedriver_autoinstaller.install()
chrome_options = Options()
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.inmotionhosting.com/"
driver.get(url)
time.sleep(15) 

soup = BeautifulSoup(driver.page_source, "html.parser")
plan_cards = soup.find_all("div", class_="imh-rostrum-card")

data = []
for card in plan_cards:
    try:
        title_element = card.find("h3", class_="imh-rostrum-card-title")
        price_element = card.find("div", class_="active imh-switcher").find("span", class_="rostrum-price")
        description_element = card.find("div", class_="imh-rostrum-sub-title")

        if title_element and price_element and description_element:
            plan_name = title_element.text.strip()
            price = price_element.text.strip()
            description = description_element.text.strip()
            data.append({"Plan Name": plan_name, "Price": price, "Description": description})

    except AttributeError as e:
        pass 

df = pd.DataFrame(data)
df.to_csv("hosting_plans.csv", index=False)
print(df)

driver.quit()