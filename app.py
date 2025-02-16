from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Set paths for GeckoDriver & Firefox (Portable version)
gecko_path = "/usr/local/bin/geckodriver"
firefox_path = "/usr/local/firefox/firefox"

# Configure Selenium to use the manually installed Firefox
options = Options()
options.binary_location = firefox_path

# Start WebDriver
service = Service("/usr/local/bin/geckodriver")  # ✅ This uses the manually installed GeckoDriver


# Open a test page
driver.get("https://www.google.com")
print(driver.title)

# Close browser
driver.quit()
