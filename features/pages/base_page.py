from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(10)


    def open_url(self):
        if len(self.url) > 0:
            self.driver.get(self.url)
        else:
            print("Wrong url")


    def get_current_url(self):
        return self.driver.current_url
    

    def is_element_exists(self, locator):
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
    

    def scroll_to_element(self, locator):
        elem = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(elem).perform()

    
    def click_on_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        elem = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(elem).click().perform()


    def wait_tabs_amount_change(self, timeout=10):
        handles_before = self.driver.window_handles
        yield
        WebDriverWait(self.driver, timeout).until(lambda driver: len(handles_before) != len(driver.window_handles))

    
    def switch_to_first_tab(self):
        self.wait_tabs_amount_change()
        self.driver.switch_to.window(self.driver.window_handles[1])


    def close_current_tab(self):
        self.driver.close()
        self.wait_tabs_amount_change()
        self.driver.switch_to.window(self.driver.window_handles[0])


    def press_back_button(self):
        self.driver.execute_script("window.history.go(-1)")

    
    def get_elem_list(self, locator):
        return self.driver.find_elements(*locator)


    def get_list_length(self, locator):
        result_list = self.get_elem_list(locator)
        return len(result_list)
    

    def get_elem_text(self, locator):
        return self.driver.find_element(*locator).text


    def select_dropdown_item_by_text(self, locator, visible_text):
        drop = Select(self.driver.find_element(*locator))
        drop.select_by_visible_text(visible_text)
        