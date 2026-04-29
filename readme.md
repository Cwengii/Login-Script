# Login Automation Project

The automation covers:
1. Opening a browser  
2. Navigating to the OrangeHRM login page  
3. Entering a username and password  
4. Clicking the login button  
5. Checking whether the login succeeded or failed  
6. Apply for leave  

## Project Layout

```
Login-Script/
├── main.py                    # Runs the automation
├── login.py                   # Login functions (browser setup, login)
├── pim.py                     # Employee management functions
├── leave.py                   # Leave application functions
├── features/                  # Behave test files
│   ├── login.feature          #  Test scenarios
│   ├── steps/
│   │   └── login_steps.py     # Behave steps
│   └── environment.py         # Browser setup for Behave
├── requirements.txt           # Required Python packages
├── setup.bat                  # Setup script
└── README.md                  # This file
```

## Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: How to Run

#### Runs the full automation: login → PIM → leave application.  
```bash
python main.py
```

#### Runs the English-style test scenarios  
```bash
python -m behave
```

### Modular Scripts (main.py, login.py, etc.)

- **What it is:** Python code split into small, reusable functions.  

**Example:**
```python
# In main.py
from login import perform_login
from pim import navigate_to_pim

def main():
    # Setup browser
    # perform_login(page)
    # navigate_to_pim(page)
    # ... 
```

### Behave folder

- **What it is:** Tests written in plain English, connected to Python code.  

**Example:**
```gherkin
Scenario: Successful login
  When I enter username "admin"
  And I enter password "admin123"
  Then I should see the dashboard
```

```python
@when('I enter username "{username}"')
def step_enter_username(context, username):
    # Python code to type in username field
```

## Common Commands

### Modular Scripts
```bash
python main.py
```

### Behave Tests
```bash
python -m behave
python -m behave -v
python -m behave features/login.feature
```

## Troubleshooting

- **"Module not found" errors:**  
  ```bash
  pip install -r requirements.txt
  ```