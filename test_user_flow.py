from playwright.sync_api import sync_playwright

def test_ai_analysis_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://dummy-ai-ui.onrender.com')
        page.fill('#text-input', 'Great product')
        page.click('#analyze-btn')
        page.wait_for_selector('#result')
        assert page.inner_text('#result')
        browser.close()
