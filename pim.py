import time

def navigate_to_pim(page):
    page.click("a[href='/web/index.php/pim/viewPimModule']")
    page.wait_for_url("**/pim/**", timeout=10000)

def select_first_employee(page):
    try:
        page.wait_for_selector(".oxd-table-row", timeout=15000)
        employee_links = page.locator(".oxd-table-row a")
        if employee_links.count() > 0:
            employee_links.first.click()
            time.sleep(2)
            return True
        return False
    except Exception:
        return False