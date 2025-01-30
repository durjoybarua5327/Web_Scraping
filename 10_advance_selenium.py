from selenium import webdriver

 # Import Service class to manage ChromeDriver
from selenium.webdriver.chrome.service import Service 
import time

# Path to ChromeDriver executable
path = "K:/chromedriver-win64/chromedriver.exe"

# Create a Service object for ChromeDriver
s = Service(path)

# Initialize Chrome WebDriver using the Service object
driver = webdriver.Chrome(service=s)  

# Navite to Google homepage
driver.get("https://www.google.com/")  

# Locate Google search box using XPath

box = driver.find_element_by_xpath('//*[@id="APjFqb"]')

# Type "house of dragon" into the search box
box.send_keys("house of dragon")

# Submit the search form 
box.submit()

time.sleep(2)  

driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[6]/div/div/div/div/div/div[1]/div/div/span/a').click() 

time.sleep(2)

driver.save_screenshot("F:/Web_Scraping/1st.png")
