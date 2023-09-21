from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
import unittest


class TestAbs(unittest.TestCase):

    def fill_forms(self, url):
        self.browser = webdriver.Edge(EdgeChromiumDriverManager().install())
        self.browser.get(url)
        self.browser.find_element(By.CSS_SELECTOR, 'input.first:required').send_keys("Elena")
        self.browser.find_element(By.CSS_SELECTOR, 'input.second:required').send_keys("Drigant")
        self.browser.find_element(By.CSS_SELECTOR, 'input.third:required').send_keys("testest@gmail.com")
        self.browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
        sleep(3)
        return self.browser.find_element(By.TAG_NAME, 'h1').text

    def test_url1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual(self.fill_forms(link), 'Congratulations! You have successfully registered!', 'Registration error')
        self.browser.quit()

    def test_url2(self):
        link1 = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual(self.fill_forms(link1), 'Congratulations! You have successfully registered!', 'Registration error')
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()