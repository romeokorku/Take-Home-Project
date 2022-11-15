import time
from behave import *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@given('Launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@when('Open the patient management app homepage')
def step_impl(context):
    context.driver.get("http://localhost:3000/")


@when('enter first name')
def step_impl(context):
    context.driver.find_element(By.NAME, "firstName").send_keys("Romeo")


@when('enter middle name')
def step_impl(context):
    context.driver.find_element(By.NAME, "middleName").send_keys("Korku")


@when('enters last name')
def step_impl(context):
    context.driver.find_element(By.NAME, "lastName").send_keys("Avemegah")

@when('enters phone number')
def step_impl(context):
    context.driver.find_element(By.NAME, "phoneNumber").send_keys("0242344621")


@when('enters date of birth')
def step_impl(context):
    context.driver.find_element(By.NAME, "dob").send_keys("03-24-1993")


@when('enters address')
def step_impl(context):
    context.driver.find_element(By.NAME, "address").send_keys("Dansoman")


@when('clicks on the Add New User button')
def step_impl(context):
    add_new_user = context.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/a")
    add_new_user.click()


@then('Patient card is created')
def step_impl(context):
    user_List = context.driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/main/div[1]")
    status = user_List.is_displayed()
    assert status is True


@then('close browser')
def step_impl(context):
    context.driver.close()
