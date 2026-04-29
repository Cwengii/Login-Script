from playwright.sync_api import sync_playwright

def before_scenario(context, scenario):
    print(f"\nRunning: {scenario.name}")
    
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    if hasattr(context, 'browser') and context.browser:
        context.browser.close()
    if hasattr(context, 'playwright') and context.playwright:
        context.playwright.stop()
