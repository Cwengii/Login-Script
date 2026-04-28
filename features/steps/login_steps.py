from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


@given('the login page is open')
def step_open_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(2)


@when('I enter username "{username}"')
def step_enter_username(context, username):
    username_field = context.wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.clear()
    username_field.send_keys(username)
    time.sleep(0.5)


@when('I enter password "{password}"')
def step_enter_password(context, password):
    password_field = context.wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.clear()
    password_field.send_keys(password)
    time.sleep(0.5)


@when('I click the login button')
def step_click_login_button(context):
    login_button = context.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()
    time.sleep(2)


@when('I leave username empty')
def step_leave_username_empty(context):
    username_field = context.wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.clear()
    time.sleep(0.5)


@when('I leave password empty')
def step_leave_password_empty(context):
    password_field = context.wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.clear()
    time.sleep(0.5)


@then('I should see the dashboard')
def step_see_dashboard(context):
    context.wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-layout']"))
    )
    page_text = context.driver.page_source
    assert "dashboard" in page_text.lower() or "home" in page_text.lower()


@then('I should see "{text}"')
def step_see_text(context, text):
    context.wait.until(
        lambda driver: text in driver.page_source or text.lower() in driver.page_source.lower()
    )


@then('I should see an error message')
def step_see_error_message(context):
    error_element = context.wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'invalid') or contains(text(), 'error') or contains(text(), 'Invalid')]"))
    )
    assert error_element.is_displayed()


@then('the error message should contain "{expected_text}"')
def step_error_message_contains(context, expected_text):
    page_text = context.driver.page_source
    assert expected_text in page_text or expected_text.lower() in page_text.lower()


@then('I should see a validation error')
def step_see_validation_error(context):
    error_present = context.wait.until(
        lambda driver: len(driver.find_elements(By.XPATH, "//*[contains(text(), 'required') or contains(text(), 'Invalid')]")) > 0
    )
    assert error_present
    assert error_present

@then('I should see a validation error')
def step_see_validation_error(context):
    validation_error = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "validation-error"))
    )
    assert validation_error.is_displayed()
    context.validation_message = validation_error.text
