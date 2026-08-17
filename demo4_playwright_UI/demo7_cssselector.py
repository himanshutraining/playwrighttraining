from playwright.sync_api import sync_playwright
import time

def handle_dialog(dialog):
    print(dialog.message)
    dialog.accept()

with sync_playwright() as p:
    browser=p.chromium.launch(channel="chrome",headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.salesforce.com/in/sales/free-trial/ee/")
    page.locator("css=input[name='firstName']").fill("john")
    page.locator("select[name='employees']").select_option(label="6-30 employees")
    page.get_by_text("I agree to the Main Services Agreement").click()
    time.sleep(5)