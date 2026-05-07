import time_conts as t

def navigate_to_pim(page):
    page.click("a[href='/web/index.php/pim/viewPimModule']")
    page.wait_for_url("**/pim/**", timeout=t.timeout)

def select_first_employee(page):
    # Wait for the employee table to load, then click the first employee's name link
    page.locator(".oxd-table-row a").first.click()
    page.wait_for_url("**/pim/viewPersonalDetails/**", timeout=t.timeout)