from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
   browser=p.chromium.launch(channel="chrome", headless=False)
   context=browser.new_context()
   page=context.new_page()

   page.goto("https://www.online.citibank.co.in")
   time.sleep(5)

   if page.locator("xpath=//button[@id='onetrust-accept-btn-handler']").count()>0:
            page.locator("xpath=//button[@id='onetrust-accept-btn-handler']").click()

   page.locator("xpath=//div[text()='My Account']").hover()
   time.sleep(5)

   with page.expect_popup() as popup_info:
           page.locator("xpath=//div[text()='Banking with Citi']").click()

   time.sleep(5)

