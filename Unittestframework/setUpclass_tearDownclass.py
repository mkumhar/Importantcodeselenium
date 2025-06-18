import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class HRMapplication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver=webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.facebook.com/")
        print("Hi welcome to the facebook page")

    def test_loginvlidatwion(self):
        driver.find_element(By.ID, 'email').send_keys("manojkumhar")
        driver.find_element(By.ID, 'pass').send_keys("manoj796")
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        print('this is login page')

    def test_titlevalidation(self):
        print(driver.title)
        print('this is a title validation')

    @classmethod
    def tearDownClass(cls):
        print('closure page')
        driver.close()


if __name__ == '__main__':
     unittest.main()