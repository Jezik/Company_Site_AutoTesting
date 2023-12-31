from selenium.webdriver.common.by import By

class MainPageLocators():
    COMPANY_LOGO = (By.XPATH, "//*[@id='menu-main-menu']/li[2]/a/img")
    JOB_OPPORTUNITY_TITLE = (By.XPATH, "//*[@id='fancy-title-11']/span")
    FACEBOOK_LINK = (By.XPATH, "//*[@data-tag='facebook']")
    TWITTER_LINK = (By.XPATH, "//*[@data-tag='twitter']")
    INSTAGRAM_LINK = (By.XPATH, "//*[@data-tag='instagram']")
    LINKEDIN_LINK = (By.XPATH, "//*[@data-tag='linkedin']")
    WHAT_WE_DO_LINK = (By.XPATH, "//*[@id='menu-item-215']/a")
    SOLUTIONS_LINK = (By.XPATH, "//*[@id='menu-item-6516']/a")
    GAMES_LINK = (By.XPATH, "//*[@id='menu-item-156']/a")
    ABOUT_LINK = (By.XPATH, "//*[@id='menu-item-216']/a")
    NEWS_LINK = (By.XPATH, "//*[@id='menu-item-3685']/a")
    CAREERS_LINK = (By.XPATH, "//*[@id='menu-item-213']/a")
    EXPLORE_BUTTON = (By.XPATH, "//*[@id='theme-page']/div[3]/div[2]/div[1]/div/div/div[1]/div/div/div/div/div/div[3]/a")
    LEARN_ABOUT_COMPANY_BUTTON = (By.XPATH, "//*[@id='theme-page']/div[9]/div[2]/div[1]/div/div/div[1]/div[6]/a")
    VACANCIES_BUTTON = (By.XPATH, "//*[@id='theme-page']/div[9]/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[10]/a")
    READ_MORE_BUTTON = (By.XPATH, "//*[@id='theme-page']/div[11]/div[4]/div[1]/div/div/a")
    LAST_NEWS_SECTION = (By.XPATH, "//*[@id='theme-page']/div[7]/div[2]/div[1]/div/div/ul")
    LAST_NEWS_LIST = (By.XPATH, "//*[@id='theme-page']/div[7]/div[2]/div[1]/div/div/ul/li")
    ARTICLE_FOR_TEST_LINK = (By.XPATH, "//*[@id='theme-page']/div[7]/div[2]/div[1]/div/div/ul/li[1]/a")
    PARTNERS_SECTION = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div/ul")
    PARTNERS_LIST = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div/div/ul/li")
