from homework25.pages.base_page import BasePage


class Bucket(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.checkout_button = page.locator('[id="checkout"]')

    def bucket_products_validate(self, product_name: str):
        return self.page.locator(
            '.inventory_item_name',
            has_text=product_name
        )

    def bucket_products_deletion(self, product_name: str):
        product = self.page.locator(
            '.cart_item',
            has_text=product_name
        )
        product.locator('[data-test^="remove"]').click()
