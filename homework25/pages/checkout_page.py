from homework25.pages.base_page import BasePage


class Checkout(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        # inputs
        self.firstname_input = page.locator('[id="first-name"]')
        self.lastname_input = page.locator('[id="last-name"]')
        self.zipcode_input = page.locator('[id="postal-code"]')

        # buttons
        self.cancel_button = page.locator('[id="cancel"]')
        self.continue_button = page.locator('[id="continue"]')
        self.finish_button = page.locator('[id="finish"]')

        # headers
        self.complete_header = page.locator('[data-test="complete-header"]')
