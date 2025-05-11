from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")  # Suppress console warnings (INFO, WARNING, ERROR)
options.add_argument("--headless")  # 👈 run headless in CI
options.add_argument("--no-sandbox")  # 👈 prevent sandbox issues in containers
options.add_argument("--disable-dev-shm-usage")  # 👈 prevent shared memory issues
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://selenium.completeprogrammer.com")
    
    add_to_cart_link = driver.find_element(By.CSS_SELECTOR, "a.add-to-cart-link[data-id='1']")
    add_to_cart_link.click()
    time.sleep(1)
    driver.get("https://selenium.completeprogrammer.com/cart.html")
    cart_items_div = driver.find_element(By.ID, "cartItems")

    #this should fail
    assert "Humble Pie" in cart_items_div.text, "Pie not found in cart!"

except Exception as e:
    print(f"Test failed: {e}")
    driver.save_screenshot("screenshot_failure.png")

finally:
    driver.quit()
