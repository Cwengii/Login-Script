import time

def navigate_to_pim(page):
    page.click("a[href='/web/index.php/pim/viewPimModule']")
    page.wait_for_url("**/pim/**", timeout=10000)

def select_first_employee(page):
    page.wait_for_selector(".oxd-table-row", timeout=10000)
    page.locator(".oxd-table-row a").first.click()
    time.sleep(2)