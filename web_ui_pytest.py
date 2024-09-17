import pytest
import time  # Import time module for adding sleep delays
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeDriver using webdriver-manager (you can use your specific path if not using webdriver-manager)
service = Service(executable_path=ChromeDriverManager().install())

@pytest.fixture(scope="module")
def setup_browser():
    """Pytest fixture for setting up the browser."""
    print("Setting up browser...")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://www.entrata.com")
    yield driver  # Provide the fixture to the test and keep the browser running
    print("Closing browser...")
    driver.quit()

def test_home_page_title(setup_browser):
    """Test to check the title of the home page."""
    driver = setup_browser
    print("Starting test: test_home_page_title")
    assert "Entrata" in driver.title, "Home page title does not contain 'Entrata'"
    print("Test passed: Home page title contains 'Entrata'")

def test_sign_in_button_text(setup_browser):
    """Test to validate the 'Sign In' button text."""
    driver = setup_browser
    print("Starting test: test_sign_in_button_text")
    
    # Locate the Sign In button at the top right corner (adjust the selector as necessary)
    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign In")

    # Validate the button's text
    assert sign_in_button.text == "Sign In", f"Expected 'Sign In', but got '{sign_in_button.text}'"
    print("Test passed: Sign In button contains the text 'Sign In'")

def test_linkedin_redirect(setup_browser):
    """Test to validate LinkedIn redirection."""
    driver = setup_browser
    print("Starting test: test_linkedin_redirect")

    # Scroll to the bottom of the page to ensure the LinkedIn icon is visible
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Add a delay to allow the page to scroll and the element to load (adjust the time if necessary)
    time.sleep(3)
    
    # Locate the LinkedIn logo element (replace the selector with the appropriate one for the LinkedIn logo)
    linkedin_logo = driver.find_element(By.CSS_SELECTOR, "a[href*='linkedin.com']")
    
    # Use ActionChains to scroll to and click the LinkedIn logo
    ActionChains(driver).move_to_element(linkedin_logo).click().perform()

    # Wait for the new window/tab to be opened
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

    # Switch to the new tab that opens
    driver.switch_to.window(driver.window_handles[1])

    # Get the current URL after the LinkedIn tab opens
    actual_url = driver.current_url

    # Define expected URL and authwall URL
    expected_url = "https://www.linkedin.com/company/entrata/"
    authwall_url = "https://www.linkedin.com/authwall"

    # Assert that the URL is either the expected LinkedIn company page or the authwall
    assert expected_url in actual_url or authwall_url in actual_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    print(f"Test passed: Redirected to LinkedIn page. Actual URL: {actual_url}")

    # Keep the browser open for 4-5 seconds
    time.sleep(5)

    # Close the LinkedIn tab and switch back to the original tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
