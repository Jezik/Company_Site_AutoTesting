from behave import given, when, then
from features.pages.about_page import AboutPage
from features.pages.locators.about_page_locators import AboutPageLocators

from features.pages.json_parser import JSONParser


@given("User opens the page https://sperasoft.com/about/")
def step_impl(context):
    AboutPage(context).open_url()


@then("The displayed url of 'About' page is correct")
def step_impl(context):
    assert AboutPage(context).get_current_url() == JSONParser().get_test_page_url("about")


@when("User scrolls down to a 'World Class Gaming Studio' section")
def step_impl(context):
    AboutPage(context).scroll_to_element(AboutPageLocators.WORLD_CLASS_SECTION)


@then("The right text description is shown in 'World Class Gaming Studio' section")
def step_impl(context):
    assert AboutPage(context).get_elem_text(AboutPageLocators.WORLD_CLASS_DESCRIPTION).lower() == JSONParser().get_required_text("world-class").lower()


@when("User scrolls down to a 'Our clients' section")
def step_impl(context):
    AboutPage(context).scroll_to_element(AboutPageLocators.CLIENTS_SECTION)


@then("User can see the list of main partners")
def step_impl(context):
    assert AboutPage(context).get_list_length(AboutPageLocators.CLIENTS_LIST) == 15


@when("User clicks on 'View all' button")
def step_impl(context):
    AboutPage(context).click_on_element(AboutPageLocators.VIEW_ALL_BUTTON)


@then("User can see the whole list of partners")
def step_impl(context):
    assert AboutPage(context).get_list_length(AboutPageLocators.CLIENTS_LIST) == 54


@when("User scrolls down to a 'Leadership team' section")
def step_impl(context):
    AboutPage(context).scroll_to_element(AboutPageLocators.READ_MORE_BUTTON)


@then("User can see the list of all company's top managers")
def step_impl(context):
    assert AboutPage(context).get_list_length(AboutPageLocators.LEADERSHIP_TEAM_LIST) == 6


@when("User clicks on 'Read more' button")
def step_impl(context):
    AboutPage(context).click_on_element(AboutPageLocators.READ_MORE_BUTTON)


@then("The page https://sperasoft.com/about/executives/ is opened")
def step_impl(context):
    assert AboutPage(context).get_current_url() == JSONParser().get_test_page_url("ceo")


@then("The correct header for this page is shown")
def step_impl(context):
    import time
    time.sleep(3)
    assert AboutPage(context).get_elem_text(AboutPageLocators.EXECUTIVES_HEADER).lower() == JSONParser().get_required_text("executives").lower()
