from framework.base_page import BasePage
from locators.locators import Locators


class SelectListDemo(BasePage):
    def select_a_day(self, day):
        self.select_dropdown_option(Locators.select_day, day)

    def get_selected_day(self):
        return self.get_text(Locators.sel_message)
