import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

use_step_matcher("re")


@given("User navigates to flipkart")
def step_user_navigates_to_flipkart(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)
    context.driver.get("https://www.flipkart.com/")

@when("User closes the login popup")
def step_user_closes_login_popup(context):
    wait = WebDriverWait(context.driver, timeout=10)
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Login']")))
    crossButton = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[@role='button']")))
    crossButton.click()
    time.sleep(2)


@when('I enter "(.*)" into search')
def step_user_enters_search_term(context, search_term):
    wait = WebDriverWait(context.driver, timeout=10)
    searchBox = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[contains(@title,'Search')]")))
    searchBox.click()
    searchBox.send_keys(search_term)
    searchBox.send_keys(Keys.ENTER)


@when('I select "(.*)" as "(.*)"')
def step_user_enters_search_term(context, accordian, option):
    wait = WebDriverWait(context.driver, timeout=10)
    accordLocator = "//div[text()='%s']" % accordian
    accordionLocator = (By.XPATH, accordLocator)
    time.sleep(1)
    wait.until(expected_conditions.element_to_be_clickable(accordionLocator)).click()
    optLocator = "//div[text()='%s']" % option
    optionLocator = (By.XPATH, optLocator)
    time.sleep(1)
    wait.until(expected_conditions.element_to_be_clickable(optionLocator)).click()


@then("Display the first gadget that appears")
def displayGadgets(context):
    wait = WebDriverWait(context.driver, timeout=10)
    gadgets = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "//span[text()='Filters']/ancestor::div/following-sibling::div//div[text()='Ultra HD (8K)']")))
    for gadget in gadgets:
        print(gadget.text)


@then('Verify the filter contains "(.*)"')
def displayGadgets(context, filter):
    wait = WebDriverWait(context.driver, timeout=10)
    Locator = "//span[text()='Filters']/ancestor::div/following-sibling::div//div[text()='%s']" % filter
    filterLocator = (By.XPATH, Locator)
    try:
        wait.until(expected_conditions.visibility_of_all_elements_located(filterLocator))
    except TimeoutException:
        error_text = "Filter is not displayed"
        assert False, error_text


def after_scenario(self):
    self.driver.quit()