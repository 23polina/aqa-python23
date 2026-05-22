from playwright.sync_api import expect


def test_user_can_login_with_correct_cred(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator('[name="login-button"]').click()
    expect(page.get_by_text("Products")).to_be_visible()


def test_user_can_add_items_into_bucket(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator('[name="login-button"]').click()
    page.locator('[id="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[class="shopping_cart_link"]').click()
    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")
    expect(page.locator('[data-test="inventory-item-name"]')).to_have_text("Sauce Labs Backpack")


def test_user_can_delete_items_from_bucket(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator('[name="login-button"]').click()
    page.locator('[id="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[class="shopping_cart_link"]').click()
    page.locator('[id="remove-sauce-labs-backpack"]').click()
    expect(page.locator('[data-test="cart-contents-container"]')).not_to_have_text(
        "Sauce Labs Backpack"
    )


def test_user_can_create_an_order_and_get_back(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.locator('[name="login-button"]').click()
    page.locator('[id="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    page.locator('[class="shopping_cart_link"]').click()
    page.locator('[class="btn btn_action btn_medium checkout_button "]').click()
    page.locator('[id="first-name"]').fill("test_first_name")
    page.locator('[id="last-name"]').fill("test_last_name")
    page.locator('[id="postal-code"]').fill("12344")
    page.locator('[class="submit-button btn btn_primary cart_button btn_action"]').click()
    page.locator('[id="finish"]').click()
    expect(page.get_by_text("Checkout: Complete!")).to_be_visible()
    expect(page.get_by_text("Thank you for your order!")).to_be_visible()
    page.locator('[id="back-to-products"]').click()
    expect(page.get_by_text("Products")).to_be_visible()


def test_user_cannot_login_with_incorrect_cred(page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("test111")
    page.get_by_placeholder("Password").fill("test11")
    page.locator('[name="login-button"]').click()
    expect(page.locator('[class="error-message-container error"]')).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )
