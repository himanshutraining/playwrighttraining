from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser=p.chromium.launch(channel="chrome",headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://app.thetestingacademy.com/playwright/frames/")
    # enter Vehicle name as creta 
    page.locator("xpath=//input[@id='RESULT_TextField-1']").fill("Creta")
    time.sleep(5)
    browser.close()