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



class BasePage(object):
    url = None

    driver = webdriver.Chrome(executable_path='/home/balous/PycharmProjects/test_selenium/chromedriver')

    def __init__(self):
        #self.driver = driver
        self.driver.maximize_window()
        #self.driver.set_page_load_timeout(60)
        self.WebDriverWait = WebDriverWait
        self.action = ActionChains(self.driver)

    def find_by_name(self, name):
        return self.WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.NAME, name))
        )
    def find_by_id(self, id):
        return self.WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.ID, id))
        )

    def find_by_css(self, css_selector):
        return self.WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

    def find_by_xpath(self, xpath):
        return self.WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def find_all_by_xpath(self, xpath):
        return self.WebDriverWait(self.driver, 50).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )



    # def move_to_element(self,element):
    #     self.action.move_to_element(element).click().perform()


    def navigate(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title
