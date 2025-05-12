import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from utils.driver_setup import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_add_classic_apple_pie_to_cart(driver):
    # 1. Open the index page
    driver.get("https://selenium.completeprogrammer.com/index.html")

    # 2. Select 'Large' from the dropdown for Classic Apple Pie (size-1)
    size_dropdown = Select(driver.find_element(By.ID, "size-1"))
    size_dropdown.select_by_visible_text("Large")

    # 3. Click the 'Add to cart' link for Classic Apple Pie
    #add_to_cart_link = driver.find_element(By.XPATH, "//a[contains(text(), '+ Add to cart') and contains(@onclick, 'id: 1')]")
    add_to_cart_link = driver.find_element(By.CSS_SELECTOR, "a.add-to-cart-link[data-id='1']")

    add_to_cart_link.click()

    # 4. Wait briefly for localStorage update
    time.sleep(1)

    # 5. Navigate to the cart page
    driver.get("https://selenium.completeprogrammer.com/cart.html")

    # 6. Verify 'Classic Apple Pie' appears in the cart items
    cart_items_div = driver.find_element(By.ID, "cartItems")
    assert "Classic Apple Pie" in cart_items_div.text, "Pie not found in cart!"

    print("Test passed: Classic Apple Pie with selected size and it should be Large added to cart successfully.")

