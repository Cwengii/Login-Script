import logging

# Set up a logger that writes to both a file and the terminal (console)
logger = logging.getLogger("hrm_automation")
logger.setLevel(logging.DEBUG)

# File handler - saves logs to a file
file_handler = logging.FileHandler("login_script.log")
file_handler.setLevel(logging.DEBUG)

# Console handler - prints logs to the terminal when you run main.py
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Format used by both handlers
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Attach both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# --- Login ---
def log_login_success():
    logger.info("User has logged in successfully")

def log_login_failure():
    logger.error("User cannot log in")


# --- Dashboard ---
def log_dashboard_success():
    logger.info("Dashboard loaded successfully")

def log_dashboard_failure():
    logger.error("Dashboard did not load")


# --- PIM ---
def log_pim_success():
    logger.info("Navigated to the PIM section")

def log_pim_failure():
    logger.error("PIM section did not load")


# --- Employee selection ---
def log_employee_selected():
    logger.info("First employee selected")

def log_employee_failure():
    logger.error("Could not select first employee")


# --- Leave navigation ---
def log_leave_nav_success():
    logger.info("Navigated to leave section")

def log_leave_nav_failure():
    logger.error("Could not navigate to leave section")


# --- Leave form ---
def log_leave_form_success():
    logger.info("Leave type selected and dates filled")

def log_leave_form_failure():
    logger.error("Could not fill leave form")


# --- Leave submission ---
def log_leave_submit_success():
    logger.info("Leave form submitted successfully")

def log_leave_submit_failure():
    logger.error("Leave form submission failed")


# --- Script lifecycle ---
def log_script_started():
    logger.info("Browser launched and script started")

def log_script_failed():
    logger.error("Script failed to run")

def log_browser_closed():
    logger.info("Browser closed successfully")