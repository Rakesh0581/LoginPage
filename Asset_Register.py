from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
        
        register_asset_link.click()
        print("Navigating to register asset.")
    except Exception as e:
        print(e)   

        # Wait for the input fields and set values

def select_react_option(driver, input_selector, option_text):
    """
    Select an option from a React-based dropdown.
    """
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
    """
    Validates that the asset was registered successfully.
    """
    try:
        # Wait for the success popup to appear
        success_popup = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[4]/div/div/div[2]/div/div[2]')
            )
        )
        success_message = success_popup.text.strip()  # Extracts and cleans the text content
        expected_message = "Asset Registered successfully."  # Replace with the exact success message

        if success_message == expected_message:
            print("Validation passed: Asset Registered successfully.")
        else:
            print(f"Validation failed: Expected '{expected_message}', but got '{success_message}'.")
    except Exception as e:
        print(f"Failed to validate asset registration: {e}")



def asset_register(driver):
    try:

        # Asset ID
        asset_id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="assetDetails"]/div[1]/input'))  # Assuming 'assetID' is the ID of the input field
        )
        asset_id_input.send_keys("B32190HJ")  # Replace with desired asset ID
        print("Assigned value to Asset ID.")

        # Serial Number
        serial_number_input = driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[2]/input')  # Replace 'serialNumber' with the actual ID
        serial_number_input.send_keys("B53gd63")  # Replace with the desired serial number
        print("Assigned value to Serial Number.")

        # Category Type (Select)
        select_react_option(driver, '#assetDetails > div:nth-child(3) > div > div > div.react-select__value-container.css-hlgwow','Laptop')
        print("Value assigned to model.")
    
        # Purchase Date (Format: dd-mm-yyyy)
        purchase_date_input = driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[4]/input')  # Replace with the actual ID of the date field
        purchase_date_input.send_keys("01-01-2023")  # Replace with the desired date
        print("Assigned value to Purchase Date.")


        # Purchase Order
        purchase_order_input = driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[5]/input')  # Replace 'purchaseOrder' with the actual ID
        purchase_order_input.send_keys("PO123456")  # Replace with the desired purchase order number
        print("Assigned value to Purchase Order.")

        # Purchase Cost (Select)
        select_react_option(driver, '#assetDetails > div:nth-child(6) > div > div > div > div > div.react-select__value-container.css-hlgwow > div.react-select__input-container.css-19bb58m','India')

        print("Country code assigned to Purchase cost.")
        purchase_cost_input = driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[6]/div/input')  # Replace 'purchaseCost' with the actual ID
        purchase_cost_input.send_keys("5000")  # Replace with the desired purchase cost
        print("Assigned value to Purchase Cost.")


        # Model
        model_input = driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[7]/input')  # Replace 'model' with the actual ID
        model_input.send_keys("Dell")  # Replace with the desired model
        print("Assigned value to Model.")

        # Invoice Date (Format: dd-mm-yyyy)
        invoice_date_input = driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[8]/input')  # Replace 'invoiceDate' with the actual ID
        invoice_date_input.send_keys("15-01-2023")  # Replace with the desired invoice date
        print("Assigned value to Invoice Date.")

        # Invoice Number
        invoice_number_input = driver.find_element(By.XPATH, '//*[@id="assetDetails"]/div[9]/input')  # Replace 'invoiceNumber' with the actual ID
        invoice_number_input.send_keys("INV7890")  # Replace with the desired invoice number
        print("Assigned value to Invoice Number.")

        # # Upload Invoice
        file_input = driver.find_element(By.XPATH, '//*[@id="file"]')  # Replace XPath with the actual locator of the file input field
        # Provide the path to the file to upload
        file_path = r"C:\Users\GAC-LP0064\Downloads\invoice.pdf"  # Replace with the actual path to the file
        file_input.send_keys(file_path)
        print(f"File '{file_path}' uploaded successfully.")
        # upload_invoice(row["InvoiceFilePath"])

        # Supplier Details
        supplier_details_input = driver.find_element(By.XPATH, '//*[@id="additionalDetails"]/div[1]/input')  # Replace the XPath
        supplier_details_input.send_keys("Dell")  # Replace with the desired supplier details
        print("Assigned value to Supplier Details.")

        # Supplier Contact
        select_react_option(driver, '#additionalDetails > div:nth-child(2) > div','India')
        print("Country code assigned to Supplier Contact.")
        Supplier_Contact = driver.find_element(By.XPATH, '//*[@id="additionalDetails"]/div[2]/div/input')  # Replace 'purchaseCost' with the actual ID
        Supplier_Contact.send_keys("0123456789")  # Replace with the desired purchase cost
        print("Assigned value to Purchase Cost.")

        # Warranty Start Date
        warranty_start_date_input = driver.find_element(By.XPATH, '//*[@id="additionalDetails"]/div[3]/input')  # Replace the XPath
        warranty_start_date_input.send_keys("01-01-2025")  # Replace with the desired start date
        print("Assigned value to Warranty Start Date.")

        # Warranty End Date
        warranty_end_date_input = driver.find_element(By.XPATH, '//*[@id="additionalDetails"]/div[4]/input')  # Replace the XPath
        warranty_end_date_input.send_keys("31-12-2025")  # Replace with the desired end date
        print("Assigned value to Warranty End Date.")

        # Asset Condition
        select_react_option(driver, '#additionalDetails > div:nth-child(5) > div > div','Good')
        print("Value assigned to Asset Condition")

        #submit button
        submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div[3]/div/button[2]')  # Replace '//*[@id="submitButton"]' with the XPath of the submit button
        submit_button.click()
        print("Form submitted successfully.") 

        #validate asset registered successfully
        validate_asset_registered(driver)


    
    except Exception as e:
        print(f"An error occurred while navigating to the Register Asset page or assigning values: {e}")
        

if __name__ == "__main__":
    driver = setup_driver()

    # Initialize the login page
    login_page = LoginPage(driver)
    
    # Perform login
    login_page.enter_email("team@gacdigital.in")  # Replace with valid email
    login_page.enter_password("ACD7BBD6")  # Replace with valid password
    login_page.click_sign_in()
    
    # Navigate to Register Asset page after successful login
    navigate_to_asset_management(driver)
    asset_register(driver)
    time.sleep(10)