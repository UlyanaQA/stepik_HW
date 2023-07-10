# Задание
# Открыть страницу https://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку Submit.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получение рандомного х
    x_element = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    # Расчет х
    y = calc(x_element)
    # Ввод ответа и чекбокса с радиобаттоном
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    # Отправляем заполненную форму
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
    print(calc(17))

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()