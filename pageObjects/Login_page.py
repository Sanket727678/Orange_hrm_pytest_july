from selenium.webdriver.common.by import By


class Login_Page_Class:
    text_username_xpath = "//input[@placeholder='Username']"
    text_password_xpath = "//input[@placeholder='Password']"
    click_login_button = "//button[@type='submit']"
    click_menu_button = "//p[@class='oxd-userdropdown-name']"
    click_logout_button = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def enterusername(self, name):
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(name)

    def enterpassword(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.click_login_button).click()

    def clickmenu(self):
        self.driver.find_element(By.XPATH, self.click_menu_button).click()

    def clicklogout(self):
        self.driver.find_element(By.XPATH, self.click_logout_button).click()

    def verify_login(self):
        try:
            self.driver.find_element(By.XPATH, self.click_menu_button).click()
            self.driver.find_element(By.XPATH, self.click_logout_button).click()
            return "loginpass"

        except:
            return "loginfailed"
