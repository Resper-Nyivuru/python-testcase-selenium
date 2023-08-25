from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the website
driver.get("https://prereg.techno-associates.live/#/eng")

# Find the login elements and perform actions
contact = driver.find_element_by_id("inputFieldContact")
#password_field = driver.find_element_by_id("password")
login_button = driver.find_element_by_xpath("/html/body/app-root/app-header/mat-sidenav-container/mat-sidenav-content/main/app-login/div[1]/div/form/mat-card/div[2]/button")

# Enter the login credentials
contact.send_keys("respernyivuru@gmail.com")
#password_field.send_keys("your_password")

# Click the login button
login_button.click()

# Add a small delay to allow page loading (not recommended in actual tests)
#time.sleep(3)

# Verify successful login
welcome_message = driver.find_element_by_id("welcome_message").text
assert "Welcome" in welcome_message, "Login failed"

# Close the browser
driver.quit()