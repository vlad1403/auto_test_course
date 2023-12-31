#главный файл для работы с курсом

from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

@pytest.fixture
def browser():
    browser = webdriver.Edge(EdgeChromiumDriverManager().install())
    browser.implicitly_wait(5)
    yield browser
    # browser.quit()

@pytest.mark.parametrize('id_lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test1_login(browser, id_lesson):
    link = f'https://stepik.org/lesson/{id_lesson}/step/1'
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

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
    button_submit = browser.find_element(By.CLASS_NAME, 'submit-submission')
    button_submit.click()
    #
    # expected_text = 'Correct!'
    # checkbox = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')
    # checkbox_text = checkbox.text
    # assert expected_text == checkbox_text, 'Ответ не правильный, ожидаемый текст не такой'

