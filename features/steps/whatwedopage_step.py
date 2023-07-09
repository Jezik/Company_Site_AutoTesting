from behave import given, when, then
from features.pages.whatwedo_page import WhatWeDo
from features.pages.locators.whatwedo_page_locators import WhatWeDoLocators

from features.pages.json_parser import JSONParser


@given("User opens the page https://sperasoft.com/whatwedo/")
def step_impl(context):
    WhatWeDo(context).open_url()


@then("The company logo is shown")
def step_impl(context):
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.COMPANY_LOGO) == True


@then("The header is shown with a correct text")
def step_impl(context):
    assert  WhatWeDo(context).get_elem_text(WhatWeDoLocators.TOP_HEADER).lower() == JSONParser().get_required_text("top_whatwedo").lower()
    assert WhatWeDo(context).get_elem_text(WhatWeDoLocators.SUB_TOP_HEADER).lower() == JSONParser().get_required_text("sub_top_whatwedo").lower()
    

@when("User scrolls down to a 'Game Development' section")
def step_impl(context):
    WhatWeDo(context).scroll_to_element(WhatWeDoLocators.GAME_DEV_SECTION)


@then("The right text description is shown in 'Game Development' section")
def step_impl(context):
    assert WhatWeDo(context).get_elem_text(WhatWeDoLocators.GAME_DEV_DESCRIPTION_FIRST).lower() == JSONParser().get_required_text("gamedev_first").lower()
    print(WhatWeDo(context).get_elem_text(WhatWeDoLocators.GAME_DEV_DESCRIPTION_SECOND).lower())
    print(JSONParser().get_required_text("gamedev_second").lower())
    assert WhatWeDo(context).get_elem_text(WhatWeDoLocators.GAME_DEV_DESCRIPTION_SECOND).lower() == JSONParser().get_required_text("gamedev_second").lower()


@when("User scrolls down to a 'Game porting' section")
def step_impl(context):
    WhatWeDo(context).scroll_to_element(WhatWeDoLocators.GAME_PORTING_SECTION)


@then("The right text description is shown in 'Game porting' section")
def step_impl(context):
    assert WhatWeDo(context).get_elem_text(WhatWeDoLocators.GAME_PORTING_DESCRIPTION).lower() == JSONParser().get_required_text("gameporting").lower()


@when("User scrolls down to a 'Engineering' section")
def step_impl(context):
    WhatWeDo(context).scroll_to_element(WhatWeDoLocators.ENGINEERING_SECTION)


@then("The right text description is shown in 'Engineering' section")
def step_impl(context):
    assert WhatWeDo(context).get_elem_text(WhatWeDoLocators.ENGINEERING_DESCRIPTION).lower() == JSONParser().get_required_text("engineering").lower()


@when("User scrolls down to a 'Creative' section")
def step_impl(context):
    WhatWeDo(context).scroll_to_element(WhatWeDoLocators.CREATIVE_SECTION)


@then("The right text description is shown in 'Creative' section")
def step_impl(context):
    assert WhatWeDo(context).get_elem_text(WhatWeDoLocators.CREATIVE_DESCRIPTION).lower() == JSONParser().get_required_text("creative").lower()


@when("User clicks on 'View all Games' button")
def step_impl(context):
    WhatWeDo(context).click_on_element(WhatWeDoLocators.ALL_GAMES_BUTTON)


@then("The page https://sperasoft.com/games/ is opened")
def step_impl(context):
    assert WhatWeDo(context).get_current_url() == JSONParser().get_test_page_url("games")


@when('User return back to whatwedo page')
def step_impl(context):
    WhatWeDo(context).press_back_button()


@when("User clicks on 'Portfolio' button")
def step_impl(context):
    WhatWeDo(context).click_on_element(WhatWeDoLocators.PORTFOLIO_BUTTON)


@then("The https://sperasoft.com/whatwedo/portfolio/ page is opened")
def step_impl(context):
    assert WhatWeDo(context).get_current_url() == JSONParser().get_test_page_url("portfolio")


@when("User clicks on 'Request more info' button")
def step_impl(context):
    WhatWeDo(context).click_on_element(WhatWeDoLocators.REQUEST_INFO_BUTTON)


@then("The the pop-up with the request form is shown")
def step_impl(context):
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.POP_UP_HEADER) == True


@when("User scrolls down to 'Company certifications' section")
def step_impl(context):
    WhatWeDo(context).scroll_to_element(WhatWeDoLocators.COMPANY_CERTIFICATIONS_SECTION)


@then("The correct list of certifications is shown")
def step_impl(context):
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.PS5_CERT) == True
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.STADIA_CERT) == True
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.XBOX_X_CERT) == True
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.NINTENDO_CERT) == True
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.PS4_CERT) == True
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.XBOX_CERT) == True
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.ANDROID_CERT) == True
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.IOS_CERT) == True
    assert WhatWeDo(context).is_element_exists(WhatWeDoLocators.PS3_CERT) == True
    