from selenium.webdriver.common.by import By
import time

from utils.driver_setup import create_driver

# Setup the driver
driver = create_driver()

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
