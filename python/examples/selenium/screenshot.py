from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

url = 'https://code-maven.com/'
driver.get(url)
print(driver.title)
driver.get_screenshot_as_file('code-maven.png')
driver.close()