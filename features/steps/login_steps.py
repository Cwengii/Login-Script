from behave import given, when, then
import time

@given('the login page is open')
def step_open_login_page(context):
    context.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)


@when('I enter username "{username}"')
def step_enter_username(context, username):
    username_field = context.page.locator("input[name=username]")
    username_field.wait_for()
    username_field.fill(username)
    time.sleep(0.5)


@when('I enter password "{password}"')
def step_enter_password(context, password):
    password_field = context.page.locator("input[name=password]")
    password_field.wait_for()
    password_field.fill(password)
    time.sleep(0.5)


@when('I click the login button')
def step_click_login_button(context):
    login_button = context.page.locator("button[type=submit]")
    login_button.wait_for()
    login_button.click()
    time.sleep(2)

@then('I should see the dashboard')
def step_see_dashboard(context):
    context.page.wait_for_selector(".oxd-layout", timeout=10000)
    page_text = context.page.content()
    assert "dashboard" in page_text.lower() or "home" in page_text.lower()