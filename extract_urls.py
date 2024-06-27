from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import mysql.connector

# Function to initialize the web driver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

# Function to perform Google search and extract URLs
def extract_urls(query, num_urls):
    driver = init_driver()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    urls = []
    while len(urls) < num_urls:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for a in soup.find_all('a', href=True):
            href = a['href']
            if "arcgis/rest/services" in href and href not in urls:
                urls.append(href)
        try:
            next_button = driver.find_element(By.ID, "pnnext")
            next_button.click()
            time.sleep(2)
        except:
            break
    
    driver.quit()
    return urls[:num_urls]

# Function to save URLs to a CSV file
def save_to_csv(urls, filename):
    df = pd.DataFrame(urls, columns=["URL"])
    df.to_csv(filename, index=False)

# Function to save URLs to MySQL database
def save_to_mysql(urls, db_config):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS urls (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(2083))")
    for url in urls:
        cursor.execute("INSERT INTO urls (url) VALUES (%s)", (url,))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    query = "https://*/arcgis/rest/services"
    num_urls = 1000
    urls = extract_urls(query, num_urls)

    # Save to CSV
    save_to_csv(urls, "arcgis_urls.csv")

    # Save to MySQL
    db_config = {
        'user': 'arcgis_user',
        'password': '@Aditya82',
        'host': 'localhost',
        'database': 'arcgis_db'
    }
    save_to_mysql(urls, db_config)
