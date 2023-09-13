from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '1.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # находим элемент, содержащий текст
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('firstname')
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('lastname')
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys('email')
    file_attachments = browser.find_element(By.ID, "file")
    file_attachments.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
