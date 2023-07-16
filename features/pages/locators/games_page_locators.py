from selenium.webdriver.common.by import By

class GamesPageLocators():
    TOP_GAMES_SECTION = (By.XPATH, "//*[@id='theme-page']/div[3]/div[2]/div[1]/div[2]/div/ul")
    TOP_GAMES_LIST = (By.XPATH, "//*[@id='theme-page']/div[3]/div[2]/div[1]/div[2]/div/ul/li")
    CREATIVE_SECTION = (By.XPATH, "//*[@id='theme-page']/div[5]/div[2]/div[1]/div/div")
    CREATIVE_GAMES_LIST = (By.XPATH, "//*[@id='theme-page']/div[5]/div[2]/div[1]/div/div/ul/li")
    SPORTS_SECTION = (By.XPATH, "//*[@id='theme-page']/div[7]/div[2]/div[1]/div/div")
    SPORTS_GAMES_LIST = (By.XPATH, "//*[@id='theme-page']/div[7]/div[2]/div[1]/div/div/ul/li")
    ACTION_SECTION = (By.XPATH, "//*[@id='theme-page']/div[9]/div[2]/div[1]/div/div")
    ACTION_GAMES_LIST = (By.XPATH, "//*[@id='theme-page']/div[9]/div[2]/div[1]/div/div/ul/li")
    