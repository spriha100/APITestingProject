import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture(scope="function")
@pytest.fixture(scope="module")
def test_launchChrome():
    global driver
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    yield
    driver.quit()

@pytest.fixture(scope="class")
def test_launchBrowser(request):
    # global driver
    request.cls.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver.get("https://www.google.com")
    yield
    request.cls.driver.quit()

@pytest.mark.gettitle
def test_open_url(test_launchChrome):
    driver.get("https://www.google.com")
    driver.title
    assert 5==4

@pytest.mark.gettitle
def test_getTitle(test_launchChrome):
    driver.get("https://www.google.com")
    driver.current_url

    assert 5==5

@pytest.mark.usefixtures("test_launchBrowser")
class Test_google:

    @pytest.mark.runit
    def test_enter_url(self):
        self.driver.get("https://www.google.com")


