import json
from multiprocessing import Process
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


from server import app

class Client_test:
    """This is class for create fixture."""
    @staticmethod
    @pytest.fixture(scope="module")
    def client():
        with app.test_client() as client:
            yield client


class Driver:
    """This is class for create fixture."""

    @staticmethod
    @pytest.fixture(scope="function")
    def driver():
        process = Process(target=app.run)
        process.daemon = True
        process.start()
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:5000")
        return driver
