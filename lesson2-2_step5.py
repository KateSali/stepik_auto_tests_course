from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
  browser = webdriver.Chrome()
  link = "https://SunInJuly.github.io/execute_script.html"
  browser.get(link)
  button = browser.find_element(By.TAG_NAME, "button")
  button.click()
finally:
    time.sleep(10)
    browser.quit()

#end
