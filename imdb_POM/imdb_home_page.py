from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class IMDBHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.actions = ActionChains(driver)

    # Locators
    NOTIFICATION_BUTTON = (By.XPATH, "//button[@class='ipc-icon-button sc-dvXXFO hqYmDU ipc-icon-button--base ipc-icon-button--onBase']")
    EXPAND_BUTTON = (By.XPATH, "//button[@data-testid='adv-search-expand-all']")
    NAME_INPUT = (By.ID, "text-input__3")
    BIRTH_YEAR_MIN = (By.ID, "text-input__10")
    BIRTH_YEAR_MAX = (By.ID, "text-input__11")
    AWARDS_BUTTON = (By.XPATH, "//button[@data-testid='test-chip-id-oscar_nominee']")
    TOPIC_DROPDOWN = (By.ID, "within-topic-dropdown-id")
    SEE_RESULTS_BUTTON = (By.XPATH, "//button[@data-testid='adv-search-get-results']")
    
    # Actions
    def load(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
    
    def handle_notification(self):
        try:
            notification_button = self.wait.until(EC.element_to_be_clickable(self.NOTIFICATION_BUTTON))
            notification_button.click()
            print("Notification button clicked.")
        except Exception as e:
            print(f"Notification button not found or an error occurred: {e}")
    
    def expand_all(self):
        try:
            expand_button = self.wait.until(EC.element_to_be_clickable(self.EXPAND_BUTTON))
            expand_button.click()
            print("Expand All button clicked.")
        except Exception as e:
            print(f"Expand All button not found: {e}")
    
    def fill_name(self, name):
        name_input = self.wait.until(EC.presence_of_element_located(self.NAME_INPUT))
        name_input.send_keys(name)
        print(f"Entered name: {name}")
    
    def fill_birth_years(self, min_year, max_year):
        min_input = self.wait.until(EC.presence_of_element_located(self.BIRTH_YEAR_MIN))
        min_input.send_keys(min_year)
        print(f"Entered minimum birth year: {min_year}")
        
        max_input = self.wait.until(EC.presence_of_element_located(self.BIRTH_YEAR_MAX))
        max_input.send_keys(max_year)
        print(f"Entered maximum birth year: {max_year}")
    
    def select_awards(self):
        try:
            awards_button = self.wait.until(EC.element_to_be_clickable(self.AWARDS_BUTTON))
            awards_button.click()
            print("Clicked on the Awards and Recognition button.")
        except Exception as e:
            print(f"Awards and Recognition button not found: {e}")
    
    def select_topic(self, topic_value):
        try:
            topic_dropdown = self.wait.until(EC.presence_of_element_located(self.TOPIC_DROPDOWN))
            topic_dropdown.send_keys(topic_value)
            print(f"Selected {topic_value} in the topic dropdown.")
        except Exception as e:
            print(f"Topic dropdown not found or not clickable: {e}")
    
    def click_see_results(self):
        see_results_button = self.wait.until(EC.element_to_be_clickable(self.SEE_RESULTS_BUTTON))
        see_results_button.click()
        print("See Results button clicked.")
