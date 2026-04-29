from playwright.sync_api import sync_playwright
from login import perform_login
from pim import navigate_to_pim, select_first_employee
from leave import navigate_to_leave, apply_for_leave

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            perform_login(page)
            navigate_to_pim(page)
            select_first_employee(page)
            navigate_to_leave(page)
            apply_for_leave(page)
        finally:
            browser.close()

if __name__ == "__main__":
    main()