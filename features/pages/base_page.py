from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(10)

    def open_url(self):
        self.driver.get(self.url)

    def get_current_url(self):
        return self.driver.current_url
    
    def is_element_exists(self, locator):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
