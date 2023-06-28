from playwright.sync_api import Page


class ClassAttributePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.primary_button = page.locator("button.btn-primary")

    def navigate(self) -> None:
        self.page.goto("/classattr")
