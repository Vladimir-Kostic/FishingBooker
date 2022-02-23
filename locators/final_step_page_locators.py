from selenium.webdriver.common.by import By


class FinalStepPageLocators:
    CARD_NUMBER_FIELD = (By.XPATH, '//*[@id="credit-card-number"]')
    EXPIRY_DATE_FIELD = (By.XPATH, '//*[@id="expiration"]')
    SECURITY_CODE_CVV = (By.XPATH, '//*[@id="cvv"]')
    CARD_NAME = (By.XPATH, '//*[@id="cardholder-name"]')
    BILLING_COUNTRY_FIELD = (By.XPATH, "//select[@class='sc-gmeYpB cctUZJ']")
    POSTAL_CODE_FIELD = (By.XPATH, '//*[@id="postal-code"]')
    CONFIRM_BOOKING = (By.XPATH, "//button[@type='submit']")
    CARD_NUMBER_IFRAME = (By.XPATH, '//*[@id="braintree-hosted-field-number"]')
    EXPIRY_DATE_IFRAME = (
        By.XPATH, "//iframe[@id='braintree-hosted-field-expirationDate']")
    SECURITY_CODE_CVV_IFRAME = (
        By.XPATH, "//iframe[@id='braintree-hosted-field-cvv']")
    CARD_NAME_IFRAME = (
        By.XPATH, "//iframe[@id='braintree-hosted-field-cardholderName']")
    POSTAL_CODE_IFRAME = (
        By.XPATH, "//iframe[@id='braintree-hosted-field-postalCode']")
