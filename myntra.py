import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path= r"C:\Users\Sandy\Downloads\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.myntra.com/")
driver.implicitly_wait(20)
driver.find_element(by=By.XPATH, value ='//div/input[@class="desktop-searchBar"]').send_keys("shoes for men")
time.sleep(10)
driver.find_element (by=By.CSS_SELECTOR, value= 'a.desktop-submit').click()
time.sleep(10)
driver.find_element(by=By.XPATH, value = '//li/label[text()="Casual Shoes"]').click()
time.sleep(40)

shoename = driver.find_elements(by=By.CLASS_NAME, value= "product-brand")
shoeprice = driver.find_elements(by=By.XPATH, value = '//div[@class="product-price"]')
description = driver.find_elements(by=By.XPATH, value= '//div/h4[@class = "product-product"]')

for name in shoename:
    print(name.text)

for price in shoeprice:
    print(price.text)

for desc in description:
    print(desc.text)
