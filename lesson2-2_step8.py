from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os


def create_file():
    with open("test.txt", "w") as file:
      content = file.write("automationbypython") 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Kate")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Salim")
    
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@mail.ru")

    create_file()

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    
    file_element = browser.find_element(By.ID, "file")
    file_element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    time.sleep(15)
    browser.quit()

# end