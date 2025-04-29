# 🧪 Selenium Demo Client

This project contains example Selenium WebDriver scripts for automating interactions with a sample web app hosted at [https://selenium.completeprogrammer.com](https://selenium.completeprogrammer.com). It is part of the *Browser Automation with Selenium* video course.

---

## 🚀 Getting Started (macOS + Homebrew)

This guide sets up your local Python environment with Selenium, Chrome, and ChromeDriver.

### 🧰 Prerequisites

- macOS with [Homebrew](https://brew.sh)
- Python 3.12+ (via Homebrew)
- Google Chrome

---

### 🛠️ Step 1: Install System Dependencies

```bash
brew install python
brew install --cask google-chrome
brew install --cask chromedriver

### 🛠️ Step 2: Create Python env

python3 -m venv selenium-env
source selenium-env/bin/activate

### 🛠️ Step 3: Install Selenium

pip install -r requirements.txt

