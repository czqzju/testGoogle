from locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyttsx3
import time

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):


    def is_title_matches(self):
        """Verifies that the hardcoded text Google appears in page title"""
        return "Google" in self.driver.title

    def click_search_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*HomePageLocators.SEARCH_BUTTON)
        element.click()

    def input_search_content(self, content):
        element = self.driver.find_element(*HomePageLocators.INPUT_AREA)
        element.send_keys(content)

    def voice_input_content(self, content):
        self.driver.find_element(*HomePageLocators.VOICE_BUTTON).click()
        try:
            alert = self.driver.switch_to_alert()
            alert.accept()
        except Exception as e:
            pass

        time.sleep(3)
        engine = pyttsx3.init()

        engine.say(content)

        engine.runAndWait()
        time.sleep(10)

    def click_image_button(self):
        element = self.driver.find_element(*HomePageLocators.IMAGE_BUTTON)
        element.click()
        try:
            element_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(HomePageLocators.IMAGE_INPUT_BUTTON)
            )
            element_input.click()
        except Exception as e:
            # log the exception e
            self.driver.close()

    def image_url_input(self, content):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(HomePageLocators.IMAGE_URL_INPUT)
            )
            element.send_keys(content)
        except Exception as e:
            # log the exception e
            self.driver.quit()

    def image_search_click(self):
        element = self.driver.find_element(*HomePageLocators.IMAGE_SEARCH_BUTTON)
        element.click()



class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def check_search_result(self, content):

        return content in self.driver.page_source

    def check_image_search_result(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(HomePageLocators.IMAGE_RESULT)
            )
            return True
        except Exception as e:
            # log the exception e
            return False