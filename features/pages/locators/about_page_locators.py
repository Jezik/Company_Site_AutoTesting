from selenium.webdriver.common.by import By

class AboutPageLocators():
    WORLD_CLASS_SECTION = (By.XPATH, "//*[@id='theme-page']/div[5]/div[2]/div[1]/div[3]")
    WORLD_CLASS_DESCRIPTION = (By.XPATH, "//*[@id='fancy-title-5']/span")
    CLIENTS_SECTION = (By.XPATH, "//*[@id='theme-page']/div[9]/div[2]/div[1]/div/div[3]")
    CLIENTS_LIST = (By.XPATH, "//*[@id='theme-page']/div[9]/div[2]/div[1]/div/div[3]/ul/li/*/img[@src]")
    VIEW_ALL_BUTTON = (By.XPATH, "//*[@id='theme-page']/div[9]/div[2]/div[1]/div/div[3]/div[1]/a/i")
    LEADERSHIP_TEAM_SECTION = (By.XPATH, "//*[@id='theme-page']/div[7]/div[2]/div[1]/div/div[1]/ul")
    LEADERSHIP_TEAM_LIST = (By.XPATH, "//*[@id='theme-page']/div[7]/div[2]/div[1]/div/div[1]/ul/li")
    READ_MORE_BUTTON = (By.XPATH, "//*[@id='theme-page']/div[7]/div[2]/div[1]/div/div[2]/a")
    EXECUTIVES_HEADER = (By.XPATH, "//*[@id='fancy-title-1']/span")
