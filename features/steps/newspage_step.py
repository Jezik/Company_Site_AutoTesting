from behave import given, when, then
from features.pages.news_page import NewsPage
from features.pages.locators.news_page_locators import NewsLocators

from features.pages.json_parser import JSONParser

@given("User opens the page https://sperasoft.com/news/")
def step_impl(context):
    NewsPage(context).open_url()


@then("The displayed url is correct")
def step_impl(context):
    assert NewsPage(context).get_current_url() == JSONParser().get_test_page_url("news")


@then("User can see the header for the latest article")
def step_impl(context):
    assert NewsPage(context).is_element_exists(NewsLocators.TOP_ARTICLE_HEADER) == True


@when("User scrolls down to the second article")
def step_impl(context):
    NewsPage(context).scroll_to_element(NewsLocators.SECOND_ARTICLE_HEADER)


@then("User can see the header for the second article")
def step_impl(context):
    assert NewsPage(context).is_element_exists(NewsLocators.SECOND_ARTICLE_HEADER) == True


@when("User scrolls down to the third article")
def step_impl(context):
    NewsPage(context).scroll_to_element(NewsLocators.THIRD_ARTICLE_HEADER)


@then("User can see the header for the third article")
def step_impl(context):
    assert NewsPage(context).is_element_exists(NewsLocators.THIRD_ARTICLE_HEADER) == True


@when("User clicks on the the header of the third article")
def step_impl(context):
    NewsPage(context).click_on_element(NewsLocators.THIRD_ARTICLE_LINK)


@then("The full artcile is shown on a new page")
def step_impl(context):
    assert NewsPage(context).get_current_url() == JSONParser().get_test_page_url("article2")
