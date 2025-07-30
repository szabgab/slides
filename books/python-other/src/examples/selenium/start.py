from selenium import webdriver
import chromedriver_autoinstaller
import sys
import re
import time

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} URL")

url = sys.argv[1]

chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
#options.add_argument('headless')
driver = webdriver.Chrome(options=options)

driver.get(url)
driver.fullscreen_window()
print(driver.title)
time.sleep(5)

box = driver.find_element_by_id('search_box')
box.send_keys("selenium")
time.sleep(5)
box.send_keys(u'\ue007')  # press enter on the box
time.sleep(5)

# element = driver.find_element_by_class_name('')
# element.is_displayed()
# print(element.get_attribute('href'))
# print(element.text)
# match = re.search(r'Code', driver.page_source)
# print(match)

# button = driver.find_element_by_class_name('')
# button.click()

#import code
#code.interact(local=locals())

#from ptpython.repl import embed
#embed(globals(), locals())


driver.close()
