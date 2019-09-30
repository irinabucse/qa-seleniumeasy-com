from framework.base_page import BasePage
from locators.locators import Locators


class CheckboxDemo(BasePage):
    def check_box1(self):
        self.click_element(Locators.check_box_id)

    def get_message(self):
        return self.get_text(Locators.message_id)

    def checkall(self):
        self.click_element(Locators.btn_checkall)

    def get_checkall_btn_value(self):
        return self.get_element(Locators.btn_checkall).get_attribute("value")

    def click_checkbox(self, index):
        elements = self.get_elements(Locators.options)
        elements[index].click()

    def get_ischecked(self):
        return self.get_element(Locators.hdn).get_attribute("value")

