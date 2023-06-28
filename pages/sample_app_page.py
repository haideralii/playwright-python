from playwright.sync_api import Page

class SampleAppPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_field = page.locator('input[name="UserName"]')
        self.password_field = page.locator('input[name="Password"]')
        self.login_button = page.locator('#login')
        self.login_status_txt = page.locator('#loginstatus')

    def navigate(self) -> None:
        self.page.goto("/sampleapp")
        
    def enter_username(self, username) -> None:
        self.username_field.fill(username)

    def enter_password(self, password) -> None:
        self.password_field.fill(password)
        
    def click_login_button(self) -> None:
        self.login_button.click()       
