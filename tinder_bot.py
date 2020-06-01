from selenium import webdriver
from time import sleep
from login_info import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    # Select "Login with Facebook" and Interact
    def login(self):
        self.driver.get('https://tinder.com')
        sleep(3)

        more_option_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button')
        more_option_button.click()
        fb_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[3]/button')
        fb_button.click()

        # assign a base_window (chrome)
        # switch to popup window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        # input credentials
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_button = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_button.click()

    def funcname(self, parameter_list):
        pass
