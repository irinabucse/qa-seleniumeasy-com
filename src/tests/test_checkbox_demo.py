from framework.page_factory import PageFactory
from framework.test_case import TestCase
import time

class CheckboxDemo(TestCase):
    url = "https://www.seleniumeasy.com"
    def test_check(self):
        page = PageFactory.get_page_object(self.driver, "checkbox_demo", self.url)
        page.open("/test/basic-checkbox-demo.html")
        self.takeScreenshot("OpenPage")
        page.check_box1()
        assert page.get_message() == "Success - Check box is checked"
        self.takeScreenshot("End Test Check")

    def test_multiple_checkbox(self):
        page = PageFactory.get_page_object(self.driver, "checkbox_demo", self.url)
        page.open("/test/basic-checkbox-demo.html")
        self.takeScreenshot("OpenPage")
        page.checkall()
        self.takeScreenshot("Click \"Check all\" button")
        assert "Uncheck All" == page.get_checkall_btn_value()
        assert "true" == page.get_ischecked()

        page.click_checkbox(0)
        time.sleep(1)
        self.takeScreenshot("Deselect Checkbox 1")

        assert "Check All" == page.get_checkall_btn_value()
        assert  "false" == page.get_ischecked()

        page.click_checkbox(0)
        time.sleep(1)
        self.takeScreenshot("Select Checkbox 1")

        assert "Uncheck All" == page.get_checkall_btn_value()
        assert "true" == page.get_ischecked()

        self.takeScreenshot("End Test Multiple Checkbox ")

