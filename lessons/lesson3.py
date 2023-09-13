from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum(a, b):
    return str(int(a)+int(b))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # находим элемент, содержащий текст
    a = browser.find_element(By.ID, "num1")
    a = a.text
    b = browser.find_element(By.ID, "num2")
    b = b.text
    c = sum(a,b)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=str(c))
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
