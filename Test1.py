import time
import unittest

import selenium
from selenium import webdriver


class LoginTests(unittest.TestCase):
    def setUp(self):
        self.url = "https://courses.ultimateqa.com/users/sign_in"
        self.driver = selenium.webdriver.Firefox(executable_path='D:\LoginTests\Drivers\geckodriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_empty_login_pass(self):
        driver = self.driver
        driver.get(self.url)
        button_login = driver.find_element_by_id('btn-signin')
        button_login.click()
        driver.implicitly_wait(10)
        user_message = driver.find_element_by_xpath("//*[@class='message-text']")
        assert user_message.text == "Invalid Email or password."

    def test_empty_password(self):
        driver = self.driver
        driver.get(self.url)
        login_field = driver.find_element_by_id('user_email')
        login_field.send_keys("evgeniya.tyutyunik@gmail.com")
        button_login = driver.find_element_by_id('btn-signin')
        button_login.click()
        driver.implicitly_wait(10)
        user_message = driver.find_element_by_xpath("//*[@class='message-text']")
        assert user_message.text == "Invalid Email or password."

    def test_invalid_login(self):
        driver = self.driver
        driver.get(self.url)
        login_field = driver.find_element_by_id('user_email')
        login_field.send_keys("email@test")
        password_field = driver.find_element_by_id('user_password')
        password_field.send_keys("passwordtest")
        button_login = driver.find_element_by_id('btn-signin')
        button_login.click()
        driver.implicitly_wait(10)
        user_message = driver.find_element_by_xpath("//*[@class='message-text']")
        assert user_message.text == "Invalid Email or password."

    def test_secured_password(self):
        driver = self.driver
        driver.get(self.url)
        password_field = driver.find_element_by_id('user_password')
        assert password_field.get_attribute('type') == 'password'

    def test_valid_login(self):
        driver = self.driver
        driver.get(self.url)
        login_field = driver.find_element_by_id('user_email')
        login_field.send_keys("evgeniya.tyutyunik@gmail.com")
        password_field = driver.find_element_by_id('user_password')
        password_field.send_keys("2870750")
        button_login = driver.find_element_by_id('btn-signin')
        button_login.click()
        driver.implicitly_wait(10)
        user_logged = driver.find_element_by_xpath("//span[@class='user-name']")
        success_mail = driver.find_element_by_xpath("//*[@class='message-text']")
        assert user_logged.text == "Evgeniya T"
        assert success_mail.text == "Signed in successfully."

    def test_sign_out(self):
        driver = self.driver
        driver.get(self.url)
        login_field = driver.find_element_by_id('user_email')
        login_field.send_keys("evgeniya.tyutyunik@gmail.com")
        password_field = driver.find_element_by_id('user_password')
        password_field.send_keys("2870750")
        button_login = driver.find_element_by_id('btn-signin')
        button_login.click()
        driver.implicitly_wait(10)
        user_menu = driver.find_element_by_xpath("//a[@id='my_account']")
        time.sleep(10)
        user_menu.click()
        button_sign_out = driver.find_element_by_xpath("//*[@href='/users/sign_out']")
        button_sign_out.click()
        driver.implicitly_wait(10)
        user_sign_out = driver.find_element_by_xpath("//*[@href='/users/sign_in']")
        assert user_sign_out.text == "Sign In"

    def test_double_login(self):
        driver = self.driver
        driver.get(self.url)
        login_field = driver.find_element_by_id('user_email')
        login_field.send_keys("evgeniya.tyutyunik@gmail.com")
        password_field = driver.find_element_by_id('user_password')
        password_field.send_keys("2870750")
        button_login = driver.find_element_by_id('btn-signin')
        button_login.click()
        time.sleep(10)
        driver.get(self.url)
        driver.implicitly_wait(10)
        user_message = driver.find_element_by_xpath("//*[@class='message-text']")
        assert user_message.text == "You are already signed in."

    def test_linkedIn_login(self):
        driver = self.driver
        driver.get(self.url)
        button_linked_in = driver.find_element_by_xpath("//a[@class='btn linkedin-signin linkedin']")
        button_linked_in.click()
        driver.implicitly_wait(10)
        linked_in_logo = driver.find_element_by_xpath("//h2[@class='in__logo']")
        linked_in_username = driver.find_element_by_xpath("//input[@id='username']")
        assert linked_in_logo.get_attribute('innerText') == "LinkedIn"
        assert linked_in_username.get_attribute('name') == "session_key"

    def tearDown(self):
        self.driver.quit()
