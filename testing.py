from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://prereg.techno-associates.live/#/eng")

# Find the login elements and perform actions
contact = driver.find_element(by='id', value='inputFieldContact')

login_button = driver.find_element(by='xpath', value='/html/body/app-root/app-header/mat-sidenav-container/mat-sidenav-content/main/app-login/div[1]/div/form/mat-card/div[2]/button')
# Enter the login credentials
contact.send_keys("respernyivuru@gmail.com")

# Click the login button
login_button.click()

# Add a small delay to allow page loading (optional)
time.sleep(10)

# Close the browser
driver.quit()