from homework25.pages.base_page import BasePage


class Login(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        # inputs
        self.username_input = page.locator('[id="user-name"]')
        self.password_input = page.locator('[id="password"]')

        # buttons
        self.login_button = page.locator('[name="login-button"]')

        # messages
        self.error_message = page.locator('[class="error-message-container error"]')
