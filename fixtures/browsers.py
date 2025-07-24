import pytest
import allure
from playwright.sync_api import Page, Playwright
from pages.authentication.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest

from tools.playwright.pages import initialize_playwright_page


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name= request.node.name)

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir= './videos/')
    page = context.new_page()

    registration_page = RegistrationPage(page= page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email= 'user.name@gmail.com', username= 'username', password= 'password')
    registration_page.click_registration_button()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    context.storage_state(path='browser-state.json')
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright, request: SubRequest) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, storage_state='browser-state.json')

