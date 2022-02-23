from selenium.webdriver.common.by import By


class FinalPageLocators:
    CREATE_PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    CREATE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    BOOKING_ID = (By.CSS_SELECTOR, "strong[data-testid='booking-id']")
