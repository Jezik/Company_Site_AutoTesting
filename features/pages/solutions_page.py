from .base_page import BasePage
from .json_parser import JSONParser

page_url = JSONParser().get_test_page_url("solutions")

class SolutionsPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver, url=page_url)
        