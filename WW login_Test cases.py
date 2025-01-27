from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Set up logging to record the outcomes
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_driver():
    options = Options()
    driver = webdriver.Chrome()  # Set your path to chromedriver
    driver.get("https://dev-myworkwise360.azurewebsites.net/")  # Replace with your actual login page URL
    return driver

def login(driver, username, password):
    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Locate email and password fields and login button
    email_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "floating-input")))  # Adjust if needed
    password_input = driver.find_elements(By.CLASS_NAME, "floating-input")[1]  # Target second input (password)
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))  # Adjust if needed

    # Enter credentials
    email_input.clear()
    password_input.clear()
    email_input.send_keys(username)
    password_input.send_keys(password)

    # Click login button
    login_button.click()

def validate_login(driver):
    try:
        # Wait for a known post-login element (e.g., a profile element, dashboard, etc.)
        wait = WebDriverWait(driver, 10)
        profile_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div > div.content > div > div.content-page > div > div > div:nth-child(1) > div > div.col > h3 > span:nth-child(1)")))  # Replace with actual element after login
        logger.info("Login successful. Welcome to Workwise 360!")
        return True
    except Exception as e:
        logger.error(f"Login failed: {e}")
        return False
    
def validate_pop_up(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.Toastify__toast-body"))) 
        return True
    except Exception as e:
        logger.info(e)



# Positive Test Case: Valid login credentials
def test_positive_login():
    driver = setup_driver()
    username = "Rakesh_Adupa@srivensolutions.com"  # Correct test username
    password = "Rakesh@581"  # Correct test password

    try:
        login(driver, username, password)
        if validate_login(driver):
            print("Positive Test: Login successful!")
        else:
            print("Positive Test: Login failed!")
    finally:
        driver.quit()

# Negative Test Case: Incorrect Username
def test_negative_login_incorrect_username():
    driver = setup_driver()
    username = "incorrect_username@example.com"  # Incorrect test username
    password = "Rakesh@581"  # Correct test password

    try:
        login(driver, username, password)
        if validate_pop_up(driver):

            print("Negative Test (Incorrect Username): Test case successful!")
        else:
            print("Negative Test (Incorrect Username): Test case failed!")
    finally:
        driver.quit()

# Negative Test Case: Incorrect Password
def test_negative_login_incorrect_password():
    driver = setup_driver()
    username = "Rakesh_Adupa@srivensolutions.com"  # Correct test username
    password = "incorrect_password"  # Incorrect test password

    try:
        login(driver, username, password)
        if validate_pop_up(driver):
            print("Negative Test (Incorrect Username): Test case successful!")
        else:
            print("Negative Test (Incorrect Username): Test case failed!")
    finally:
        driver.quit()

# Negative Test Case: Empty Username and Password
def test_negative_login_empty_fields():
    driver = setup_driver()
    username = ""  # Empty username
    password = ""  # Empty password

    try:
        login(driver, username, password)
        if validate_pop_up(driver):
            print("Negative Test (Incorrect Username): Test case successful!")
        else:
            print("Negative Test (Incorrect Username): Test case failed!")
    finally:
        driver.quit()

# Negative Test Case: Invalid Email Format
def test_negative_login_invalid_email_format():
    driver = setup_driver()
    username = "invalidemail.com"  # Invalid email format (missing @)
    password = "Rakesh@581"  # Correct password

    try:
        login(driver, username, password)
        if validate_pop_up(driver):
            print("Negative Test (Incorrect Username): Test case successful!")
        else:
            print("Negative Test (Incorrect Username): Test case failed!")
    finally:
        driver.quit()

# Negative Test Case: Special Characters in Username
def test_negative_login_special_characters_username():
    driver = setup_driver()
    username = "Rakesh@#$%"  # Username with special characters
    password = "Rakesh@581"  # Correct password

    try:
        login(driver, username, password)
        if validate_pop_up(driver):
            print("Negative Test (Incorrect Username): Test case successful!")
        else:
            print("Negative Test (Incorrect Username): Test case failed!")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_positive_login()  # Test with valid credentials
    test_negative_login_incorrect_username()  # Test with invalid username
    test_negative_login_incorrect_password()  # Test with invalid password
    test_negative_login_empty_fields()  # Test with empty fields
    test_negative_login_invalid_email_format()  # Test with invalid email format
    test_negative_login_special_characters_username()  # Test with special characters in username
