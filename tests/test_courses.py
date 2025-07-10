from playwright.sync_api import expect
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage
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

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form('','','','0','0')
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.jpg')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form('Playwright', '2 weeks', 'Playwright', '100', '10')
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_courses_card('Playwright', '100', '10', '2 weeks', 0)

