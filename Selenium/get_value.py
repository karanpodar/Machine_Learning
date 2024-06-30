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

# Find element by ID
Asearch = driver.find_element(By.ID, 'twotabsearchtextbox')
# Find element by XPATH
# https://www.geeksforgeeks.org/introduction-to-xpath/
Asearchgo = driver.find_element(By.XPATH, "//input[@type='submit'][@value='Go']")

if Asearch and Asearchgo:

    Asearch.send_keys('iphone 15')
    Asearchgo.click()
    
    shoe_path = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/div[1]/a/span/span[2]/span[2]')

    if shoe_path:
        print('in if', shoe_path)
        shoe_value = shoe_path.get_attribute('innerHTML')
        print(shoe_value)
    
if not debugging:
    driver.quit()   