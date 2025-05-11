from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")  # Suppress console warnings (INFO, WARNING, ERROR)
options.add_argument("--headless")  # 👈 run headless in CI
options.add_argument("--no-sandbox")  # 👈 prevent sandbox issues in containers
options.add_argument("--disable-dev-shm-usage")  # 👈 prevent shared memory issues
driver = webdriver.Chrome(options=options)

try:
    # Navigate to your pie shop index.html
    driver.get("https://selenium.completeprogrammer.com/index.html")

    # Click the first 'Mark as Favorite' button
    favorite_button = driver.find_element(By.XPATH, "//button[contains(text(),'Mark as Favorite')]")
    favorite_button.click()

    # Wait a bit for the alert to appear
    time.sleep(1)

    # Switch to the alert and capture the text
    alert = Alert(driver)
    alert_text = alert.text
    print("Alert text:", alert_text)

    # Accept the alert
    alert.accept()

    # Verify expected alert text (simple assert)
    assert "added to your favorites" in alert_text

    print("✅ Test passed: Favorite alert displayed and accepted.")

except Exception as e:
    print("❌ Test failed:", e)

finally:
    # Clean up
    time.sleep(2)
    driver.quit()
