import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from login_Page import LoginPage  # Importing the LoginPage class
import time


def setup_driver():
    options = Options()
    driver = webdriver.Chrome()  # Set path to chromedriver if needed
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
        register_asset_link.click()
        print("Navigating to register asset.")
    except Exception as e:
        print(f"Error navigating to asset management: {e}")

def select_react_option(driver, input_selector, option_text):
    try:
        input_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, input_selector))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
        input_element.click()

        input_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"{input_selector} input.react-select__input"))
        )
        input_field.send_keys(option_text)
        input_field.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Failed to select option '{option_text}' in dropdown: {e}")

def validate_asset_registered(driver):
    try:
        success_popup = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[4]/div/div/div[2]/div/div[2]')
            )
        )
        success_message = success_popup.text.strip()
        expected_message = "Asset Registered successfully."

        if success_message == expected_message:
            print("Validation passed: Asset Registered successfully.")
        else:
            print(f"Validation failed: Expected '{expected_message}', but got '{success_message}'.")
    except Exception as e:
        print(f"Failed to validate asset registration: {e}")

def asset_register_from_csv(driver, csv_file_path):
    try:
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Asset ID
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="assetDetails"]/div[1]/input'))
                ).send_keys(row["AssetID"])
                print("Assigned value to Asset ID.")

                # Serial Number
                driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[2]/input').send_keys(row["SerialNumber"])
                print("Assigned value to Serial Number.")

                # Category Type (Dropdown)
                select_react_option(driver, '#assetDetails > div:nth-child(3) > div > div > div.react-select__value-container.css-hlgwow', row["CategoryType"])

                # Purchase Date
                driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[4]/input').send_keys(row["PurchaseDate"])

                # Purchase Order
                driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[5]/input').send_keys(row["PurchaseOrder"])

                # Purchase Cost
                select_react_option(driver, '#assetDetails > div:nth-child(6) > div > div > div > div > div.react-select__value-container.css-hlgwow > div.react-select__input-container.css-19bb58m',row["Country"])
                driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[6]/div/input').send_keys(row["PurchaseCost"])
                
                # Model
                driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[7]/input').send_keys(row["Model"])

                # Invoice Date
                driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[8]/input').send_keys(row["InvoiceDate"])

                # Invoice Number
                driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[9]/input').send_keys(row["InvoiceNumber"])

                # Upload Invoice
                driver.find_element(By.XPATH, '//*[@id="file"]').send_keys(row["InvoiceFilePath"])

                # Supplier Details
                driver.find_element(By.XPATH, '//*[@id="additionalDetails"]/div[1]/input').send_keys(row["SupplierDetails"])

                # Supplier Contact
                select_react_option(driver, '#additionalDetails > div:nth-child(2) > div',row["Country1"])
                driver.find_element(By.XPATH, '//*[@id="additionalDetails"]/div[2]/div/input').send_keys(row["SupplierContact"])

                # Warranty Start Date
                driver.find_element(By.XPATH, '//*[@id="additionalDetails"]/div[3]/input').send_keys(row["WarrantyStartDate"])

                # Warranty End Date
                driver.find_element(By.XPATH, '//*[@id="additionalDetails"]/div[4]/input').send_keys(row["WarrantyEndDate"])

                # Asset Condition
                select_react_option(driver, '#additionalDetails > div:nth-child(5) > div > div > div.react-select__value-container.css-hlgwow', row["AssetCondition"])

                # Submit form
                driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div[3]/div/button[2]').click()
                print("Form submitted successfully.")

                # Validate registration
                validate_asset_registered(driver)

    except Exception as e:
        print(f"An error occurred while registering assets from CSV: {e}")

if __name__ == "__main__":
    driver = setup_driver()

    # Initialize the login page
    login_page = LoginPage(driver)

    # Perform login
    login_page.enter_email("team@gacdigital.in")  # Replace with valid email
    login_page.enter_password("ACD7BBD6")  # Replace with valid password
    login_page.click_sign_in()

    # Navigate to Register Asset page
    navigate_to_asset_management(driver)

    # Register assets from CSV
    asset_register_from_csv(driver, "asset_data.csv")
    time.sleep(10)

    driver.quit()
