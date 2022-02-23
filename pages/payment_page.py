from locators.final_step_page_locators import FinalStepPageLocators
from base.base_driver import BaseDriver
import time
from utilities.utilities import Utils
from utilities.custom_logger import LogGen


class FinalStep(BaseDriver, FinalStepPageLocators):
    logg = Utils.logging_setup()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def card_number_field(self):
        return self.wait_element_to_be_clickable(self.CARD_NUMBER_FIELD)

    def expiry_date_field(self):
        return self.wait_element_to_be_clickable(self.EXPIRY_DATE_FIELD)

    def security_code_cvv(self):
        return self.wait_element_to_be_clickable(self.SECURITY_CODE_CVV)

    def card_name_field(self):
        return self.wait_element_to_be_clickable(self.CARD_NAME)

    def billing_country_field(self):
        return self.wait_element_to_be_clickable(self.BILLING_COUNTRY_FIELD)

    def postal_code_field(self):
        return self.wait_element_to_be_clickable(self.POSTAL_CODE_FIELD)

    def confirm_booking_button(self):
        return self.wait_element_to_be_clickable(self.CONFIRM_BOOKING)

    def card_number_iframe(self):
        return self.wait_presence_of_element_located(self.CARD_NUMBER_IFRAME)

    def expiry_date_iframe(self):
        return self.wait_presence_of_element_located(self.EXPIRY_DATE_IFRAME)

    def security_code_cvv_iframe(self):
        return self.wait_presence_of_element_located(self.SECURITY_CODE_CVV_IFRAME)

    def card_name_iframe(self):
        return self.wait_presence_of_element_located(self.CARD_NAME_IFRAME)

    def postal_code_iframe(self):
        return self.wait_presence_of_element_located(self.POSTAL_CODE_IFRAME)


# ===================================================================================================
# opcija da se iframe-ovi provuku kroz petlju, pa da se na osnovu atributa odabere trazeno polje?


    def select_card_number_field(self, card_number):
        self.driver.switch_to.frame(self.card_number_iframe())
        self.card_number_field().click()
        self.card_number_field().send_keys(card_number)
        self.driver.switch_to.default_content()

    def select_expiry_date_field(self, expiry_date):
        self.driver.switch_to.frame(self.expiry_date_iframe())
        self.expiry_date_field().click()
        self.expiry_date_field().send_keys(expiry_date)
        self.driver.switch_to.default_content()

    def select_security_code_cvv_field(self, cvv_code):
        self.driver.switch_to.frame(self.security_code_cvv_iframe())
        self.security_code_cvv().click()
        self.security_code_cvv().send_keys(cvv_code)
        self.driver.switch_to.default_content()

    def select_card_name_field(self, card_name):
        self.driver.switch_to.frame(self.card_name_iframe())
        self.card_name_field().click()
        self.card_name_field().send_keys(card_name)
        self.driver.switch_to.default_content()

    def select_billing_country(self, country):
        self.billing_country_field().click()
        self.select_dd_menu_by_text(self.billing_country_field(), country)

    def select_postal_code_field(self, postal_code):
        self.driver.switch_to.frame(self.postal_code_iframe())
        self.postal_code_field().click()
        self.postal_code_field().send_keys(postal_code)
        self.driver.switch_to.default_content()
        time.sleep(5)

    def click_confirm_booking_button(self):
        self.confirm_booking_button().click()
        self.logg.info(
            "********************** All required data for payment are entered successfully **********************")

# ==========================================================================================================

    def final_step_validation(self, card_number, expiry_date, cvv_code, card_name, country, postal_code):
        self.page_scroll_down()
        self.select_card_number_field(card_number)
        self.select_expiry_date_field(expiry_date)
        self.select_security_code_cvv_field(cvv_code)
        self.select_card_name_field(card_name)
        self.select_billing_country(country)
        self.select_postal_code_field(postal_code)
        self.click_confirm_booking_button()
        self.page_is_loading()
        time.sleep(5)
