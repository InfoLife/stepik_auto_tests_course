from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(treasure_result):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    treasure = browser.find_element(By.ID, "treasure")
    find_treasure = treasure.get_attribute("valuex")
    x = find_treasure
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
    #input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    #input1.send_keys("check")
    #input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    #input2.send_keys("check")
    #input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    #input3.send_keys("check")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
