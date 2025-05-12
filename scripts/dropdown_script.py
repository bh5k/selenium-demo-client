#dropdown_script.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Setup the driver
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")  # Suppress console warnings (INFO, WARNING, ERROR)
driver = webdriver.Chrome(options=options)

try:
    # 1. Open the index page
    driver.get("https://selenium.completeprogrammer.com/index.html")

    # 2. Select 'Large' from the dropdown for Classic Apple Pie (size-1)

    # 3. Click the 'Add to cart' link for Classic Apple Pie

    # 4. Wait briefly for localStorage update
    time.sleep(1)

    # 5. Navigate to the cart page
    driver.get("https://selenium.completeprogrammer.com/cart.html")

    # 6. Verify 'Classic Apple Pie' appears in the cart items

except Exception as e:
    print("❌ Test failed:", e)

finally:
    # Optional: wait before closing to see result
    time.sleep(3)
    driver.quit()    