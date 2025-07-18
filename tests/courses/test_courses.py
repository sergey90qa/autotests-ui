import pytest
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, chromium_page_with_state, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')

        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(title='', estimated_time='', description='', max_score='0',
                                                            min_score='0')
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.jpg')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(title='Playwright',
                                                   estimated_time='2 weeks',
                                                   description='Playwright',
                                                   max_score='100',
                                                   min_score='10')
        create_course_page.create_course_toolbar_view.click_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(0, 'Playwright', '100', '10', '2 weeks')

    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.jpg')
        create_course_page.create_course_form.fill(title='Python',
                                                   estimated_time='3 weeks',
                                                   description='Python',
                                                   max_score='100',
                                                   min_score='10')
        create_course_page.create_course_toolbar_view.click_button()
        courses_list_page.course_view.check_visible(index=0,
                                                    title='Python',
                                                    estimated_time='3 weeks',
                                                    max_score='100',
                                                    min_score='10')
        courses_list_page.course_view.menu.click_edit(index= 0)
        create_course_page.create_course_form.fill(title='Js',
                                                   estimated_time='4 weeks',
                                                   description='Js',
                                                   max_score='1000',
                                                   min_score='100')
        create_course_page.create_course_toolbar_view.click_button()
        courses_list_page.course_view.check_visible(index=0,
                                                    title='Js',
                                                    estimated_time='4 weeks',
                                                    max_score='1000',
                                                    min_score='100')

