from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """Search locator"""
    SEARCH_BUTTON = (By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
    INPUT_AREA = (By.NAME, 'q')
    VOICE_BUTTON=(By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[3]/div[2]')
    IMAGE_BUTTON = (By.XPATH, '//*[@id="gbw"]/div/div/div[1]/div[2]/a')

    IMAGE_INPUT_BUTTON = (By.CLASS_NAME, 'LM8x9c')
    IMAGE_URL_INPUT = (By.NAME, 'image_url')
    IMAGE_SEARCH_BUTTON = (By.XPATH, '//*[@id="aoghAf"]/input')
    IMAGE_RESULT = (By.XPATH, '//*[@id="Z6bGOb"]/a/img')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass