from selenium import webdriver

driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("https://www.google.com/")  
driver.find_element(by='id', value='input').send_keys("javatpoint")
driver.close()  