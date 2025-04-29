from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")  # Suppress console warnings (INFO, WARNING, ERROR)
driver = webdriver.Chrome(options=options)

try:
    # Load the login page
    driver.maximize_window()
    driver.get("https://selenium.completeprogrammer.com/login.html")
    
    # Fill in username and password
    driver.find_element(By.ID, "username").send_keys("jack")
    driver.find_element(By.ID, "password").send_keys("test1234")

    # Submit the form
    driver.find_element(By.ID, "loginButton").click()

    # Wait for result message to appear
    # Wait for the loginMessage element to become visible
    message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginMessage"))
    )

     #Get the message text and check for "Login successful!"
    message_text = message_element.text
    assert "Login successful!" in message_text, f"Login failed! Message: {message_text}"

    print("✅ Login was successful and confirmed via result message.")

finally:
    time.sleep(2)
    driver.quit()
