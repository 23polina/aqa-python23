from homework25.pages.base_page import BasePage


class SwagLabs(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.title = page.locator('[class="title"]')
        self.bucket = page.locator('[class="shopping_cart_link"]')

    def add_products_to_card(self, product_name: str):
        product = self.page.locator(
            '.inventory_item',
            has_text=product_name
        )
        product.locator('[data-test^="add-to-cart"]').click()
