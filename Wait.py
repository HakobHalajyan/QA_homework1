from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Wait:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_type_enum, locator,
                         timeout=10):
        element = None
        try:
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be visible")
            element = WebDriverWait(self.driver, timeout).\
                until(EC.visibility_of_element_located((locator_type_enum, locator)))
            print("Element appeared on the web page")
        except NoSuchElementException:
            print("Element not appeared on the web page")
        return element