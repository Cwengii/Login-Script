## The Files

1. **login.feature** - Tests written in English
2. **login_steps.py** - Python code that does the actual testing  
3. **environment.py** - Sets up the browser before each test

## How to Use

1. Install packages:
```bash
pip install -r requirements.txt
```

2. Run tests:
```bash
behave
```

That's it! It opens Chrome and tests the login page.

## Common Commands

```bash
behave                    # Run all tests
behave -v                 # Show more details
behave features/login.feature   # Run just login tests
```

## How It Works

1. Feature file says what to test (in English)
2. login_steps.py has Python code for each step
3. environment.py opens/closes the browser
4. Tests run automatically

## Project Structure

```
features/
├── login.feature              # Test scenarios in English
├── steps/
│   └── login_steps.py        # Python implementation of steps
└── environment.py            # Setup/teardown configuration

requirements.txt              # Python packages to install
README.md            # This file!
```

### Feature File (login.feature)

```gherkin
Feature: User Login
  Background:
    Given the login page is open
    
  Scenario: Successful login with valid credentials
    When I enter username "testuser"
    And I enter password "password123"
    And I click the login button
    Then I should see the dashboard
```

**Reading this:**
1. **Feature**: Describes what we're testing (User Login)
2. **Background**: Steps that run before every scenario
3. **Scenario**: A specific test case
4. **When/And/Then**: Individual steps

### Step Definition File (login_steps.py)

Each line in the feature file is matched to a Python function:

```python
@when('I enter username "{username}"')
def step_enter_username(context, username):
    # Find the username field and type the value
    username_field = context.wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys(username)
```

**The `@when` decorator** matches the step in the feature file.
The function name doesn't matter - only the text in quotes matters!

## How Tests Work

1. **Browser Setup** (environment.py: `before_scenario`)
   - Opens Chrome browser
   - Maximizes window
   - Sets up waits

2. **Run Scenario Steps**
   - Execute `Given` steps (setup)
   - Execute `When` steps (actions)
   - Execute `Then` steps (assertions)
   - Print progress with ✓ or ✗

3. **Browser Cleanup** (environment.py: `after_scenario`)
   - Closes browser
   - Saves screenshots on failure
   - Prints results

## Debugging

### Common Issues:

**Error: "webdriver not found"**
```bash
pip install webdriver-manager
```

**Error: "NoSuchElementException"**
- The element selector is wrong
- The page hasn't loaded yet
- The element ID/NAME changed

**To Debug:**
1. Run with verbose mode: `behave -v`
2. Add print statements in your step definitions
3. Take screenshots on failure (automatically done)
4. Check the element IDs in the browser (F12)
