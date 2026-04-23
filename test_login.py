from playwright.sync_api import sync_playwright
import time

def test_login():

    # 1: Setup browser and login
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        
        page.fill("input[name=username]", "Admin")
        page.fill("input[name=password]", "admin123")
        page.click("button[type=submit]")

        # Wait for dashboard
        page.wait_for_url("**/dashboard**", timeout=15000)

        # 2: Go to PIM 
        page.click("a[href='/web/index.php/pim/viewPimModule']")
        page.wait_for_url("**/pim/**", timeout=10000)

        # 3: Click first employee in the list
        page.wait_for_selector(".oxd-table-row", timeout=10000)  
        page.locator(".oxd-table-row a").first.click()
        time.sleep(2)

        # 4: Go to Leave module
        page.click("a[href='/web/index.php/leave/viewLeaveModule']")
        page.wait_for_url("**/leave/**", timeout=10000)

        # 5: Apply for leave
        page.click("a[href='/web/index.php/leave/applyLeave']")
        page.wait_for_url("**/applyLeave**", timeout=10000)

        # 6: Fill leave application form
        print("Selecting leave type...")
        page.locator(".oxd-select-text").first.click()
        page.locator(".oxd-select-option").first.click()

        # Enter dates 
        print("Filling dates...")
        page.locator("input[placeholder='yyyy-dd-mm']").nth(0).fill("2026-04-27") 
        page.locator("input[placeholder='yyyy-dd-mm']").nth(1).fill("2026-04-29")             
        page.locator("textarea").fill("Personal leave request")
        print("Submitting form...")
        page.locator("button[type=submit]").click()

        time.sleep(5)
        browser.close()

if __name__ == "__main__":
    test_login()