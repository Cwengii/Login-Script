import time

def navigate_to_leave(page):
    page.click("a[href='/web/index.php/leave/viewLeaveModule']")
    page.wait_for_url("**/leave/**", timeout=10000)

def apply_for_leave(page):
    try:
        page.click("text=Apply")
        page.wait_for_url("**/applyLeave**", timeout=10000)
        fill_leave_form(page)
        return True
    except Exception as e:
        print(f"  Could not apply for leave: {e}")
        return False

def fill_leave_form(page):
    try:
        page.wait_for_selector(".oxd-form-loader", state="hidden", timeout=20000)
        select_box = page.locator(".oxd-select-text").first
        select_box.wait_for(timeout=10000)
        select_box.click()
        option = page.locator(".oxd-select-option").first
        option.wait_for(timeout=10000)
        option.click()

        date_fields = page.locator("input[placeholder='yyyy-dd-mm']")
        date_fields.nth(0).fill("2026-04-27")
        date_fields.nth(1).fill("2026-04-29")
        page.locator("textarea").fill("Personal leave request")

        submit_button = page.locator("button[type=submit]").first
        submit_button.wait_for(timeout=10000)
        submit_button.click()
        time.sleep(3)
    except Exception as e:
        print(f"  Could not fill leave form: {e}")
    