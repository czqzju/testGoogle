import unittest
from selenium import webdriver
import page
from selenium.webdriver.chrome.options import Options



class TestGoogle(unittest.TestCase):

    def setUp(self):
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome('webdrivers/chromedriver', options=self.chrome_options)
        self.driver.get("https://www.google.co.nz")
        self.main_page = page.HomePage(self.driver)
        assert self.main_page.is_title_matches(), "Home page load failed!"

    def test_key_word_search(self):
        content = "animal"

        self.main_page.input_search_content(content)
        self.main_page.click_search_button()
        search_result_page = page.SearchResultsPage(self.driver)
        assert search_result_page.check_search_result(content), "{} search failed".format(content)

    def test_voice_input_search(self):
        content = "animal"

        self.main_page.voice_input_content(content)

        search_result_page = page.SearchResultsPage(self.driver)
        assert search_result_page.check_search_result(content), "{} voice search failed".format(content)

    def test_image_input_search(self):

        imageLink = "https://c-ssl.duitang.com/uploads/item/201209/01/20120901083238_GiQaC.thumb.1000_0.jpeg"
        self.main_page.click_image_button()
        self.main_page.image_url_input(imageLink)
        self.main_page.image_search_click()

        search_result_page = page.SearchResultsPage(self.driver)
        search_result_page.check_image_search_result()

        assert search_result_page.check_image_search_result(), "{} image search failed!".format(imageLink)

    def tearDown(self):
        self.driver.close()
