import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from imdb_home_page import IMDBHomePage


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument(f"window-size={1280},{720}")
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestIMDBSearch:
    def test_imdb_search(self):
        # URL of the IMDB Name Search page
        url = "https://www.imdb.com/search/name/"
        
        # Create an instance of the IMDBHomePage
        imdb_page = IMDBHomePage(self.driver)
        imdb_page.load(url)

        # Handle notification popup
        imdb_page.handle_notification()

        # Expand all search options
        imdb_page.expand_all()

        # Fill in the search fields
        imdb_page.fill_name("Tom Cruise")
        imdb_page.fill_birth_years("1950", "1970")
        imdb_page.select_awards()
        imdb_page.select_topic("QUOTES")

        # Click the "See Results" button
        imdb_page.click_see_results()

       