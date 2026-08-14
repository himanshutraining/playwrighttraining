from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
   browser=p.chromium.launch(channel="chrome", headless=False)
   context=browser.new_context()
   page=context.new_page()

   page.goto("https://www.orangehrm.com/book-a-free-demo")
   time.sleep(5)
   if page.locator("xpath=//button[text()='Allow all']").count()>0:
         page.locator("xpath=//button[text()='Allow all']").click()
   time.sleep(2)

   #AI Helpdesk click logic

   with page.expect_popup() as popup_info:
        page.locator("xpath=//a[normalize-space()='AI Help Desk']").click()

   new_page=popup_info.value

   new_page.locator("xpath=//input[@id='chat-input']").fill("Hello")
   
   time.sleep(5)

   print(page.title())

   browser.close()

