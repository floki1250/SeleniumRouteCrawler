import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from multiprocessing import Pool
import json
import time
import os

def get_title_selenium(url):
    driver.get(url)
    title = driver.title.strip() if driver.title else None
    return title

def fetch_title(route):
    current_url = f"{base_url}{route}"
    response = requests.head(current_url)

    if response.status_code == 200:
        title = get_title_selenium(current_url)
        return {
            "route": current_url,
            "title": title
        }
    else:
        return None

def find_routes_with_selenium(base_url, routes):
    with Pool(concurrent_processes) as pool:
        results = pool.map(fetch_title, routes)

    return [result for result in results if result is not None]

def save_to_json(data, filename):
    with open(filename, 'a', encoding='utf-8') as json_file:
        for item in data:
            json.dump(item, json_file, ensure_ascii=False)
            json_file.write('\n')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <base_url> <start_range> <end_range>")
        sys.exit(1)

    base_url = sys.argv[1]
    start_range = int(sys.argv[2])
    end_range = int(sys.argv[3])

    output_file = "api_routes.json"
    concurrent_processes = 4  # Adjust the number of concurrent processes as needed

    # Create a reusable Chrome WebDriver instance
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    routes = list(range(start_range, end_range + 1))

    start_time = time.time()

    all_routes = find_routes_with_selenium(base_url, routes)
    save_to_json(all_routes, output_file)

    # Close the WebDriver instance after use
    driver.quit()

    end_time = time.time()
    duration = end_time - start_time

    print(f"Routes and titles appended to {output_file}")
    print(f"Script execution time: {duration:.2f} seconds")
