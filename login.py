import time_conts as t

# Navigates to the login portal then fills in the deatils 
def perform_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("input[name=username]", "Admin")
    page.fill("input[name=password]", "admin123")
    page.click("button[type=submit]")
    page.wait_for_url("**/dashboard**",timeout=  t.request_timeout)