from selenium.webdriver.common.by import By

class CareerLocators():
    BIG_HEADER_PART1 = (By.XPATH, "//*[@id='fancy-title-1']/span")
    BIG_HEADER_PART2 = (By.XPATH, "//*[@id='fancy-title-2']/span")
    JOBS_SPERASOFT_SECTION = (By.XPATH, "//*[@id='theme-page']/div[5]/div[2]/div[1]/div")
    ABOUT_US_LINK = (By.XPATH, "//*[@id='theme-page']/div[3]/div[2]/div[1]/div[2]/div/ul/li[1]/a")
    BOOTCAMP_LINK = (By.XPATH, "//*[@id='theme-page']/div[3]/div[2]/div[1]/div[2]/div/ul/li[2]/a")
    NEWS_LINK = (By.XPATH, "//*[@id='theme-page']/div[3]/div[2]/div[1]/div[2]/div/ul/li[3]/a")
    SELECT_CITY_DROPDOWN = (By.XPATH, "//*[@id='theme-page']/div[5]/div[2]/div[1]/div/div[1]/div[2]/div[1]/select[1]")
    FIRST_ENGINEERING_JOB_LINK = (By.XPATH, "//*[@id='theme-page']/div[5]/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[4]/a")
