from behave import given, when, then
from features.pages.main_page import MainPage
from features.pages.locators.main_page_locators import MainPageLocators

from features.pages.json_parser import JSONParser


@given("User openes main site page")
def step_impl(context):
    main_page = MainPage(context)
    main_page.open_url()


@then("The url should be valid")
def step_impl(context):
    assert MainPage(context).get_current_url() == JSONParser().get_test_page_url("main")


@then("The company logo is shown")
def step_impl(context):
    main_page = MainPage(context)
    assert main_page.is_element_exists(MainPageLocators.COMPANY_LOGO) == True
    assert main_page.is_image_loaded(MainPageLocators.COMPANY_LOGO) == True


@when("User scrolls down to Job opportunity section")
def step_impl(context):
    MainPage(context).scroll_to_element(MainPageLocators.LEARN_ABOUT_COMPANY_BUTTON)


@then("Links to social media appear on the right side")
def step_impl(context):
    assert MainPage(context).is_element_exists(MainPageLocators.FACEBOOK_LINK) == True
    assert MainPage(context).is_element_exists(MainPageLocators.TWITTER_LINK) == True
    assert MainPage(context).is_element_exists(MainPageLocators.INSTAGRAM_LINK) == True
    assert MainPage(context).is_element_exists(MainPageLocators.LINKEDIN_LINK) == True


@when("User clicks on Facebook icon")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.FACEBOOK_LINK)


@then("Facebook company page opens in a new tab")
def step_impl(context):
    main_page = MainPage(context)
    main_page.switch_to_first_tab()
    assert main_page.get_current_url() == JSONParser().get_social_media_link("facebook")


@when("User closes the tab")
def step_impl(context):
    MainPage(context).close_current_tab()


@when("User clicks on Twitter icon")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.TWITTER_LINK)


@then("Twitter company page opens in a new tab")
def step_impl(context):
    main_page = MainPage(context)
    main_page.switch_to_first_tab()
    assert main_page.get_current_url() == JSONParser().get_social_media_link("twitter")


@when("User clicks on Instagram icon")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.INSTAGRAM_LINK)


@then("Instagram company page opens in a new tab")
def step_impl(context):
    main_page = MainPage(context)
    main_page.switch_to_first_tab()
    assert main_page.get_current_url() == JSONParser().get_social_media_link("instagram")


@when("User clicks on LinkedIn icon")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.LINKEDIN_LINK)


@then("LinkedIn company page opens in a new tab")
def step_impl(context):
    main_page = MainPage(context)
    main_page.switch_to_first_tab()
    assert main_page.get_current_url() == JSONParser().get_social_media_link("linkedin")


@when("User clicks on 'What we do' link")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.WHAT_WE_DO_LINK)


@then("The page 'Whatwedo' is opened")
def step_impl(context):
    assert MainPage(context).get_current_url() == JSONParser().get_test_page_url("whatwedo")


@when("User clicks on 'Solutions' link")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.SOLUTIONS_LINK)


@then("The page 'Solutions' is opened")
def step_impl(context):
    assert MainPage(context).get_current_url() == JSONParser().get_test_page_url("solutions")


@when("User clicks on 'Games' link")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.GAMES_LINK)


@then("The page 'Games' is opened")
def step_impl(context):
    assert MainPage(context).get_current_url() == JSONParser().get_test_page_url("games")


@when("User clicks on 'About' link")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.ABOUT_LINK)


@then("The page 'About' is opened")
def step_impl(context):
    assert MainPage(context).get_current_url() == JSONParser().get_test_page_url("about")


@when("User clicks on 'News' link")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.NEWS_LINK)


@then("The page 'News' is opened")
def step_impl(context):
    assert MainPage(context).get_current_url() == JSONParser().get_test_page_url("news")


@when("User clicks on 'Careers' link")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.CAREERS_LINK)


@then("The page 'Career' is opened")
def step_impl(context):
    assert MainPage(context).get_current_url() == JSONParser().get_test_page_url("careers")


@when("User clicks on 'Explore' button")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.EXPLORE_BUTTON)


@when("User presses back button in a browser")
def step_impl(context):
    MainPage(context).press_back_button()


@when("User clicks on 'Learn about the company' button")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.LEARN_ABOUT_COMPANY_BUTTON)


@when("User clicks on 'View all open vacancies' button")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.VACANCIES_BUTTON)


@when("Scrolls down to Bootcamps section")
def step_impl(context):
    MainPage(context).scroll_to_element(MainPageLocators.READ_MORE_BUTTON)


@when("Clicks on 'Read more' button")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.READ_MORE_BUTTON)


@then("The page 'Bootcamp' is opened")
def step_impl(context):
    assert MainPage(context).get_current_url() == JSONParser().get_test_page_url("bootcamps")


@when("User scrolls down to a news section")
def step_impl(context):
    MainPage(context).scroll_to_element(MainPageLocators.LAST_NEWS_SECTION)


@then("User can see four last news")
def step_impl(context):
    assert MainPage(context).get_list_length(MainPageLocators.LAST_NEWS_LIST) == 4


@when("User clicks on a specific article")
def step_impl(context):
    MainPage(context).click_on_element(MainPageLocators.ARTICLE_FOR_TEST_LINK)


@then("The new page with right content is opened")
def step_impl(context):
    assert MainPage(context).get_current_url() == JSONParser().get_test_page_url("article")


@when("User scrolls down to a 'Our partners' section")
def step_impl(context):
    MainPage(context).scroll_to_element(MainPageLocators.PARTNERS_SECTION)


@then("User can see appropriate list of partners")
def step_impl(context):
    assert MainPage(context).get_list_length(MainPageLocators.PARTNERS_LIST) == 14
    #TODO: assert real images
