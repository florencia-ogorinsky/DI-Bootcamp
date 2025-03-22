from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def scrape_bbc_weather(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        service = Service(executable_path=r'C:\Users\flore\OneDrive\Escritorio\DI-Bootcamp\week6\day4\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".wr-day-carousel__list"))
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")

        days = soup.select(".wr-day-carousel__list .wr-day")

        data = []
        for day in days:
            try:
                date_long = day.select_one(".wr-date__long")
                date_longish = day.select_one(".wr-date__longish")

                if date_long:
                    date = date_long.text.strip()
                elif date_longish:
                    day_of_week = date_longish.contents[0].strip()  # Extract "Fri"
                    day_of_month = day.select_one(".wr-date__longish__dotm").text.strip()  # Extract "4th"
                    date = f"{day_of_week} {day_of_month}"  # Combine them
                else:
                    date = "Unknown Date"

                temp_high_element = day.select_one(".wr-day-temperature__high .wr-value--temperature--c")
                temp_high = temp_high_element.text.replace("°", "").strip() if temp_high_element else None

                temp_low_element = day.select_one(".wr-day-temperature__low .wr-value--temperature--c")
                temp_low = temp_low_element.text.replace("°", "").strip() if temp_low_element else None

                condition_element = day.select_one(".wr-day__details__weather-type-description")
                condition = condition_element.text.strip() if condition_element else None

                if date and temp_high and temp_low and condition:
                    data.append({"Date": date, "High Temp": temp_high, "Low Temp": temp_low, "Condition": condition})
                else:
                    print(f"Missing data for day: {date}")

            except Exception as e:
                print(f"Error extracting data from a day: {e}")

        return pd.DataFrame(data)

    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        return None
    finally:
        if 'driver' in locals() and driver:
            driver.quit()

def analyze_and_visualize(df):
    if df is None or df.empty:
        print("No data to analyze.")
        return

    df["High Temp"] = df["High Temp"].astype(int)
    df["Low Temp"] = df["Low Temp"].astype(int)

    print("Average High Temperature:", df["High Temp"].mean())
    print("Average Low Temperature:", df["Low Temp"].mean())
    print("Most Common Condition:", df["Condition"].mode()[0])

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="Date", y="High Temp", label="High Temp")
    sns.lineplot(data=df, x="Date", y="Low Temp", label="Low Temp")
    plt.title("Temperature Trends in Tel Aviv")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x="Condition")
    plt.title("Weather Condition Distribution in Tel Aviv")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    url = "https://www.bbc.com/weather/293397"
    df = scrape_bbc_weather(url)
    analyze_and_visualize(df)