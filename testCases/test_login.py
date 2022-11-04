import pytest
from selenium import webdriver
from testCases import conftest
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUserName()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot("C:\\salesautomation\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = Loginpage(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("****Login test passed ****")
            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\salesautomation\\Screenshots\\test_login.png")
            self.logger.info("****Login test failed****")
            self.driver.close()
            assert False




