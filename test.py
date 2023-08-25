from selenium import webdriver

driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("https://www.google.com/")  
driver.find_element_by_id("input").send_keys("javatpoint")
#driver.find_element()  