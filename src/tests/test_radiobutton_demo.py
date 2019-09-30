from framework.page_factory import PageFactory
from framework.test_case import TestCase

class RadioButtonDemo(TestCase):
    url = "https://www.seleniumeasy.com"

    def test_radio_btn(self):
        page = PageFactory.get_page_object(self.driver, "radiobutton_demo", self.url)
        page.open("/test/basic-radiobutton-demo.html")
        self.takeScreenshot("OpenPage")

        page.click_male_btn()
        page.click_get_checked_value_btn()
        assert page.get_checked_message() == "Radio button 'Male' is checked"
        self.takeScreenshot("Click male button")
        page.click_female_btn()
        page.click_get_checked_value_btn()
        assert page.get_checked_message() == "Radio button 'Female' is checked"
        self.takeScreenshot("Click female button")
