import softest
import pytest
from pages.Home_Page import BookerHomePage
import time
from utilities.utilities import Utils
from ddt import ddt, file_data, data, unpack
from pages.Enter_Your_Details_page import EnterDetails
from pages.payment_page import FinalStep
from pages.verification_details_page import FinalPage
from utilities.custom_logger import LogGen


@pytest.mark.usefixtures("setup")
@ddt
class Test_001_Booking(softest.TestCase):
    logg = Utils.logging_setup()

    @pytest.fixture(autouse=True, scope="class")
    def class_setup(self):
        self.home_page = BookerHomePage(self.driver)
        self.enter_details_page = EnterDetails(self.driver)
        self.final = FinalStep(self.driver)

    def test_book_4_hour_trip(self, ):
        self.logg.info(
            "********************** Test_001_Booking with required data *****************************")
        self.home_page.booking_4_hour_trip()

    @data(*Utils.read_data_from_excel(".\\test_data\\enter_your_details_data.xlsx", "Sheet1"))
    @unpack
    def test_enter_details(self, first_name, last_name, email, mobile, text, provide_country):
        self.logg.info(
            "********************** Test_002_Entering personal data in all mandatory fields *****************************")
        self.enter_details_page = EnterDetails(self.driver)
        self.enter_details_page.enter_details(
            first_name, last_name, email, mobile, text, provide_country)

    @data(*Utils.read_data_from_excel(".\\test_data\\final_step_page_data.xlsx", "Sheet1"))
    @unpack
    def test_final_page(self, card_number, expiry_date, cvv_code, card_name, country, postal_code):
        self.logg.info(
            "********************** Test_003_Entering payment paramenters *****************************")
        self.final = FinalStep(self.driver)
        self.final.final_step_validation(
            card_number, expiry_date, cvv_code, card_name, country, postal_code)

    def test_record_ID(self):
        self.logg.info(
            "********************** Test_003_Verifying booking data *****************************")
        self.record = FinalPage(self.driver)
        self.record.read_and_record_data()


# pytest --browser chrome --html=reports\booking_report.html --self-contained-html
