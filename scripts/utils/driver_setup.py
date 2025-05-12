from selenium import webdriver

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)
