from playwright.sync_api import expect
from homework25.test_data.test_data import CorrectUser, InCorrectUser, ErrorMessage


def test_user_can_logic_successfully(login, swaglabs):
    login.goto("https://www.saucedemo.com/")
    login.username_input.fill(CorrectUser.USERNAME)
    login.password_input.fill(CorrectUser.PASSWORD)
    login.login_button.click()
    expect(swaglabs.title).to_have_text("Products")


def test_user_cannot_logic(login):
    login.goto("https://www.saucedemo.com/")
    login.username_input.fill(InCorrectUser.USERNAME)
    login.password_input.fill(InCorrectUser.PASSWORD)
    login.login_button.click()
    expect(login.error_message).to_have_text(ErrorMessage.INCORRECT_LOGIN)


def test_user_adds_items_into_bucket(login, swaglabs, bucket):
    login.goto("https://www.saucedemo.com/")
    login.username_input.fill(CorrectUser.USERNAME)
    login.password_input.fill(CorrectUser.PASSWORD)
    login.login_button.click()
    swaglabs.add_products_to_card("Sauce Labs Backpack")
    swaglabs.add_products_to_card("Sauce Labs Bike Light")
    swaglabs.bucket.click()
    expect(bucket.bucket_products_validate("Sauce Labs Backpack")).to_be_visible()
    expect(bucket.bucket_products_validate("Sauce Labs Bike Light")).to_be_visible()


def test_user_deletes_items_from_bucket(login, swaglabs, bucket):
    login.goto("https://www.saucedemo.com/")
    login.username_input.fill(CorrectUser.USERNAME)
    login.password_input.fill(CorrectUser.PASSWORD)
    login.login_button.click()
    swaglabs.add_products_to_card("Sauce Labs Backpack")
    swaglabs.add_products_to_card("Sauce Labs Bike Light")
    swaglabs.bucket.click()
    bucket.bucket_products_deletion("Sauce Labs Backpack")
    expect(bucket.bucket_products_validate("Sauce Labs Backpack")).not_to_be_visible()
    expect(bucket.bucket_products_validate("Sauce Labs Bike Light")).to_be_visible()


def test_user_cancels_checkout(login, swaglabs, bucket, checkout):
    login.goto("https://www.saucedemo.com/")
    login.username_input.fill(CorrectUser.USERNAME)
    login.password_input.fill(CorrectUser.PASSWORD)
    login.login_button.click()
    swaglabs.add_products_to_card("Sauce Labs Backpack")
    swaglabs.bucket.click()
    bucket.checkout_button.click()
    checkout.cancel_button.click()
    expect(bucket.bucket_products_validate("Sauce Labs Backpack")).to_be_visible()


def test_user_creates_order(login, swaglabs, bucket, checkout):
    login.goto("https://www.saucedemo.com/")
    login.username_input.fill(CorrectUser.USERNAME)
    login.password_input.fill(CorrectUser.PASSWORD)
    login.login_button.click()
    swaglabs.add_products_to_card("Sauce Labs Backpack")
    swaglabs.bucket.click()
    bucket.checkout_button.click()
    checkout.firstname_input.fill(CorrectUser.FIRSTNAME)
    checkout.lastname_input.fill(CorrectUser.LASTNAME)
    checkout.zipcode_input.fill(CorrectUser.ZIPCODE)
    checkout.continue_button.click()
    checkout.finish_button.click()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
