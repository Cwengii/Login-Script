from playwright.sync_api import sync_playwright
import time

def test_login():
    username = "Acwengile"
    password = "Cw3567"
    login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(login_url)

        page.fill("input[name=username]", username)
        page.fill("input[name=password]", password)

        print("Login succeeded")
        time.sleep(10)   

        browser.close()


if __name__ == "__main__":
    test_login()
