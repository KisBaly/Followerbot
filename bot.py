from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

# Log in to Twitter
username = driver.find_element_by_name("session[username_or_email]")
password = driver.find_element_by_name("session[password]")
username.send_keys("your_twitter_username")
password.send_keys("your_twitter_password")
password.send_keys(Keys.RETURN)
time.sleep(5)

# Follow a profile
driver.get("https://twitter.com/profile_name")
time.sleep(5)
follow_button = driver.find_element_by_xpath('//span[text()="Follow"]')
follow_button.click()
