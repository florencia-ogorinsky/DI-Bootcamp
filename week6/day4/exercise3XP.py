from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def scrape_rotten_tomatoes():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        service = Service(executable_path=r'C:\Users\flore\OneDrive\Escritorio\DI-Bootcamp\week6\day4\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        url = "https://www.rottentomatoes.com/browse/movies_at_home/affiliates:netflix~critics:certified_fresh"
        driver.get(url)
        time.sleep(10)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "html.parser")
        movie_containers = soup.find_all("div", class_="js-tile-link")
        movies = []
        for container in movie_containers:
            title_element = container.find("span", class_="p--small")
            score_element = container.find("score-pairs-deprecated")
            release_date_element = container.find("span", class_="smaller")
            title = title_element.text.strip() if title_element else "N/A"
            critic_score = score_element.find("rt-text", slot="criticsScore").text.strip() if score_element.find("rt-text", slot="criticsScore") else "N/A"
            audience_score = score_element.find("rt-text", slot="audienceScore").text.strip() if score_element.find("rt-text", slot="audienceScore") else "N/A"
            release_date = release_date_element.text.strip() if release_date_element else "N/A"
            movies.append({"title": title, "critic_score": critic_score, "audience_score": audience_score, "release_date": release_date})
        for movie in movies:
            print(f"Title: {movie['title']}")
            print(f"Critic Score: {movie['critic_score']}")
            print(f"Audience Score: {movie['audience_score']}")
            print(f"Release Date: {movie['release_date']}")
            print("-" * 20)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'driver' in locals() and driver:
            driver.quit()

if __name__ == "__main__":
    scrape_rotten_tomatoes()