from framework.page_factory import PageFactory
from framework.test_case import TestCase


class SimpleFormTest(TestCase):
    url = "https://www.seleniumeasy.com"

    def test_single_form(self):
        page = PageFactory.get_page_object(self.driver, "simple_form_demo", self.url)
        page.open("/test/basic-first-form-demo.html")
        self.takeScreenshot("OpenPage")
        page.enter_message("try me")
        page.click_show_message()
        assert page.get_text_form1() == "try me"
        self.takeScreenshot("Finish")

    def test_two_fields(self):
        page = PageFactory.get_page_object(self.driver, "simple_form_demo", self.url)
        page.open("/test/basic-first-form-demo.html")
        self.takeScreenshot("OpenPage")
        page.enter_value_a(2)
        page.enter_value_b(8)
        page.calculate()
        assert page.get_total() == "10"
        self.takeScreenshot("Finish")