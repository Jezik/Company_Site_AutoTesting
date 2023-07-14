from behave import given, when, then
from features.pages.careers_page import CareersPage
from features.pages.locators.career_page_locators import CareerLocators

from features.pages.json_parser import JSONParser

	
@given("User opens the page https://sperasoft.com/career/")
def step_impl(context):
    CareersPage(context).open_url()


@then("The displayed url of this page is correct")
def step_impl(context):
    assert CareersPage(context).get_current_url() == JSONParser().get_test_page_url("careers")


@then("The big header 'Join #Sperasoft' is shown")
def step_impl(context):
    assert CareersPage(context).get_elem_text(CareerLocators.BIG_HEADER_PART1).lower() == JSONParser().get_required_text("jobs_1").lower()
    assert CareersPage(context).get_elem_text(CareerLocators.BIG_HEADER_PART2).lower() == JSONParser().get_required_text("jobs_2").lower()


@then("The section 'Jobs at Sperasoft' is shown")
def step_impl(context):
    assert CareersPage(context).is_element_exists(CareerLocators.JOBS_SPERASOFT_SECTION) == True


@when("User clicks on a 'About us' link")
def step_impl(context):
    CareersPage(context).click_on_element(CareerLocators.ABOUT_US_LINK)


@then("The page https://sperasoft.com/about/ is shown")
def step_impl(context):
    assert CareersPage(context).get_current_url() == JSONParser().get_test_page_url("about")


@when("User clicks on 'Sperasoft bootcamp' link")
def step_impl(context):
    CareersPage(context).click_on_element(CareerLocators.BOOTCAMP_LINK)


@then("The page https://sperasoft.com/career/bootcamp/ is opened")
def step_impl(context):
    assert CareersPage(context).get_current_url() == JSONParser().get_test_page_url("bootcamps")


@when("User clicks on 'Sperasoft news' link")
def step_impl(context):
    CareersPage(context).click_on_element(CareerLocators.NEWS_LINK)


@then("The page https://sperasoft.com/news/ is opened")
def step_impl(context):
    assert CareersPage(context).get_current_url() == JSONParser().get_test_page_url("news")


@when("User picks from drop down list city Warsaw")
def step_impl(context):
    CareersPage(context).select_dropdown_item_by_text(CareerLocators.SELECT_CITY_DROPDOWN, "Warsaw")


@when("User clicks on job header")
def step_impl(context):
    CareersPage(context).click_on_element(CareerLocators.FIRST_ENGINEERING_JOB_LINK)


@then("The job description openes in on a new page")
def step_impl(context):
    assert CareersPage(context).get_current_url() == JSONParser().get_test_page_url("job")
