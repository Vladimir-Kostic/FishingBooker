from selenium.webdriver.common.by import By


class EnterDetailsLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='Enter your first name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Enter your last name']")
    EMAIL_ADDRESS = (By.XPATH, "//input[@placeholder='Watch out for typos']")
    MOBILE_NUMBER = (By.XPATH, "//input[@placeholder='+381 60 1234567']")
    TEXT_AREA_FIELD = (
        By.XPATH, "//*[@data-testid='special-requests-textarea']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    SELECT_COUNTRY = (By.XPATH, "//div[@class='iti-arrow']")
    All_COUNTRIES = (By.XPATH, "//ul[@class='country-list']//li")
