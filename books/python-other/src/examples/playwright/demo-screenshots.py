from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    for browser_type in [play.chromium]: #, play.firefox, play.webkit]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('http://whatsmyuseragent.org/')
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()
