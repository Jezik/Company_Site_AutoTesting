from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver, url="https://sperasoft.com/")
