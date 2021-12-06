from selenium import webdriver
import chromedriver_autoinstaller
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} URL")

url = sys.argv[1]

chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

driver.get(url)
print(driver.title)
driver.get_screenshot_as_file('screenshot.png')
driver.close()
