from selenium.webdriver.common.by import By

class NewsLocators():
    TOP_ARTICLE_HEADER = (By.XPATH, "//*[@id='entry-8929']/div[1]/h3")
    SECOND_ARTICLE_HEADER = (By.XPATH, "//*[@id='entry-8919']/div[1]/h3")
    THIRD_ARTICLE_HEADER = (By.XPATH, "//*[@id='entry-8895']/div[1]/h3")
    THIRD_ARTICLE_LINK = (By.XPATH, "//*[@id='entry-8895']/div[1]/h3/a")
