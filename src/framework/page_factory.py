from pages.checkbox_demo import CheckboxDemo
from pages.radiobutton_demo import RadiobuttonDemo
from pages.select_list_demo import SelectListDemo
from pages.simple_form_demo import SimpleFormDemo


class PageFactory():
    "PageFactory uses the factory design pattern."

    @staticmethod
    def get_page_object(driver, page_name, base_url=None,trailing_slash_flag=True):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        print("PageName: %s" % page_name)
        if page_name == "simple_form_demo":
            return SimpleFormDemo(driver=driver, base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        if page_name == "checkbox_demo":
            return CheckboxDemo(driver=driver, base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        if page_name == "radiobutton_demo":
            return RadiobuttonDemo(driver=driver, base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        if page_name == "select_list_demo":
            return SelectListDemo(driver=driver, base_url=base_url,trailing_slash_flag=trailing_slash_flag)

        return test_obj

