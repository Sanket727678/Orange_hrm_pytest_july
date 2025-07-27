import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig_Class():

    @staticmethod
    def get_username():
        username = config.get('Login Data', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('Login Data', 'password')
        return password

    @staticmethod
    def get_baseurl():
        baseurl = config.get('Application Url', 'base_url')
        return baseurl

    @staticmethod
    def get_login_url():
        loginurl = config.get('Application Url', 'login_url')
        return loginurl


