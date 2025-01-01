import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#from pythonProject1.utilities.BaseClass import BaseClass

from PythonSeleniumFramework.pageObjects.Homepage import Homepage
from PythonSeleniumFramework.pythonProject1.utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        HomePage=Homepage(self.driver)
        self.driver.implicitly_wait(10)
        HomePage.shopitems().click()
        #self.driver.find_element(By.LINK_TEXT, "Shop").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in products:
            # wait=WebDriverWait(product, 5)
            # wait.until(expected_conditions.presence_of_element_located((By.XPATH, '/div/h4/a')))
            product_name = product.find_element(By.XPATH, 'div/h4/a').text
            # print(product_name)
            if product_name == 'Blackberry':
                product.find_element(By.XPATH, "div/button").click()
        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        # wait=WebDriverWait(driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@class='btn btn-success']")))
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.XPATH,
                            "//input[@class='validate filter-input form-control ng-untouched ng-pristine ng-valid']").send_keys(
            "Ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        # countries=driver.find_elements(By.XPATH, "//div[@class='suggestions']")
        # for country in countries:
        #    if country.text=='India':
        #        country.click()
        #       break
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
        success_msg = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        assert "Success" in success_msg
        print(success_msg)
        time.sleep(5)
