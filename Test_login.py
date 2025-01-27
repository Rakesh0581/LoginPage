from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from login_Page import LoginPage  # Importing the LoginPage class

def setup_driver():
    # Setup the driver and open the URL
    options = Options()
    driver = webdriver.Chrome()  # Set your path to chromedriver if needed
    driver.get("https://dev-myworkwise360.azurewebsites.net/")  # Replace with the actual login URL
    return driver

def navigate_to_asset_management(driver):
    try:
       
        # Wait for the "Register Asset" menu button to be clickable and then click it
        assetmanagement_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#icon-pills-tab > li:nth-child(3) > a")) 
        )
        assetmanagement_button.click()
        
        print("Navigating to asset management.")

        # Wait for the asset management link to be clickable and click it
        register_asset_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="asset-management"]/li[1]/a'))
        )
        time.sleep(5)
        register_asset_link.click()

        print("Navigating to register asset.")

    
    except Exception as e:
        print(f"An error occurred while navigating to the Register Asset page: {e}")


if __name__ == "__main__":
    driver = setup_driver()

    # Initialize the login page
    login_page = LoginPage(driver)
    
    # Perform login"
    login_page.enter_email("team@gacdigital.in")  # Replace with valid email
    login_page.enter_password("ACD7BBD6")  # Replace with valid password
    login_page.click_sign_in()
    
    # Navigate to Register Asset page after successful login
    navigate_to_asset_management(driver)
    time.sleep(10)
