from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(channel="chrome", headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.google.com")

    actual_title=page.title()
    print(actual_title)







