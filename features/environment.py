from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

try:
    from webdriver_manager.chrome import ChromeDriverManager
    HAS_WEBDRIVER_MANAGER = True
except ImportError:
    HAS_WEBDRIVER_MANAGER = False


def before_scenario(context, scenario):
    print(f"\nRunning: {scenario.name}")
    
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--no-sandbox')
    
    if HAS_WEBDRIVER_MANAGER:
        context.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    else:
        context.driver = webdriver.Chrome(options=options)
    
    context.driver.implicitly_wait(10)
    context.wait = WebDriverWait(context.driver, 10)

def after_scenario(context, scenario):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
