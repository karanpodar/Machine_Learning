import io
import logging
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

debugging = False

log_stream = io.StringIO()
log_format = "%(message)s"

logging.basicConfig(stream=log_stream, level=logging.INFO, format=log_format)

load_dotenv()

LOGIN_PAGE = os.getenv("LOGIN_PAGE")
ACCOUNT_NUMBER = os.getenv("ACCOUNT_NUMBER")
LAST_NAME = os.getenv("LAST_NAME")
CARD_NUM = os.getenv("CARD_NUM")
CARD_MONTH = os.getenv("CARD_MONTH")
CARD_YEAR = os.getenv("CARD_YEAR")
CARD_CVV = os.getenv("CARD_CVV")
PHONE_NUMBER = os.getenv("PHONE_NUM")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# This gets the parent folder of the current project file
script_directory = Path(__file__).resolve().parent

# This joins parent folder to the chromediver path
driver_path = script_directory.joinpath("chromedriver-win64", "chromedriver")

chrome_options = Options()
if debugging:
    chrome_options.add_experimental_option("detach", True)
else:
    chrome_options.add_argument("--headless")


def set_field_to_password(driver, element_id):
    driver.execute_script(f"document.getElementById('{element_id}').type = 'password'")


def wait_for_element(driver, by, element_identifier, timeout=5):
    try:
        element_present = EC.presence_of_element_located((by, element_identifier))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        logging.info(f"Timed out wating for {element_identifier}")
        return None
    return driver.find_element(by, element_identifier)


def login_to_account(driver):
    driver.get(LOGIN_PAGE)

    account_input = wait_for_element(driver, By.ID, "Account")
    name_input = wait_for_element(driver, By.ID, "Name")

    if account_input and name_input:
        set_field_to_password(driver, "Account")
        set_field_to_password(driver, "Name")
        account_input.send_keys(ACCOUNT_NUMBER)
        name_input.send_keys(LAST_NAME)

    submit_button = wait_for_element(
        driver, By.XPATH, '//input[@type="submit"][@name="Submit"]'
    )

    if submit_button:
        submit_button.click()


def submit_payment(driver):
    num_input = wait_for_element(driver, By.ID, "cardnumber")
    month_input = wait_for_element(driver, By.ID, "month")
    year_input = wait_for_element(driver, By.ID, "year")
    cvv_input = wait_for_element(driver, By.ID, "cvv")
    payment_amt = wait_for_element(driver, By.ID, "payment")
    confirm_checkbox = wait_for_element(driver, By.ID, "confirm")
    submit_button = wait_for_element(driver, By.ID, "submitbtn")

    if payment_amt:
        payment_amt_str = payment_amt.get_attribute("value")
        logging.info(f"Payment Amount: {payment_amt_str}")
        try:
            payment_amount = float(payment_amt_str)
            if payment_amount <= 0.00:
                logging.info("No Payment Due.")
                return False
            elif payment_amount > 300.00:
                logging.info("Payment Amount High. Check Manually.")
                return False
        except ValueError:
            logging.info("Invalid Payment Amount.")
            return False

    if (
        num_input
        and month_input
        and year_input
        and cvv_input
        and confirm_checkbox
        and submit_button
    ):
        num_input.send_keys(CARD_NUM)
        month_input.send_keys(CARD_MONTH)
        year_input.send_keys(CARD_YEAR)
        cvv_input.send_keys(CARD_CVV)

        confirm_checkbox.click()
        submit_button.click()

    try:
        WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//body"), "Thank you for your payment"
            )
        )
        return True
    except TimeoutException:
        return False


def send_message(subject, receiver):
    sender = "YourEmail@gmail.com"

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(log_stream.getvalue())

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, APP_PASSWORD)
        smtp.send_message(msg)


def main():
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        login_to_account(driver)
        payment_success = submit_payment(driver)
        if payment_success:
            message = "Successful Payment."
            logging.info(message)
            send_message(message, "YourEmail@gmail.com")
            send_message(message, f"{PHONE_NUMBER}@mms.att.net")
        else:
            message = "Failed Payment."
            logging.info(message)
            send_message(message, "YourEmail@gmail.com")
            send_message(message, f"{PHONE_NUMBER}@mms.att.net")
    except WebDriverException as e:
        logging.info(f"General WebDriver error: {e}")
        send_message("Failed to run script", "YourEmail@gmail.com")
        send_message("Failed to run script", f"{PHONE_NUMBER}@mms.att.net")
    finally:
        if debugging:
            print(log_stream.getvalue())
        else:
            driver.quit()


if __name__ == "__main__":
    main()