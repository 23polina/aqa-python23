import pytest
from playwright.sync_api import sync_playwright
from homework25.pages.login_page import Login
from homework25.pages.swaglabs_page import SwagLabs
from homework25.pages.bucket_page import Bucket
from homework25.pages.checkout_page import Checkout
from homework27.endpoints import ApiClient


@pytest.fixture(name="page")
def fixture_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        browser_page = context.new_page()
        yield browser_page
        browser.close()


@pytest.fixture(name="login")
def fixture_login(page):
    return Login(page)


@pytest.fixture(name="swaglabs")
def fixture_swaglabs(page):
    return SwagLabs(page)


@pytest.fixture(name="bucket")
def fixture_bucket(page):
    return Bucket(page)


@pytest.fixture(name="checkout")
def fixture_checkout(page):
    return Checkout(page)


@pytest.fixture(name="api_client")
def fixture_api_client():
    client = ApiClient("https://restful-booker.herokuapp.com")
    return client


@pytest.fixture(name="auth")
def fixture_auth(api_client):
    body = {
        "username": "admin",
        "password": "password123"
    }
    response = api_client.post_request("/auth", body=body)
    return response.json()["token"]


@pytest.fixture(name="request_body")
def fixture_request_body():
    body = {
        "firstname": "Test",
        "lastname": "Brown",
        "totalprice": 11204,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "Breakfast"
    }
    return body
