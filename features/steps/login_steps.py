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


@when('I leave username empty')
def step_leave_username_empty(context):
    username_field = context.page.locator("input[name=username]")
    username_field.wait_for()
    username_field.fill("")
    time.sleep(0.5)


@when('I leave password empty')
def step_leave_password_empty(context):
    password_field = context.page.locator("input[name=password]")
    password_field.wait_for()
    password_field.fill("")
    time.sleep(0.5)


@then('I should see the dashboard')
def step_see_dashboard(context):
    context.page.wait_for_selector(".oxd-layout", timeout=10000)
    page_text = context.page.content()
    assert "dashboard" in page_text.lower() or "home" in page_text.lower()


@then('I should see "{text}"')
def step_see_text(context, text):
    context.page.wait_for_load_state("networkidle")
    page_text = context.page.content()
    assert text in page_text or text.lower() in page_text.lower()


@then('I should see an error message')
def step_see_error_message(context):
    error_locator = context.page.locator("text=/invalid|error|Invalid/")
    error_locator.wait_for(timeout=5000)
    assert error_locator.is_visible()


@then('the error message should contain "{expected_text}"')
def step_error_message_contains(context, expected_text):
    page_text = context.page.content()
    assert expected_text in page_text or expected_text.lower() in page_text.lower()


@then('I should see a validation error')
def step_see_validation_error(context):
    validation_locator = context.page.locator("text=/required|Invalid/")
    validation_locator.wait_for(timeout=5000)
    assert validation_locator.is_visible()
