from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Explicit wait for 10 seconds by default

        # Locators
        self.email_locator = (By.CSS_SELECTOR, "input[type='email']")
        self.password_locator = (By.CSS_SELECTOR, "input[type='password']")
        self.sign_in_button_locator = (By.CSS_SELECTOR, "button.btn.btn-primary")

    # Methods
    def enter_email(self, email):
        email_field = self.wait.until(EC.presence_of_element_located(self.email_locator))
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait.until(EC.presence_of_element_located(self.password_locator))  # Added wait here
        password_field.clear()
        password_field.send_keys(password)

    def click_sign_in(self):
        sign_in_button = self.wait.until(EC.element_to_be_clickable(self.sign_in_button_locator))  # Added wait for clickability
        sign_in_button.click()
