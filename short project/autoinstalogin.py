from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('D:/chromedriver')
driver.get('https://www.instagram.com/')
sleep(2)

driver.maximize_window()
driver.get('https://www.instagram.com/account/login/?source=auth_switcher')
sleep(2)

driver.find_element_by_namey("username").send_keys('_mayank__dhodi_')
sleep(2)

driver.find_element_by_name("password").send_keys('9528499374')
sleep(2)

driver.find_element_by_name("password").send_keys(u'\ue007')
sleep(2)