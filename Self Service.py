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

def navigate_to_Selfservice(driver):
    try:
        # Wait for the "Advance_salary" menu button to be clickable and then click it
        Selfservice_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#icon-pills-tab > li:nth-child(4) > a > span > i")) 
        )
        Selfservice_button.click()       
        print("Navigating to Selfservice.")

       
        AdvanceSalary_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="self-service-pan"]/div[2]/div/div[4]/div/a'))
        )
        
        AdvanceSalary_link.click()
        print("Navigating to AdvanceSalary.")
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

def Validate_Advance_Salary_Request(driver):
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
        expected_message = "Advance Salary Requested successfully."  # Replace with the exact success message

        if success_message == expected_message:
            print("Validation passed: Advance Salary Requested successfully.")
        else:
            print(f"Validation failed: Expected '{expected_message}', but got '{success_message}'.")
    except Exception as e:
        print(f"Failed to validate asset registration: {e}")



def Advance_salary(driver):
    try:

        # Amount (Select)
        select_react_option(driver, '#root > div > div.content > div > div.content-page > div > div:nth-child(2) > div.col-lg-8 > div > div > form > div > div:nth-child(1) > div > div > div > div > div','India')
        print("Country code assigned to Amount.")

        Amount_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div/form/div/div[1]/div/div/input')  # Replace 'Amount' with the actual ID
        Amount_input.send_keys("5000")  # Replace with the desired Amount
        print("Assigned value to Amount.")


        # Reason
        model_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div/form/div/div[2]/div/input')  # Replace 'Reason' with the actual ID
        model_input.send_keys("Medical")  # Replace with the desired model
        print("Assigned value to Reason.")


        # Description
        invoice_number_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div/form/div/div[3]/div/textarea')  # Replace 'invoiceNumber' with the actual ID
        invoice_number_input.send_keys("Hospital expenses")  # Replace with the desired Description
        print("Assigned value to Description.")


        #submit button
        submit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div[3]/div/button[2]')  # Replace '//*[@id="submitButton"]' with the XPath of the submit button
        submit_button.click()
        print("Form submitted successfully.") 

        #validate asset registered successfully
        Validate_Advance_Salary_Request(driver)


    
    except Exception as e:
        print(f"An error occurred while navigating to the Advance_salary page or assigning values: {e}")
        

if __name__ == "__main__":
    driver = setup_driver()

    # Initialize the login page
    login_page = LoginPage(driver)
    
    # Perform login
    login_page.enter_email("team@gacdigital.in")  # Replace with valid email
    login_page.enter_password("ACD7BBD6")  # Replace with valid password
    login_page.click_sign_in()
    
    # Navigate to Advance_salary page after successful login
    navigate_to_Selfservice(driver)
    Advance_salary(driver)
    time.sleep(10)