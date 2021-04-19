from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    #заполняем поля
    btn = browser.find_element_by_id("book")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,'price'),'100')
    )
    btn.click()

    x = browser.find_element_by_css_selector('#input_value').text
    res = calc(x)
    answ = browser.find_element_by_css_selector('#answer')
    answ.send_keys(res)
    # submit
    browser.find_element_by_css_selector('button.btn#solve').click()
except AssertionError:
    print('Test was not passed')
except Exception as ex:
    print(ex)
else:
    print('Test was passed')
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
