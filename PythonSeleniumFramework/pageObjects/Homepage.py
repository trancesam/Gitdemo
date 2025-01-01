from selenium.webdriver.common.by import By


class Homepage:
    shop = (By.LINK_TEXT, "Shop") #shop is the class variable

    def __init__(self,driver):
        self.driver=driver

    def shopitems(self):
        return self.driver.find_element(*Homepage.shop) #calling class variable in the argument by using class name
#*Homepage.shop-- here * is used to unpack the tuple Homepage.shop so that desirable argument- By.LINK_TEXT, "Shop", gets inserted.