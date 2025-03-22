from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import statistics

def scrape_weather_data():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        service = Service(executable_path=r'C:\Users\flore\OneDrive\Escritorio\DI-Bootcamp\week6\day4\chromedriver.exe')  # Reuse path from Exercise 4
        driver = webdriver.Chrome(service=service, options=chrome_options)
        url = "https://www.accuweather.com/en/us/attica/30607/weather-forecast/2139413"
        driver.get(url)
        time.sleep(10)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, "html.parser")
        
        temperatures = []
        conditions = []
        humidity_values = []
        
        forecast_items = soup.find_all("div", class_="forecast-card")
        for item in forecast_items:
            temp = item.find("span", class_="temp")
            condition = item.find("div", class_="condition")
            humidity = item.find("div", class_="humidity")
            
            if temp and condition and humidity:
                temperature = temp.text.strip()
                condition_text = condition.text.strip()
                humidity_text = humidity.text.strip()
                
                try:
                    temp_value = int(temperature.split("°")[0].strip())
                    temperatures.append(temp_value)
                except ValueError:
                    pass
                
                conditions.append(condition_text)
                humidity_values.append(humidity_text)
        
        avg_temperature = statistics.mean(temperatures) if temperatures else 0
        most_common_condition = statistics.mode(conditions) if conditions else "No data"
        
        print(f"Average Temperature: {avg_temperature}°F")
        print(f"Most Common Weather Condition: {most_common_condition}")
        print(f"Humidity Values: {humidity_values}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'driver' in locals() and driver:
            driver.quit()

if __name__ == "__main__":
    scrape_weather_data()
