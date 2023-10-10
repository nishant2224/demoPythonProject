from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import sys

@Given("User navigates to google")
def logIntoGoogle(self):
    self.driver = webdriver.Edge()
    self.driver.maximize_window()
    self.driver.implicitly_wait(15)
    self.driver.get("https://www.google.com/")

@When("I enter qa testing and search")
def enterSearchText(self):
    wait= WebDriverWait(self.driver,timeout=10)
    search = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//textarea[@aria-label='Search']")))
    search.click()
    search.send_keys("qa testing")
    search.send_keys(Keys.ENTER)

@Then("Display the required information")
def displayHeadingAndHyperlinks(self):
    wait = WebDriverWait(self.driver, timeout=10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@data-snc]//div[contains(@class,'notranslate')]/preceding-sibling::h3")))
    headings = self.driver.find_elements(By.XPATH,"//div[@data-snc]//div[contains(@class,'notranslate')]/preceding-sibling::h3")
    print("Headings :")
    for heading in headings:
        print(heading.text,end="\n")
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@data-snc]//div[contains(@class,'notranslate')]/preceding-sibling::h3/parent::a")))
    print("Links :")
    hyperlinks = self.driver.find_elements(By.XPATH,"//div[@data-snc]//div[contains(@class,'notranslate')]/preceding-sibling::h3/parent::a")
    print(len(hyperlinks))
    for hyperlink in hyperlinks:
        print(hyperlink.get_attribute("href"),end="\n")