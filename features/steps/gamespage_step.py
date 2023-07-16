from behave import given, when, then
from features.pages.games_page import GamesPage
from features.pages.locators.games_page_locators import *

from features.pages.json_parser import JSONParser

@given("User opens the page https://sperasoft.com/games/")
def step_impl(context):
    GamesPage(context).open_url()


@then("The displayed url of games page is correct")
def step_impl(context):
    assert GamesPage(context).get_current_url() == JSONParser().get_test_page_url("games")


@then("User can see the correct list of top games")
def step_impl(context):
    games_page = GamesPage(context)
    list_games = games_page.get_elem_list(GamesPageLocators.TOP_GAMES_LIST)
    assert games_page.get_list_length(GamesPageLocators.TOP_GAMES_LIST) == 8

    for i in range(0, len(list_games)):
        game_name = list_games[i].find_element(By.XPATH, f"//*[@id='theme-page']/div[3]/div[2]/div[1]/div[2]/div/ul/li[{i+1}]/div[2]/div[1]")       
        game_studio = list_games[i].find_element(By.XPATH, f"//*[@id='theme-page']/div[3]/div[2]/div[1]/div[2]/div/ul/li[{i+1}]/div[2]/div[2]")
        test_name, test_studio = JSONParser().get_top_game_name_studio(i)     
        assert game_name.text.lower() == test_name.lower()
        assert game_studio.text.lower() == test_studio.lower()


@when("User scrolls down to 'Creative' section")
def step_impl(context):
    GamesPage(context).scroll_to_element(GamesPageLocators.CREATIVE_SECTION)


@then("User can see the correct list of games in 'Creative' section")
def step_impl(context):
    games_page = GamesPage(context)
    list_games = games_page.get_elem_list(GamesPageLocators.CREATIVE_GAMES_LIST)
    assert games_page.get_list_length(GamesPageLocators.CREATIVE_GAMES_LIST) == 8

    for i in range(0, len(list_games)):
        selector = f"//*[@id='theme-page']/div[5]/div[2]/div[1]/div/div/ul/li[{i+1}]/img"
        assert games_page.is_image_loaded((By.XPATH, selector)) == True


@when("User scrolls down to 'Sports' section")
def step_impl(context):
    GamesPage(context).scroll_to_element(GamesPageLocators.SPORTS_SECTION)


@then("User can see the correct list of games in 'Sports' section")
def step_impl(context):
    games_page = GamesPage(context)
    list_games = games_page.get_elem_list(GamesPageLocators.SPORTS_GAMES_LIST)
    assert games_page.get_list_length(GamesPageLocators.SPORTS_GAMES_LIST) == 8

    for i in range(0, len(list_games)):
        selector = f"//*[@id='theme-page']/div[7]/div[2]/div[1]/div/div/ul/li[{i+1}]/img"
        assert games_page.is_image_loaded((By.XPATH, selector)) == True


@when("User scrolls down to 'Action/Shooter' section")
def step_impl(context):
    GamesPage(context).scroll_to_element(GamesPageLocators.ACTION_SECTION)


@then("User can see the correct list of games in 'Action/Shooter' section")
def step_impl(context):
    games_page = GamesPage(context)
    list_games = games_page.get_elem_list(GamesPageLocators.ACTION_GAMES_LIST)
    assert games_page.get_list_length(GamesPageLocators.ACTION_GAMES_LIST) == 4

    for i in range(0, len(list_games)):
        game_name = list_games[i].find_element(By.XPATH, f"//*[@id='theme-page']/div[9]/div[2]/div[1]/div/div/ul/li[{i+1}]/div[2]/div[1]")  
        game_studio = list_games[i].find_element(By.XPATH, f"//*[@id='theme-page']/div[9]/div[2]/div[1]/div/div/ul/li[{i+1}]/div[2]/div[2]")
        test_name, test_studio = JSONParser().get_action_game_name_studio(i)     
        assert game_name.text.lower() == test_name.lower()
        assert game_studio.text.lower() == test_studio.lower()
