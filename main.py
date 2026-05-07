from playwright.sync_api import sync_playwright
from login import perform_login
from pim import navigate_to_pim, select_first_employee
from leave import navigate_to_leave, apply_for_leave
import logs

def main():
    logs.log_script_started()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        try:
            perform_login(page)
            logs.log_login_success()

            navigate_to_pim(page)
            logs.log_pim_success()

            select_first_employee(page)
            logs.log_employee_selected()

            navigate_to_leave(page)
            logs.log_leave_nav_success()

            apply_for_leave(page)
            logs.log_leave_submit_success()

        except Exception as e:
            logs.logger.error(f"An error occurred: {e}")
            raise

        finally:
            browser.close()
            logs.log_browser_closed()

if __name__ == "__main__":
    main()