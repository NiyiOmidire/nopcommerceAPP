# # To run testcase file just go to Terminal at the bottom, type pytest -v -s paste copied relative path of testcase after right click on testcase file, press enter
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger= LogGen.loggen()

    # # def test_homePageTitle(self):  # To reduce the duplication of calling the driver in each testcase, I created a conftest file such that if I call setup, it will return the driver for us
    # #    self.driver = webdriver.Chrome()  #This is how the code would have been b4 replace it with setup
    #  #   self.driver.get(self.baseURL) #

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login ********** ")  # Always use TC name for ur log file name
        self.logger.info("*********** Verifying Home Page Title ********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("*************** Home page title test is passed ********** ")
            self.driver.close()

        else:  # if the testcase failed, it will take screenshot of failed TC. I put relative path of Screenshot folder in bracket
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")  # dot . represents my current project directory (i.e nopComm...), then \\ to show inside this prjt this folder exists. If not it will throw an error. Note name of screnshot should be same as testcase name (+ "test_homePa.png"
            self.driver.close()
            self.logger.error("*************** Home page title test is failed ********** ")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):  # Setup returns my browser
        self.logger.info("*************** Verifying Login test ********** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)  # we need to create an object, lp, to access the actions in LoginPage class inside PageObjects
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************** Login test is passed ********** ")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("*************** Login test is failed ********** ")
            assert False

