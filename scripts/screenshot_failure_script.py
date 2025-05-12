#screenshot_failure_script.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")  # Suppress console warnings (INFO, WARNING, ERROR)
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://selenium.completeprogrammer.com/index.html")

except Exception as e:
    print("❌ Test failed:", e)

finally:
    # Optional: wait before closing to see result
    time.sleep(3)
    driver.quit() 