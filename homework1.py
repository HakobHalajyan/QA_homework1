from selenium import webdriver
from selenium.webdriver.common.by import By

from QA_homeworks.Wait import Wait

class One_time_functions:
    # requires browser type
    def __init__(self,browser):
        self.browser=browser.lower()
        if(self.browser=="chrome"):
            self.driver = webdriver.Chrome()
        elif(self.browser=="firefox"):
            driver = webdriver.Firefox()
        elif (self.browser == "Edge"):
            driver = webdriver.Edge()
        self.waitObject1 = Wait(self.driver)

    def site_opener(self):
        self.driver.implicitly_wait(4)
        self.driver.get("https://www.demoblaze.com/")

    def navbar_check(self):
        self.driver.implicitly_wait(4)
        self.driver.get("https://www.demoblaze.com/")
        try:
            self.driver.find_element(By.XPATH, "//from[@id='navbarExample']/ul/li[1]/a")
            print("Element is located")
        except:
            print("No Such Element")

    def categories_check(self):
        self.driver.implicitly_wait(4)

