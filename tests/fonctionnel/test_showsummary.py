from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


from tests.conftest  import Driver, Client_test


def login(driver, email):
    email_input = driver.find_element_by_name("email")
    email_input.send_keys(email)
    email_input.submit()

def book_place(driver, number_of_place):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Welcome')]"))
    )
    btn = driver.find_element(By.XPATH, "//html/body/ul/li[1]/a")
    btn.click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Places')]"))
    )
    placesinput = driver.find_element_by_name("places")
    placesinput.send_keys(number_of_place)
    placesinput.submit()


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


class Testbooking(Client_test, Driver):

    @staticmethod
    def test_try_to_book_more_than_point(driver):
        email_test = "admin@irontemple.com"
        number_of_places = 10
        login(driver, email_test)
        book_place(driver,number_of_places)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//li[contains(text(),'You')]"))
        )
        assert "You don't have enough points" in driver.page_source

    @staticmethod
    def test_try_to_book_more_than_12_places(driver):
        email_test = "john@simplylift.co"
        number_of_places = 13
        login(driver, email_test)
        book_place(driver, number_of_places)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//li[contains(text(),'You')]"))
        )
        assert "You can't book than 12 places" in driver.page_source

    @staticmethod
    def test_reflected_purchase(driver):
        email_test = "john@simplylift.co"
        login(driver, email_test)
        number_of_places = 3
        book_place(driver, number_of_places)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//li[contains(text(),'Great')]"))
        )
        assert f"Points available: {4}" in driver.page_source

    @staticmethod
    def test_book_past_competition(driver):
        email_test = "john@simplylift.co"
        login(driver, email_test)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Welcome')]"))
        )
        try:
            driver.find_element(By.XPATH, "//html/body/ul/li[2]/a")
            have_a_link = True
        except NoSuchElementException:
            have_a_link = False
        assert have_a_link == False

