from behave import given, when, then
from features.pages.solutions_page import SolutionsPage
from features.pages.locators.solutions_page_locators import SolutionsLocators

from features.pages.json_parser import JSONParser


@given("User opens the page https://sperasoft.com/solutions/")
def step_impl(context):
    SolutionsPage(context).open_url()


@then("Both headers have correct text")
def step_impl(context):
    assert SolutionsPage(context).get_elem_text(SolutionsLocators.SOLUTIONS_HEADER_MAIN).lower() == JSONParser().get_required_text("solutions_head").lower()
    assert SolutionsPage(context).get_elem_text(SolutionsLocators.SOLUTIONS_HEADER_SECOND).lower() == JSONParser().get_required_text("solutions_subh").lower()


@when("User scrolls down to a 'Live services' section")
def step_impl(context):
    SolutionsPage(context).scroll_to_element(SolutionsLocators.LIVE_SERVICES_SECTION)


@then("The right text description is shown in 'Live services' section")
def step_impl(context):
    assert SolutionsPage(context).get_elem_text(SolutionsLocators.LIVE_SERVICES_DESCRIPTION).lower() == JSONParser().get_required_text("live_ser").lower()


@when("User scrolls down to a 'NOC' section")
def step_impl(context):
    SolutionsPage(context).scroll_to_element(SolutionsLocators.NOC_SECTION)


@then("The right text description is shown in 'NOC' section")
def step_impl(context):
    assert SolutionsPage(context).get_elem_text(SolutionsLocators.NOC_DESCRIPTION).lower() == JSONParser().get_required_text("noc").lower()


@when("User scrolls down to a 'eCommerce' section")
def step_impl(context):
    SolutionsPage(context).scroll_to_element(SolutionsLocators.E_COMMERCE_SECTION)


@then("The right text description is shown in 'eCommerce' section")
def step_impl(context):
    assert SolutionsPage(context).get_elem_text(SolutionsLocators.E_COMMERCE_DESCRIPTION).lower() == JSONParser().get_required_text("e_commerce").lower()


@when("User srolls down to a 'DevOps' section")
def step_impl(context):
    SolutionsPage(context).scroll_to_element(SolutionsLocators.DEVOPS_SECTION)


@then("The right text description is shown in 'DevOps' section")
def step_impl(context):
    assert SolutionsPage(context).get_elem_text(SolutionsLocators.DEVOPS_DESCRIPTION_FIRST).lower() == JSONParser().get_required_text("dev_ops_first").lower()
    assert SolutionsPage(context).get_elem_text(SolutionsLocators.DEVOPS_DESCRIPTION_SECOND).lower() == JSONParser().get_required_text("dev_ops_second").lower()


@when("User srolls down to a 'QE' section")
def step_impl(context):
    SolutionsPage(context).scroll_to_element(SolutionsLocators.QE_SECTION)


@then("The right text description is shown in 'QE' section")
def step_impl(context):
    assert SolutionsPage(context).get_elem_text(SolutionsLocators.QE_DESCRIPTION_FIRST).lower() == JSONParser().get_required_text("qe_first").lower()
    assert SolutionsPage(context).get_elem_text(SolutionsLocators.QE_DESCRIPTION_SECOND).lower() == JSONParser().get_required_text("qe_second").lower()


@when("User clicks on 'Contact us' field")
def step_impl(context):
    SolutionsPage(context).click_on_element(SolutionsLocators.CONTACT_US_BUTTON)


@then("The form for requests should be shown")
def step_impl(context):
    assert SolutionsPage(context).is_element_exists(SolutionsLocators.CONTACT_US_SEND_BUTTON) == True
    