from selenium import webdriver
from base.basepage import BasePage
from page_objects.home_page import HomePage

#Locators
_email_login_field = '//input[@name="email"]'
_password_login_field = "//input[@name='passwd']"
_login_button = '//button[@id="SubmitLogin"]'
_bad_credentials_error_alert = '//div[@class="alert alert-danger"]/p'
_go_to_login_with_fb = '//div[@class="fblogin-link fblogin toLeft _marginLeft"]//span[contains(text(),"Zaloguj się z Facebook")]'


#driver = webdriver.Chrome(executable_path='/home/balous/PycharmProjects/test_selenium/chromedriver')

class LoginPage(BasePage):
    url = 'https://sklep.kfd.pl/logowanie'


    def send_keys_to_email_field(self,email):
        email_field = self.find_all_by_xpath(_email_login_field)[1]
        email_field.clear()
        email_field.send_keys(email)
    #
    def send_keys_to_password_field(self,password):
        passw = self.find_all_by_xpath(_password_login_field)[1]
        passw.clear()
        passw.send_keys(password)
    #
    def click_login_button(self):
        self.find_all_by_xpath(_login_button)[1].click()

    def go_to_login_with_fb(self):
        self.find_all_by_xpath(_go_to_login_with_fb)[1].click()


    def bad_credentials_error_alert(self):
        alert = self.find_by_xpath(_bad_credentials_error_alert)
        return alert



