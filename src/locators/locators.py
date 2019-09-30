from selenium.webdriver.common.by import By


class Locators:
    message_field = (By.ID, "user-message")
    show_message_button = (By.CSS_SELECTOR, "#get-input > button")
    div_message_id = (By.ID, "display")

    # two input fields
    val_a = (By.ID, "sum1")
    val_b = (By.ID, "sum2")
    get_total_btn = (By.CSS_SELECTOR, "#gettotal > button")
    dsp_value = (By.ID, "displayvalue")

    # checkbox demo page
    check_box_id = (By.ID, "isAgeSelected")
    message_id = (By.ID, "txtAge")

    # multiple checkbox
    options = (By.CLASS_NAME, "cb1-element")
    btn_checkall = (By.ID, "check1")
    hdn = (By.ID, "isChkd")


    # radio button demo
    radio_btn_male = (By.XPATH, "//*[@id=\"easycont\"]/div/div[2]/div[1]/div[2]/label[1]/input")
    radio_btn_female= (By.XPATH, "//*[@id=\"easycont\"]/div/div[2]/div[1]/div[2]/label[2]/input")
    get_checked_button = (By.ID, "buttoncheck")
    checked_message = (By.CLASS_NAME, "radiobutton")


    # select dropdown list
    select_day = (By.ID, "select-demo")
    sel_message = (By.CLASS_NAME, "selected-value")