from playwright.sync_api import expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(title).to_be_visible()

    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    empty_list_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_list_title).to_be_visible()

    empty_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_description).to_be_visible()