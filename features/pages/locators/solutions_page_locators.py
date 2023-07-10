from selenium.webdriver.common.by import By

class SolutionsLocators():
    COMPANY_LOGO = (By.XPATH, "//*[@id='menu-main-menu']/li[2]/a/img")
    SOLUTIONS_HEADER_MAIN = (By.XPATH, "//*[@id='fancy-title-1']/span")
    SOLUTIONS_HEADER_SECOND = (By.XPATH, "//*[@id='fancy-title-2']/span")
    LIVE_SERVICES_SECTION = (By.XPATH, "//*[@id='theme-page']/div[5]/div[2]/div[1]/div[1]")
    LIVE_SERVICES_DESCRIPTION = (By.XPATH, "//*[@id='fancy-title-5']/span")
    NOC_SECTION = (By.XPATH, "//*[@id='theme-page']/div[7]/div[2]/div[1]/div[2]")
    NOC_DESCRIPTION = (By.XPATH, "//*[@id='fancy-title-9']/span")
    E_COMMERCE_SECTION = (By.XPATH, "//*[@id='theme-page']/div[9]/div[2]/div[1]/div[1]")
    E_COMMERCE_DESCRIPTION = (By.XPATH, "//*[@id='fancy-title-12']/span")
    DEVOPS_SECTION = (By.XPATH, "//*[@id='theme-page']/div[11]/div[2]/div[1]/div[2]")
    DEVOPS_DESCRIPTION_FIRST = (By.XPATH, "//*[@id='theme-page']/div[11]/div[2]/div[1]/div[2]/div/p[1]")
    DEVOPS_DESCRIPTION_SECOND = (By.XPATH, "//*[@id='theme-page']/div[11]/div[2]/div[1]/div[2]/div/p[2]")
    QE_SECTION = (By.XPATH, "//*[@id='theme-page']/div[13]/div[2]/div[1]/div[1]")
    QE_DESCRIPTION_FIRST = (By.XPATH, "//*[@id='fancy-title-18']/span")
    QE_DESCRIPTION_SECOND = (By.XPATH, "//*[@id='fancy-title-19']/span")
    CONTACT_US_BUTTON = (By.XPATH, "//*[text()='Contact Us']")
    CONTACT_US_SEND_BUTTON = (By.XPATH, "//*[text()='Send']")
    