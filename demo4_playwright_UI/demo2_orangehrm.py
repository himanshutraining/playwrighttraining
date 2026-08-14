from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
   browser=p.chromium.launch(channel="chrome", headless=False)
   context=browser.new_context()
   page=context.new_page()

   page.goto("https://www.orangehrm.com/book-a-free-demo")
   time.sleep(5)

   page.locator("xpath=//button[text()='Allow all']").click()
   time.sleep(2)

   page.locator("xpath=//input[@id='Form_getForm_FullName']").fill("John Wick")
   time.sleep(2)
   page.locator("xpath=//input[@id='Form_getForm_Email']").fill("abc@xyz.com")
   time.sleep(2)
   page.locator("xpath=//input[@id='Form_getForm_Contact']").fill("1234567890")
   time.sleep(2)
   page.locator("xpath=//input[@id='Form_getForm_JobTitle']").fill("Manager")
   time.sleep(2) 
   page.locator("xpath=//input[@id='Form_getForm_CompanyName']").fill("ABCCorporation")
   time.sleep(2) 
   page.locator("xpath=//select[@id='Form_getForm_Country']").select_option(label="India ")
   time.sleep(2)
   page.locator("xpath=//select[@id='Form_getForm_NoOfEmployees']").select_option(label="51 - 200")


   time.sleep(5)
