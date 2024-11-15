from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

# Open the target page
driver.get("https://example.com")  # Replace with the actual main page URL

try:
    # Step 1: Click the "mobile-toggle-btn" to open the mobile menu
    mobile_toggle_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mobile-toggle-btn"))
    )
    mobile_toggle_button.click()
    print("Clicked the mobile toggle button successfully!")

    # Step 2: Click the "mob-nav-login" link to navigate to the login page
    mobile_login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mob-nav-login"))
    )
    mobile_login_link.click()
    print("Clicked the mobile login link successfully!")

    # Step 3: Log in
    # Locate and fill in the username field
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))  # Replace with the actual ID
    )
    username_input.send_keys("username")  # Replace with your actual username

    # Locate and fill in the password field
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))  # Replace with the actual ID
    )
    password_input.send_keys("password")  # Replace with your actual password

    # Locate and click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-submit"))  # Replace with the actual login button ID
    )
    login_button.click()
    print("Logged in successfully!")

    # Step 4: Perform search actions after login
    # Click the "submit-search" link
    submit_search_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-search"))
    )
    submit_search_link.click()
    print("Clicked the submit-search link successfully!")

    # Step 5: Click the "filter-group-btn-Remote" button
    remote_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "filter-group-btn-Remote"))
    )
    remote_button.click()
    print("Clicked the filter-group-btn-Remote button successfully!")

    # Step 6: Check the input with ID "cat-checkbox-100%-Remote-Work"
    remote_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cat-checkbox-100%-Remote-Work"))
    )
    if not remote_checkbox.is_selected():  # Check if the checkbox is already selected
        remote_checkbox.click()
    print("Checked the 100%-Remote-Work checkbox successfully!")

    # Step 7: Type "Florida" into the input with ID "search-by-location"
    location_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search-by-location"))
    )
    location_input.clear()  # Clear any pre-filled text in the input field
    location_input.send_keys("Florida")
    print("Typed 'Florida' into the location search box successfully!")

    # Step 8: Click the "submit-search" button again to execute the search
    submit_search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-search"))
    )
    submit_search_button.click()
    print("Clicked the submit-search button again to execute the search!")

except Exception as e:
    print(f"Error occurred: {e}")

# Close the driver
driver.quit()
