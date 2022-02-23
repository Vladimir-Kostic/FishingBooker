from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def page_scroll_down_1(self):
        y = 1000
        for timer in range(0, 1):
            self.driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 1000
            time.sleep(1)

    def page_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 350)")
        time.sleep(1)

    def page_scroll_to_element(self, web_element):
        actions = ActionChains(self.driver)
        actions.move_to_element(web_element).perform()

    def page_is_loading(self):
        self.wait.until(lambda driver: driver.execute_script(
            "return document.readyState") == "complete")

    def select_dd_menu(self, web_element, value):
        drop_down = Select(web_element)
        drop_down.select_by_value(value)

    def select_dd_menu_by_text(self, web_element, text):
        drop_down = Select(web_element)
        drop_down.select_by_visible_text(text)

    def wait_element_to_be_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((locator)))
        return element

    def wait_presence_of_all_elements_located(self, locator):
        list_of_elements = self.wait.until(
            EC.presence_of_all_elements_located((locator)))
        return list_of_elements

    def wait_presence_of_element_located(self, locator):
        element = self.wait.until(EC.presence_of_element_located((locator)))
        return element
