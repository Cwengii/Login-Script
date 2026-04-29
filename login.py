from playwright.sync_api import sync_playwright
import time

def perform_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("input[name=username]", "admin")
    page.fill("input[name=password]", "admin123")
    page.click("button[type=submit]")
    page.wait_for_selector(".oxd-layout", timeout=15000)