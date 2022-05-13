import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(executable_path= r"C:\Users\Sandy\Downloads\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.myntra.com/")
driver.implicitly_wait(20)
driver.find_element(by=By.XPATH, value ='//div/input[@class="desktop-searchBar"]').send_keys("shoes for men")
time.sleep(5)
driver.find_element (by=By.CSS_SELECTOR, value= 'a.desktop-submit').click()
time.sleep(5)
driver.find_element(by=By.XPATH, value = '//li/label[text()="Casual Shoes"]').click()
time.sleep(40)

Brand = driver.find_elements_by_class_name("product-brand")
Price = driver.find_elements_by_xpath('.//div[@class="product-price"]')
description = driver.find_elements_by_xpath('.//div/h4[@class = "product-product"]')

scraped_data=[]

for i in range(len(Brand)):
    scrap_info = {
        'Brand' : Brand [i].text,
        'Price': Price [i]. text,
        'Description': description [i].text
    }
    scraped_data.append(scrap_info)

df = pd.DataFrame(scraped_data)

df.to_csv('Myntra_Scraped_Data.csv', index=False)

#for i in range(len(shoename)):




#with open ('Myntra_CS_Data.csv', 'a') as file:
    
 #       file.write(shoename[i].text + ";" + shoeprice[i].text + ";" + description[i].text + "\n")

#for name in shoename:
 #   print(name.text)

#for price in shoeprice:
 #   print(price.text)

#for desc in description:
 #   print(desc.text)
