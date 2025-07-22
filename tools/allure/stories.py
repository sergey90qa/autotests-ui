from enum import Enum


class AllureStory(str, Enum):
    COURSES = 'Courses'
    DASHBOARD = 'Dasboard'
    REGISTRATION = 'Registration'
    AUTHORIZATION = 'Authorization'