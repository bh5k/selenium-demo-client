from selenium import webdriver

def get_driver():
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=3")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        return driver