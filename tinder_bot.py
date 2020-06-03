from selenium import webdriver
from time import sleep
from login_info import username, password
import random

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    # Select "Login with Facebook" and Interact
    def login(self):
        self.driver.get('https://tinder.com')
        sleep(3)

        more_option_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        more_option_button.click()
        sleep(1)

        fb_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
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

        self.driver.switch_to_window(base_window)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            #coin flip
            flip_coin = bool(random.getrandbits(1))
            if flip_coin:
                # make it 25% chance to swipe right
                flip_coin = bool(random.getrandbits(1))
                if flip_coin:
                    try:
                        self.like()
                    except Exception:
                        try:
                            self.close_popup()
                        except Exception:
                            self.close_match()
                else:
                    try:
                        self.dislike()
                    except Exception:
                        try:
                            self.close_popup()
                        except Exception:
                            self.close_match()
            else:
                try:
                    self.dislike()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
sleep(3)
bot.auto_swipe()
