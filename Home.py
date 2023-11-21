import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

#driver.get("https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test")
#driver.get("https://www.amazon.in/")
driver.get("https://irmp-stage.eogresources.com/dashboard")
print(driver.title)
driver.implicitly_wait(0.5)
print('Title print')
driver.close()

