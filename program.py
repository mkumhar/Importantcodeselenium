'''s=input("Enter any string:")
rev=s[::-1]
print("reverse string is:",rev)

s=input("Enter any string:")
r=reversed(s)
output="".join(r)
print(output)
output1=output.replace(" ","")
print(output1)

s=input("Enter any string:")
i=len(s)-1
print(i)
output=''
while i>=0:
    output=output+s[i]
    i=i-1
print(output)


s=input("Enter any string:")
i=len(s)-1
print(i)
output=''
while i>=0:
    output=output+s[i]
    i=i-1
print(output)
if s==output:
    print("given string is palindrome")
else:
    print("given string is not palindrome")

s1=input("enter the string:")
l=("".join(sorted(s1)))
print(l)
s2=input("enter the string:")
m=("".join(sorted(s2)))
print(m)
if l==m:
	print("string are anagrams")
else:
    print("string are not anagrams")

s=input("Enter any string:")
l=s.split()
output=[]
for i in l:
    if i not in output:
        output.append(i)
print(" ".join(output))


driver = webdriver.Chrome()
# 2. Copy the title of the page
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
page_title = driver.title
print("original Page title is:",page_title)
driver.find_element(By.XPATH,"//button[text()='    click   ']").click()
time.sleep(2)
windows=driver.window_handles
driver.switch_to.window(windows[1])
print("New window title is:",driver.title)
time.sleep(2)
#driver.find_element(By.XPATH,"//input[@type='text']").send_keys(page_title)
driver.switch_to.window(windows[0])
print("primary window title is:",driver.title)
time.sleep(2)
driver.switch_to.window(windows[1])
time.sleep(2)
driver.close()
driver.quit()'''
import driver
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.window import WindowTypes
import time

from urllib3 import request
'''
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for link in links:
    #print(link.text)
    href=link.get_attribute("href")
    response=requests.get(href)
    if response.status_code>=400:
        print("broken link is",href,"and response code is",response.status_code)
driver.quit() 

import time

from selenium import webdriver

from selenium.webdriver import ActionChains

from selenium.webdriver.common import keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com")

# driver.find_element(By.ID,"name").send_keys("Nikhil")

print(driver.current_url)
driver.implicitly_wait(10)
assert "Automation Testing" in driver.title
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Pradeep")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("raj@gmail.com")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("564656654")
driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("Hyderabad")
static_webtable = driver.find_element(By.XPATH, "//h2[text()='Static Web Table']")
driver.execute_script("arguments[0].scrollIntoView();", static_webtable)
time.sleep(3)

# particular column data
price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[4]")
print(price.text)
subject = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[4]/td[3]")
print(subject.text)

# Entire row data
row_data = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td")
for data in row_data:
    print(data.text)

# total_columns
len_column = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[6]/td")
total_columns = len(len_column)

# total_rows
len_row = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
total_rows = len(len_row)

# entire column data
for row in range(2, total_rows + 1):
    entir_price_column = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(row) + "]/td[4]")
    print(entir_price_column.text)

# entire table data
for row in range(2, total_rows + 1):

    for column in range(1, total_columns + 1):
        table_data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(row) + "]/td[" + str(
            column) + "]")

        print(table_data.text, end=" ")

    print()
    

#dynamic web table
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com")
print(driver.current_url)
driver.implicitly_wait(10)
assert "Automation Testing" in driver.title
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Pradeep")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("raj@gmail.com")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("564656654")
driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("Hyderabad")
dynamic_webtable = driver.find_element(By.XPATH, "//h2[text()='Dynamic Web Table']")
driver.execute_script("arguments[0].scrollIntoView();", dynamic_webtable)
time.sleep(3)

#Particular data
disk=driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr[1]/td[4]")
print(disk.text)
Memory=driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr[4]/td[2]")
print(Memory.text)

#Total rows
rows=driver.find_elements(By.XPATH,"//table[@id='taskTable']/tbody/tr")
print(len(rows))
len_row=len(rows)

#Total columns
columns=driver.find_elements(By.XPATH,"//table[@id='taskTable']/tbody/tr/td[1]")
print(len(columns))
len_colm=len(columns)

#Entire rows data
entire_rows_data=driver.find_elements(By.XPATH,"//table[@id='taskTable']/tbody/tr")
for data in entire_rows_data:
    print(data.text)

#Entire columns data
for row in range(1, len_row + 1):
    entir_memory_column = driver.find_element(By.XPATH, "//table[@id='taskTable']/tbody/tr[" + str(row) + "]/td[1]")
    print(entir_memory_column.text)

#Entire table
l=[]
for row in range(1, len_row + 1):
    for column in range(1,len_colm+1):
        entire_data=driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr[" + str(row) + "]/td[" +str(column)+ "]")
        print(entire_data.text,end=" ")
    print()

driver.quit()

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for link in links:
    #print(link.text)
    href=link.get_attribute("href")
    response=requests.get(href)
    if response.status_code>=400:
        print("broken link is",href,"and response code is",response.status_code)
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com")
#driver.find_element(By.ID,"name").send_keys("Nikhil")
print (driver.current_url)
driver.implicitly_wait(10)
assert "Automation Testing" in driver.title
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Pradeep")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("raj@gmail.com")
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("564656654")
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("Hyderabad")
date_picker= driver.find_element(By.XPATH,"//input[@id='datepicker']")
driver.execute_script("arguments[0].scrollIntoView();",date_picker)
date_picker.click()
time.sleep(3)
#choosing specific date - 18th June
date1= driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[4]")
print (date1.text)
#date1.click()
time.sleep(3)
# Choosing a date from iterating calendar
total_rows= driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr")
print(len(total_rows))
total_columns=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td/a")

for row in range(1,len(total_rows)):
   for column in range(1,len(total_columns)+1):
       date_needed = '18'
       date=driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr["+str(row)+"]/td["+str(column)+"]/a")
       print(date.text)
       if date.text == date_needed:
           date.click()
       else:
           pass
time.sleep(3)


from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()
time.sleep(3)
date=driver.find_element(By.ID,"datepicker1").click()

time.sleep(2)
#date_picker=driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td[3]")
#date_picker.click()
time.sleep(2)
total_rows=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr")
rows=print(len(total_rows))
total_col=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr[3]/td")
colms=print(len(total_col))
for row in range(1,len(total_rows)+1):
    for column in range(1,len(total_col)+1):
        date_needed = '18'
        date1=driver.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr["+str(row)+"]/td["+str(column)+"]")
        print(date1.text)
        if date1.text == date_needed:
            date1.click()
        else:
            pass
        time.sleep(3)
driver.quit()

'''
