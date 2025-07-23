from playwright.sync_api import Page, expect
from typing import Pattern
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f"Opening URL: {url}"):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f"Reloading page with URL: {self.page.url}"):
            self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f"Checking current URL matches pattern: {expected_url.pattern}"):
            expect(self.page).to_have_url(expected_url)