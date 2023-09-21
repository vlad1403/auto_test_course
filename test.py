#файл для тестирования отдельных функций

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
browser.implicitly_wait(5)

link = 'https://stepik.org/lesson/236895/step/1'
browser.get(link)
button = browser.find_element(By.ID, 'ember33')
button.click()
input1 = browser.find_element(By.ID, 'id_login_email')
input1.send_keys('pankratov.v95@gmail.com')
input2 = browser.find_element(By.ID, 'id_login_password')
input2.send_keys('vlad1403vlad')
button2 = browser.find_element(By.CLASS_NAME, 'button_with-loader')
button2.click()

time.sleep(10)


answer = math.log(int(time.time()))
answer2 = str(answer)
input_answer = browser.find_element(By.CSS_SELECTOR, 'textarea.string-quiz__textarea')
input_answer.send_keys(answer2)

button_submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
button_submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
button_submit.click()