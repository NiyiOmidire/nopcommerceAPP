# #To run testcase file just go to Terminal at the bottom, type pytest -v -s paste copied relative path of testcase after right click on testcase file, press enter
import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("*********** Test_002_DDT_Login **********")
        self.logger.info("*************** Verifying Login DDT test ********** ")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver) # we need to create an object, lp, to access the actions in LoginPage class inside PageObjects

        self.rows=XLUtils.getRowCount(self.path,'sheet1')
        print("Number of rows in Excel:",self.rows)
        list_status=[] # Empty list variable
        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'sheet1',r,1)
            self.password=XLUtils.readData(self.path,'sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'sheet1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("***** Passed *****")
                    self.lp.clickLogout()
                    list_status.append("pass")
                elif self.exp=="Fail":
                    self.logger.info("***** Failed *****")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp=='Pass':
                    self.logger.info("**** Failed ****")
                    list_status.append("Fail")
                elif self.exp== "Fail":
                    self.logger.info("**** Passed ****")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("***** Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT test failed ***")
            self.driver.close()
            assert False
        self.logger.info("***** End of Login DDT Test *****")
        self.logger.info("***** Completed TC_Login_DDT_002 *****");



