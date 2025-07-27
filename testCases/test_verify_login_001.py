import pytest
from selenium import webdriver

from pageObjects.Login_page import Login_Page_Class
from utilities.Logger import logger_class
from utilities.Read_Config import ReadConfig_Class


@pytest.mark.usefixtures("driver_setup")
class Test_Login_001:
    driver = None
    base_url = ReadConfig_Class.get_baseurl()
    login_url = ReadConfig_Class.get_login_url()
    username = ReadConfig_Class.get_username()
    password = ReadConfig_Class.get_password()
    log = logger_class.log_gen_method()

    def test_verify_url_01(self):
        self.log.info("test case test_verify_url_01 is started")
        self.log.info(f"going to base url:{self.base_url}")
        self.driver.get(self.base_url)
        self.log.info("printing title of the page")
        print(self.driver.title)
        self.log.info(f"verifying url of orangehrm:{self.driver.title}")
        if self.driver.title == "OrangeHRM":
            self.log.info("taking screenshots of pass testcase")
            self.driver.save_screenshot(".\\ScreenShots\\test_verify_url_01pass.png")
            print("url is verify")
            assert True
        else:
            self.log.info("taking screenshots of failed testcase")
            self.driver.save_screenshot(".\\ScreenShots\\test_verify_url_01fail.png")
            print("url is not correct")
            assert False

    def test_orangehrm_login_02(self):
        # self.driver = driver_setup
        # driver = webdriver.Chrome()
        self.driver.get(self.login_url)
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)

        lp = Login_Page_Class(self.driver)
        lp.enterusername(self.username)
        lp.enterpassword(self.password)
        lp.clicklogin()

        if lp.verify_login() == "loginpass":
            # lp.clickmenu()
            # lp.clicklogout()
            print("Login Success")
            assert True
        else:
            print("Login Failed")
            assert False
