import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Testsample():
     @pytest.yield_fixture()
     def f1(self):
        global driver
        driver = webdriver.Chrome()
        yield
        driver.close()

     @pytest.mark.sanity
     @pytest.mark.run(order=2)
     def test1_1(self,f1):
         #global driver
         #driver = webdriver.Firefox()
         driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C589460569891%7Cb%7Cfacebook%20signin%7C&placement=&creative=589460569891&keyword=facebook%20signin&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696221832%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-3821998899%26loc_physical_ms%3D9145227%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQjwmtGjBhDhARIsAEqfDEdNs5_boACFx0f1X1-2Jve1HjsZX9NhP6p6zF2iuXh2QRPL69esEAgaAuGMEALw_wcB")
         driver.maximize_window()
         driver.implicitly_wait(5)
         print(driver.title)

     @pytest.mark.regression
     @pytest.mark.run(order=3)
     @pytest.mark.parametrize("username,password", [("9024785662", "Manoj@796"), ("Admin123", "admin111")])
     def test2_2(self,f1,username,password):
         #global driver
         #driver = webdriver.Firefox()
         driver.get("https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjg1MzY0Nzc5LCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D")
         driver.find_element(By.XPATH, "//input[@name='email']").send_keys("username")
         driver.find_element(By.XPATH, "//input[@name='pass']").send_keys("password")
         driver.find_element(By.XPATH, "//button[@name='login']").click()

     @pytest.mark.sanity
     @pytest.mark.regression
     @pytest.mark.run(order=1)
     def test3_3(self,f1):
         #global driver
         #driver = webdriver.Firefox()
         driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C589460569891%7Cb%7Cfacebook%20signin%7C&placement=&creative=589460569891&keyword=facebook%20signin&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696221832%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-3821998899%26loc_physical_ms%3D9145227%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=Cj0KCQjwmtGjBhDhARIsAEqfDEdNs5_boACFx0f1X1-2Jve1HjsZX9NhP6p6zF2iuXh2QRPL69esEAgaAuGMEALw_wcB")
         driver.maximize_window()
         driver.implicitly_wait(5)
         driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Prahil")
         driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Prajapat")
         driver.find_element(By.XPATH, "(//input[@data-type='text'])[3]").send_keys('9024785662')
         driver.find_element(By.XPATH, "//input[@data-type='password']").send_keys("Manoj@796")
         select1 = Select(driver.find_element(By.XPATH, "//select[@name='birthday_day']"))
         select2 = Select(driver.find_element(By.XPATH, "//select[@name='birthday_month']"))
         select3 = Select(driver.find_element(By.XPATH, "//select[@name='birthday_year']"))
         select1.select_by_value("5")
         select2.select_by_index("1")
         select3.select_by_visible_text("1996")
         driver.find_element(By.XPATH, "//label[text()='Male']").click()
         time.sleep(2)
         driver.find_element(By.XPATH, "//button[@name='websubmit']").click()
         time.sleep(5)

     @pytest.mark.skip("ignored bcz not useful")
     def test4_4(self):
         print("this is fourth test case")

     @pytest.mark.run(order=4)
     def test5_5(self):
          print("this is five test case")