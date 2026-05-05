import time
import time_conts as t

# Navigates to the leave portal
def navigate_to_leave(page):
    page.click("a[href='/web/index.php/leave/viewLeaveModule']")
    page.wait_for_url("**/leave/**", t.timeout)

# Waits for the user to apply for the leave 
def apply_for_leave(page):
    page.click("a[href='/web/index.php/leave/applyLeave']")
    page.wait_for_url("**/applyLeave**", t.timeout)

# Select the type of leave you want applied then auto fills iin dates of the leave 
    print("Selecting leave type...")
    page.locator(".oxd-select-text").first.click()
    page.locator(".oxd-select-option").first.click()

    print("Filling dates...")
    page.locator("input[placeholder='yyyy-dd-mm']").nth(0).fill("2026-04-27")
    page.locator("input[placeholder='yyyy-dd-mm']").nth(1).fill("2026-04-29")
    page.locator("textarea").fill("Personal leave request")

    print("Submitting form...")
    page.locator("button[type=submit]").click()

    time.sleep(t.minute)    