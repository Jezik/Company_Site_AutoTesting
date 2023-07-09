from selenium.webdriver.common.by import By

class WhatWeDoLocators():
    COMPANY_LOGO = (By.XPATH, "//*[@id='menu-main-menu']/li[2]/a/img")
    TOP_HEADER = (By.XPATH, "//*[@id='fancy-title-1']/span")
    SUB_TOP_HEADER = (By.XPATH, "//*[@id='fancy-title-2']/span")
    GAME_DEV_SECTION = (By.XPATH, "//*[@id='theme-page']/div[5]/div[2]/div[1]/div[1]")
    GAME_PORTING_SECTION = (By.XPATH, "//*[@id='theme-page']/div[7]/div[2]/div[1]/div[2]")
    ENGINEERING_SECTION = (By.XPATH, "//*[@id='theme-page']/div[9]/div[2]/div[1]/div[1]")
    CREATIVE_SECTION = (By.XPATH, "//*[@id='theme-page']/div[11]/div[2]/div[1]/div[2]")
    GAME_DEV_DESCRIPTION_FIRST = (By.XPATH, "//*[@id='fancy-title-5']/span")
    GAME_DEV_DESCRIPTION_SECOND = (By.XPATH, "//*[@id='fancy-title-6']/span")
    GAME_PORTING_DESCRIPTION = (By.XPATH, "//*[@id='fancy-title-10']/span")
    ENGINEERING_DESCRIPTION = (By.XPATH, "//*[@id='fancy-title-13']/span")
    CREATIVE_DESCRIPTION = (By.XPATH, "//*[@id='fancy-title-17']/span")
    ALL_GAMES_BUTTON = (By.XPATH, "//*[@id='theme-page']/div[5]/div[2]/div[1]/div[1]/div[5]")
    PORTFOLIO_BUTTON = (By.XPATH, "//*[@id='theme-page']/div[11]/div[2]/div[1]/div[2]/div[3]")
    REQUEST_INFO_BUTTON = (By.XPATH, "//*[@id='theme-page']/div[9]/div[2]/div[1]/div[1]/div[3]")
    POP_UP_HEADER = (By.XPATH, "//*[text()='Want to receive more information about our Engineering and QA competencies?']")
    COMPANY_CERTIFICATIONS_SECTION = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div[1]")

    #Certifications
    PS5_CERT = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div[1]/div[1]/img")
    STADIA_CERT = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div[1]/div[2]/img")
    XBOX_X_CERT = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div[1]/div[3]/img")
    NINTENDO_CERT = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div[1]/div[4]/img")
    PS4_CERT = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div[1]/div[5]/img")
    XBOX_CERT = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div[1]/div[6]/img")
    ANDROID_CERT = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div[1]/div[7]/img")
    IOS_CERT = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div[1]/div[8]/img")
    PS3_CERT = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div[1]/div[9]/img")
    