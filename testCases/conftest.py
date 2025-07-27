import pytest
from selenium import webdriver


# @pytest.fixture
# def driver_setup():
#     print("Browser Started")
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#     print("Browser Closed")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class")
def driver_setup(request):
    global driver
    browser_value = request.config.getoption("--browser")
    if browser_value == "chrome":
        print("Launching Chrome Browser")
        driver = webdriver.Chrome()

    elif browser_value == "firefox":
        print("Firefox Browser Started")
        driver = webdriver.Firefox()

    elif browser_value == "edge":
        print("Edge Browser Started")
        driver = webdriver.Edge()

    elif browser_value == "headless":
        print("Headless Browser Started")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    else:
        print("By Default Launching Chrome Browser")
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver

    yield driver
    driver.quit()






    
