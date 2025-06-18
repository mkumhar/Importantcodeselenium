import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class HRMapplication(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")

    def test_loginvlidatwion(self):
        self.driver.find_element(By.ID, 'email').send_keys("manojkumhar")
        self.driver.find_element(By.ID, 'pass').send_keys("manoj796")
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    def test_titlevalidation(self):
        print(self.driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ =='__main__':
        unittest.main()