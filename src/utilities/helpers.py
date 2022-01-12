import random
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument("--start-maximized")  # open Browser in maximized mode
options.add_argument("--no-sandbox")  # bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


def simulate_human(start=0, limit=90):
    sleep(random.uniform(start, limit))


def wait_and_find_element(browser, xpath, wait=20, nowait=False):
    if nowait:
        return browser.find_element(By.XPATH, xpath)
    WebDriverWait(browser, wait).until(
        expected_conditions.presence_of_element_located((By.XPATH, xpath)))
    return browser.find_element(By.XPATH, xpath)


def wait_and_find_elements(browser, xpath, wait=20, nowait=False):
    if nowait:
        return browser.find_elements(By.XPATH, xpath)
    WebDriverWait(browser, wait).until(
        expected_conditions.presence_of_element_located((By.XPATH, xpath)))
    return browser.find_elements(By.XPATH, xpath)


def wait_and_find_elements_by_class(browser, class_selector, wait=20, nowait=False):
    if nowait:
        return browser.find_elements(By.CLASS_NAME, class_selector)
    WebDriverWait(browser, wait).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, class_selector)))
    return browser.find_elements(By.CLASS_NAME, class_selector)


def wait_and_find_elements_by_tag(browser, tag, wait=20, nowait=False):
    if nowait:
        return browser.find_elements(By.TAG_NAME, tag)
    WebDriverWait(browser, wait).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, tag)))
    return browser.find_elements(By.TAG_NAME, tag)


def fill_field(element, text, submit=False):
    element.clear()
    element.send_keys(text)
    simulate_human()
    if submit:
        element.send_keys(Keys.RETURN)