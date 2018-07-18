from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import time
import random
from random import shuffle
from selenium.webdriver.common.action_chains import ActionChains
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select


# Locators
_go_to_login_page = '//div[@class="login_box_r"]/a'
_category_menu = '//li/a[@title="Kategorie"]'
_producents_menu = '//a[@title="Producenci"]'
_go_to_kfd_stores_list= '//a[@title= "Sklepy KFD"]'
_shipping_and_payment='//a[@title="Dostawa i płatność"]'
_search_box = '//input[@id = "search_query_top"]'
_go_to_login_with_fb = '//span[@class="bluefb"]'
_fb_email_field = '//input[@id="email"]'
_fb_password_field = '//input[@id="pass"]'
_fb_login_button = '//label[@id="loginbutton"]'


driver = webdriver.Chrome(executable_path='/home/balous/PycharmProjects/test_selenium/chromedriver')

_password_field = "user_password"
_login_button = "commit"

class HomePage(BasePage):
    url = "https://sklep.kfd.pl/"

    def go_to_login_page(self):
        go_to_login_button = self.find_by_xpath(_go_to_login_page).click()

    def drop_down_category(self,category_xpath_locator):
        drop_down_menu = self.find_by_xpath(_category_menu)
        self.action.move_to_element(drop_down_menu).perform()
        category = self.find_by_xpath(category_xpath_locator)
        self.action.move_to_element(category).click().perform()

    def drop_down_producents(self,producent_xpath_locator):
        drop_down_menu = self.find_by_xpath(_producents_menu)
        self.action.move_to_element(drop_down_menu).perform()
        producent = self.find_by_xpath(producent_xpath_locator)
        self.action.move_to_element(producent).click().perform()

    def kfd_stores(self):
        self.find_by_xpath(_go_to_kfd_stores_list).click()

    def shipping_and_payment(self):
        self.find_by_xpath(_shipping_and_payment).click()

    def send_keys_to_search_box(self,text_for_search):
        self.find_by_xpath(_search_box).send_keys(text_for_search).submit()

    def go_to_login_with_fb(self):
        self.find_by_xpath(_go_to_login_with_fb).click()

    def login_with_facebook(self,email ,password):
        self.driver.switch_to.window(driver.window_handles[-1])
        print(driver.title)

        email_field = self.find_by_xpath(_fb_email_field)
        password_field = self.find_by_xpath(_fb_password_field)
        login_button = self.find_by_xpath(_fb_login_button)
        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()
        try:
            confirm_button = self.find_by_xpath('//button[@name="__CONFIRM__"]')
            confirm_button.click()
        except:
            pass
        self.driver.switch_to.window(driver.window_handles[0])



















#switch to new window : driver.SwitchTo().Window(driver.WindowHandles.Last());?? driver.getWindowHandle();





a = HomePage(driver)
a.navigate()
a.go_to_login_with_fb()
a.login_with_facebook()
#a.filter_product_by_category()