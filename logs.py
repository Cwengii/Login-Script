import logging

logging.basicConfig(filename='login_script.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("User has logged in")
logging.error("User cannot log in")

logging.info("dashboard pops up")
logging.error("dashboard does not pop up")

logging.info("navigates to the PIM section")
logging.error("PIM section does not pop up")

logging.info("first employee selected")
logging.error("could not select first employee")

logging.info("navigated to leave section")
logging.error("could not navigate to leave section")

logging.info("leave type selected and dates filled")
logging.error("could not fill leave form")

logging.info("leave form submitted")
logging.error("leave form submission failed")

logging.info("browser launched and script started")
logging.error("script failed to run")

logging.info("browser closed successfully")