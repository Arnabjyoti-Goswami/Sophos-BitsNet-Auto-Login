import time
import os
from dotenv import load_dotenv

load_dotenv()
sophos_username = os.getenv('username')
sophos_password = os.getenv('password')
url = os.getenv('url')

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False # True if you want to run Chrome in headless mode

driver = webdriver.Chrome(options=options)
driver.get(url)

# Add a delay to ensure the page is loaded
time.sleep(2)

# Copy the full x-path of the input html elements using inspect element in browser
username_input_xpath = f"/html/body/font/font/font/font/div/div[1]/div[2]/div[1]/div[1]/input[1]"
password_input_xpath = f"/html/body/font/font/font/font/div/div[1]/div[2]/div[1]/div[1]/input[2]"

username_input_element = driver.find_element("xpath", username_input_xpath)
password_input_element = driver.find_element("xpath", password_input_xpath)

# Input your username and password
username_input_element.send_keys(sophos_username)
password_input_element.send_keys(sophos_password)

# Submit by clicking the 'Sign-in' button
login_button_xpath = f"/html/body/font/font/font/font/div/div[1]/div[2]/div[3]/a/div"
login_button_element = driver.find_element("xpath", login_button_xpath)
login_button_element.click()

time.sleep(1)

driver.quit()
