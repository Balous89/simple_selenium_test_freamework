from base.basepage import BasePage
from page_objects.home_page import HomePage
import time





#Locators
_top_bar_menu = '//div[@class="login_box_r"]'
_user_profile = '//div[@class="login_box_r"]//a[@class="account"]'
_logout = '//div[@class="login_box_r"]//a[@class="logout"]'


#driver = webdriver.Chrome(executable_path='/home/balous/PycharmProjects/test_selenium/chromedriver')

class HomePageAfterLogin(BasePage):
    url = None

    def top_bar_menu(self):
        time.sleep(1)
        menu = self.find_by_xpath(_top_bar_menu)
        print(menu.text)
        return menu

    def go_to_user_profile(self):
        profile_button = self.find_by_xpath(_user_profile)
        print(profile_button.text)
        profile_button.click()

    def logout_user(self):
        logout_button = self.find_by_xpath(_logout)
        logout_button.click()


home = HomePage()
home.navigate()
home.go_to_login_with_fb()
home.login_with_facebook('balut89@gmail.com','9663645620')

afterlogin=HomePageAfterLogin()

afterlogin.go_to_user_profile()
afterlogin.logout_user()

