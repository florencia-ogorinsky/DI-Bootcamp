from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from collections import defaultdict
import datetime
import re

def scrape_bbc_tech_news():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        service = Service(executable_path=r'C:\Users\flore\OneDrive\Escritorio\DI-Bootcamp\week6\day4\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        url = "https://www.bbc.com/innovation/technology"
        driver.get(url)
        time.sleep(10)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "html.parser")
        articles_by_month = defaultdict(list)
        articles = soup.find_all("div", attrs={"data-testid": "card-text-wrapper"})
        print(f"Number of articles found: {len(articles)}")
        for article in articles:
            title_element = article.find("h2", attrs={"data-testid": "card-headline"})
            description_element = article.find("div", attrs={"data-testid": "card-description"})
            time_element = article.find("time", attrs={"datetime": True})
            if not time_element:
                parent_div = article.find_parent("div", recursive=True)
                if not parent_div:
                    parent_div = article.find_parent("div", recursive=False).find_parent("div", recursive=False)
                if parent_div:
                    time_span_elements = parent_div.find_all("span", attrs={"data-testid": "card-metadata-lastupdated"})
                    if time_span_elements:
                        time_text = time_span_elements[0].text.strip()
                        time_element = calculate_datetime(time_text)
            print(f"Title Element: {title_element}")
            print(f"Description Element: {description_element}")
            print(f"Time Element: {time_element}")
            if title_element and time_element:
                title = title_element.text.strip()
                if isinstance(time_element, datetime.datetime):
                    date_object = time_element
                else:
                    date_object = datetime.datetime.fromisoformat(time_element['datetime'])
                month_name = date_object.strftime("%B")
                articles_by_month[month_name].append(title)
                print(f"Title: {title}")
                print(f"Date: {date_object}")

        for month, titles in articles_by_month.items():
            print(f"--- {month} ---")
            for title in titles:
                print(f"- {title}")
            print()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'driver' in locals() and driver:
            driver.quit()

def calculate_datetime(time_text):
    match = re.match(r"(\d+)\s+(hour|hrs|min|mins|sec|secs|day|days)\s+ago", time_text)
    if match:
        value = int(match.group(1))
        unit = match.group(2)
        now = datetime.datetime.now(datetime.timezone.utc)
        if unit.startswith("hour"):
            return now - datetime.timedelta(hours=value)
        elif unit.startswith("min"):
            return now - datetime.timedelta(minutes=value)
        elif unit.startswith("sec"):
            return now - datetime.timedelta(seconds=value)
        elif unit.startswith("day"):
            return now - datetime.timedelta(days=value)
    return None

if __name__ == "__main__":
    scrape_bbc_tech_news()