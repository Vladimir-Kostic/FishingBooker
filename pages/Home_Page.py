
from locators.home_page_locators import BookingPageLocators
from base.base_driver import BaseDriver
import time
from utilities.utilities import Utils
from utilities.custom_logger import LogGen


class BookerHomePage(BaseDriver, BookingPageLocators):
    logg = Utils.logging_setup()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


# =================================================================================================
# pretvaranje web elemenata u funkcije

    def trip_date_button(self):
        return self.wait_element_to_be_clickable(self.TRIP_DATE)

    def next_month_button(self):
        return self.wait_element_to_be_clickable(self.NEXT_MONTH_BUTTON)

    def days_button(self):
        return self.wait_element_to_be_clickable(self.DAYS)

    def group_size_button(self):
        return self.wait_element_to_be_clickable(self.GROUP_SIZE)

    def adults_minus_button(self):
        return self.wait_element_to_be_clickable(self.ADULTS_MINUS_BUTTON)

    def children_plus_button(self):
        return self.wait_element_to_be_clickable(self.CHILDREN_PLUS_BUTTON)

    def check_availability(self):
        return self.wait_element_to_be_clickable(self.CHECK_AVAILABILITY)

    # za petlju za klik na sledeci mesec
    def starting_month(self):
        return self.wait_presence_of_element_located(self.STARTING_MONTH)

    def days_in_month(self):
        return self.wait_presence_of_all_elements_located(self.DAYS_IN_MONTH)

    def instant_book_button(self):
        return self.wait_element_to_be_clickable(self.INSTANT_BOOK_BUTTON)


# ==========================================================================================================================
#

    # provuci next button kroz petlju

    def select_trip_date_button(self):
        self.page_scroll_down_1()
        self.trip_date_button().click()
        self.next_month_button().click()
        self.next_month_button().click()
        for date in self.days_in_month():
            if date.text == "4":
                date.click()
                break

    def click_days_field(self):
        self.days_button().click()
        self.select_dd_menu(self.days_button(), "1")

    def click_group_size_field(self):
        self.group_size_button().click()
        self.adults_minus_button().click()
        self.children_plus_button().click()

    def click_check_availability(self):
        self.check_availability().click()

    def click_instant_book_button(self):
        self.instant_book_button().click()
        self.logg.info(
            "********************** All required data are entered successfully **********************")

# ======================================================================================================================

# main function for the home page

    def booking_4_hour_trip(self):
        self.select_trip_date_button()
        self.click_days_field()
        self.click_group_size_field()
        self.click_check_availability()
        self.click_instant_book_button()
