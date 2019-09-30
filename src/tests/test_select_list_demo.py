from framework.page_factory import PageFactory
from framework.test_case import TestCase

class SelectListDemo(TestCase):
    url = "https://www.seleniumeasy.com"

    def test_select_list(self):
        page = PageFactory.get_page_object(self.driver, "select_list_demo", self.url)
        page.open("/test/basic-select-dropdown-demo.html")
        self.takeScreenshot("OpenPage")

        page.select_a_day("Monday")
        assert page.get_selected_day() == "Day selected :- Monday"
