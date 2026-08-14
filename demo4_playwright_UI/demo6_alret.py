from playwright.sync_api import sync_playwright
import time

def handle_dialog(dialog):
    print(dialog.message)
    dialog.accept()

with sync_playwright() as p:
    browser=p.chromium.launch(channel="chrome",headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://www.nasscom.in/nasscom-membership")
    time.sleep(5)
    #page.on("dialog",handle_dialog)
    #page.locator("xpath=//a[text()='Calculate Fee']").click()
    #time.sleep(5)

    page.locator("xpath=//input[@type='file' and @id='edit-field-additional-document-0-upload']").set_input_files(r"C:\TestData.docx")



    time.sleep(5)
    browser.close()