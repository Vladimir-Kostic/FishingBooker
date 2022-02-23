from locators.final_page_locators import FinalPageLocators
from base.base_driver import BaseDriver
from utilities.utilities import Utils
from utilities.custom_logger import LogGen
import time


class FinalPage(BaseDriver, FinalPageLocators):
    logg = Utils.logging_setup()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def booking_id(self):
        return self.wait_presence_of_element_located(self.BOOKING_ID)
# ===========================================================

    def read_and_record_data(self):
        record_data = Utils()
        record_data.write_text_to_file(
            f"Your verification number is: {self.booking_id().text}")
        self.logg.info(
            "********************** Verification is successful ********************** ")
