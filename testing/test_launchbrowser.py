import pytest
from selenium.webdriver.chrome.service import Service
from selenium  import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.regression()
def test_launchBrowser():

    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.google.com")

    assert 5==5
@pytest.mark.sanity()
def test_launchBrowser1():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.google.com")

    assert 5 == 4