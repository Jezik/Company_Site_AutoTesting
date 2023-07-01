from behave import given, when, then
from features.pages.main_page import MainPage
from features.pages.locators.main_page_locators import MainPageLocators


@given("User openes main site page")
def step_impl(context):
    main_page = MainPage(context)
    main_page.open_url()

@then("The url should be valid")
def step_impl(context):
    assert MainPage(context).get_current_url() == "https://sperasoft.com/"

@then("The company logo should be displayed correctly")
def step_impl(context):
    assert MainPage(context).is_element_exists(MainPageLocators.COMPANY_LOGO)
