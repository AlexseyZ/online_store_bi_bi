import pytest
from playwright.sync_api import sync_playwright



@pytest.fixture()
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)  # True - Экран выключен False - Экран включен
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()
        yield page
        context.close()
        page.close()
        browser.close()
