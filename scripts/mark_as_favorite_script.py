#mark_as_favorite_script.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")  # Suppress console warnings (INFO, WARNING, ERROR)
driver = webdriver.Chrome(options=options)

try:
    # Navigate to your pie shop index.html
    driver.get("https://selenium.completeprogrammer.com/index.html")





except Exception as e:
    print("❌ Test failed:", e)

finally:
    # Clean up
    time.sleep(2)
    driver.quit()
