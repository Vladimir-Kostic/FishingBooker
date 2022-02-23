from selenium.webdriver.common.by import By


class BookingPageLocators:
    TRIP_DATE = (
        By.XPATH, "//input[@id='booking_date_availability_form_search']")
    NEXT_MONTH_BUTTON = (By.CSS_SELECTOR,
                         "div[class='datepicker-days'] th[class='next']")
    DAYS = (By.XPATH, "//select[@id='booking_days']")
    GROUP_SIZE = (By.XPATH, '//*[@data-events-category="Availability search"]')
    ADULTS_PLUS_BUTTON = (
        By.XPATH, '//*[@id="charter-trips"]/div[2]/div/div[3]/div[2]/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td[3]/button')
    ADULTS_MINUS_BUTTON = (
        By.XPATH, '//*[@id="charter-trips"]/div[2]/div/div[3]/div[2]/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td[1]/button')
    CHILDREN_PLUS_BUTTON = (
        By.XPATH, '//*[@id="charter-trips"]/div[2]/div/div[3]/div[2]/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td[3]/button')
    CHILDREN_MINUS_BUTTON = (
        By.XPATH, '//*[@id="charter-trips"]/div[2]/div/div[3]/div[2]/div/table[2]/tbody/tr/td[2]/table/tbody/tr/td[1]/button')
    CHECK_AVAILABILITY = (By.XPATH, "//button[@id='check-availability-btn']")
    INSTANT_BOOK_BUTTON = (By.ID, "bookbtn-0")
    STARTING_MONTH = (By.XPATH, "//th[normalize-space()='February 2022']")
    DAYS_IN_MONTH = (By.XPATH, "//div[@class='datepicker-days']//td")
