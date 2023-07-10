# Открыть страницу https://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


try:
    link = "https://suninjuly.github.io/selects1.html"
    # link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получение чисел и их суммирование
    x1 = int(browser.find_element(By.ID, "num1").text)
    x2 = int(browser.find_element(By.ID, "num2").text)
    y = str(x1 + x2)
    # Раскрытие выпадающего списка
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    # Выбор нужного элемента
    select.select_by_value(y)
    # Отправляем заполненную форму
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()