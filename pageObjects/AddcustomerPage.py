import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    # Add customer Page
    linkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtcustomerRoles_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    listitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    listitemforumModerators_xpath = "//li[contains(text(),'Forum Moderators')]"
    listitemGuests_xpath = "//li[contains(text(),'Guests')]"
    listitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    listitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//select[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()
        elif gender=="Female":
            self.driver.find_element(By.ID, self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click() # Here means if I did not select any gender, then default will be Male

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH, self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(comname)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemAdministrators_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemforumModerators_xpath)
        elif role == "Guests":
            # Here user can be Registered (or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click() # Inspect the x at the end of listed item
            self.listitem = self.driver.find_element(By.XPATH, self.listitemGuests_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemRegistered_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.listitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.listitemGuests_xpath) # If not is selected by default , then i will select Guest as default
        time.sleep(3)
        ## self.listitem.click(); # This click action is not working on the list items there we use execute script wch is JavaScript
        self.driver.execute_script("arguments[0].click();", self.listitem) # This is a JavaScript statement to perform click on

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH, self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()



