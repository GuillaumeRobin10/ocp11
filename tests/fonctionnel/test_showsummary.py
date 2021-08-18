from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from tests.conftest  import Driver, Client_test


def login(driver, email):
    email_input = driver.find_element_by_name("email")
    email_input.send_keys(email)
    email_input.submit()

class Testlogin(Client_test, Driver):
    """This is class for ui tests."""

    @staticmethod
    def test_login_is_invalid(driver):
        """Test as index and show_summary routes endpoint."""
        # the user enters his email and clicks on the "enter" button.
        # it is redirected to index page with a error message.
        login(driver,"unknown@unknown.com")
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//li[contains(text(),'Sorry')]"))
        )
        assert "Sorry, that email wasn't found." in driver.page_source

    @staticmethod
    def test_login_is_valid(driver):
        """Test as index and show_summary routes endpoint."""
        # the user enters his email and clicks on the "enter" button.
        # .
        email_test="john@simplylift.co"
        login(driver, email_test)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Welcome')]"))
        )
        assert f"Welcome, {email_test}" in driver.page_source



