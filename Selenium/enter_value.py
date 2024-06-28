from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

debugging = True


# This gets the parent folder of the current project file
script_directory = Path(__file__).resolve().parent

# This joins parent folder to the chromediver path
driver_path = script_directory.joinpath("chromedriver-win64", "chromedriver.exe")

# print(driver_path)

chrome_options = Options()
if debugging:
    chrome_options.add_experimental_option('detach', True)
else:
    # To run in background when not debugging
    chrome_options.add_argument('--headless')


# We will now initiate a Selenium Service
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.amazon.in/')

Asearch = driver.find_element(By.ID, 'twotabsearchtextbox')

if Asearch:
    Asearch.send_keys('nike sneakers for men')

if not debugging:
    driver.quit()