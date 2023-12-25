from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "form[action='#'] :nth-child(6) [type='submit']")
button.click()

# input1 = browser.find_element(By.CSS_SELECTOR, "form[action='#'] :nth-child(1) input")
# input1.send_keys("Ivan")
