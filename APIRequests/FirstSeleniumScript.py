import asserts
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import asserts

driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.google.com')
search='Selenium'
driver.find_element(By.NAME,'q').send_keys(search)
driver.find_element(By.XPATH,'//div[@class="FPdoLc lJ9FBc"]/center/input[1]').click()
asserts.assert_true(search in driver.title)

driver.close()