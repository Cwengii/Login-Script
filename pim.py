import time
import time_conts as t

def navigate_to_pim(page):
    page.click("a[href='/web/index.php/pim/viewPimModule']")
    page.wait_for_url("**/pim/**", t.timeout)

def select_first_employee(page):
    page.locator('div[class="oxd-table-card"]').nth(0).click()
    time.sleep(t.minute)
    page.locator(".oxd-table-row a").first.click()
    time.sleep(t.minute)