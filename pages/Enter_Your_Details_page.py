from locators.Enter_Your_Details_locators import EnterDetailsLocators
from base.base_driver import BaseDriver
from utilities.utilities import Utils
from utilities.custom_logger import LogGen
import time


class EnterDetails(BaseDriver, EnterDetailsLocators):
    logg = Utils.logging_setup()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def first_name_field(self):
        return self.wait_element_to_be_clickable(self.FIRST_NAME)

    def last_name_field(self):
        return self.wait_element_to_be_clickable(self.LAST_NAME)

    def email_address_field(self):
        return self.wait_element_to_be_clickable(self.EMAIL_ADDRESS)

    def mobile_number_field(self):
        return self.wait_element_to_be_clickable(self.MOBILE_NUMBER)

    def text_area_field(self):
        return self.wait_element_to_be_clickable(self.TEXT_AREA_FIELD)

    def submit_button(self):
        return self.wait_element_to_be_clickable(self.SUBMIT_BUTTON)

    def select_country_arrow(self):
        return self.wait_element_to_be_clickable(self.SELECT_COUNTRY)

    def all_countries(self):
        return self.wait_presence_of_all_elements_located(self.All_COUNTRIES)

# ===========================================================================================

    def enter_first_name(self, first_name):
        self.first_name_field().click()
        self.first_name_field().clear()
        self.first_name_field().send_keys(first_name)

    def enter_last_name(self, last_name):
        self.last_name_field().click()
        self.last_name_field().clear()
        self.last_name_field().send_keys(last_name)

    def enter_email_address(self, email):
        self.email_address_field().click()
        self.email_address_field().clear()
        self.email_address_field().send_keys(email)

    def click_country_arrow(self, provide_country):
        self.driver.execute_script(
            "arguments[0].click();", self.select_country_arrow())
        for country in self.all_countries():
            if provide_country in country.text:
                country.click()
                break

    def enter_mobile_number(self, mobile):
        self.mobile_number_field().click()
        self.mobile_number_field().send_keys(mobile)

    def enter_text_area_field(self, text):
        self.text_area_field().click()
        self.text_area_field().clear()
        self.text_area_field().send_keys(text)

    def click_submit_button(self):
        self.submit_button().click()
        self.logg.info(
            "********************** All required personal data are entered successfully **********************")

# ================================================================================

    def enter_details(self, first_name, last_name, email, mobile, text, country):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email_address(email)
        self.click_country_arrow(country)
        self.enter_mobile_number(mobile)
        self.page_scroll_down()
        self.enter_text_area_field(text)
        self.click_submit_button()
        time.sleep(5)
