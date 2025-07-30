from playwright.sync_api import sync_playwright
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} URL")

url = sys.argv[1]

with sync_playwright() as play:
    for browser_type in [play.chromium]: #, play.firefox, play.webkit]:
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        search_box = page.query_selector("#search_box");

        #from ptpython.repl import embed
        #embed(globals(), locals())


        #page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()

