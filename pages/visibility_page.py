from playwright.sync_api import Page


class VisibilityPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.hide_button = page.locator("button#hideButton")
        self.removed_button = page.locator("button#removedButton")
        self.zero_width_button = page.locator("button#zeroWidthButton")
        self.overlapped_button = page.locator("button#overlappedButton")
        self.opacity_zero_button = page.locator("button#transparentButton")
        self.visibility_hidden_button = page.locator("button#invisibleButton")
        self.display_none_button = page.locator("button#notdisplayedButton")
        self.offscreen_button = page.locator("button#offscreenButton")

    def navigate(self) -> None:
        self.page.goto("/visibility")
