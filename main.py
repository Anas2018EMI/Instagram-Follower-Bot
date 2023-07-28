from selenium import webdriver
from selenium. webdriver. chrome. options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "/home/msi/Ma formation/100 Days of Code - The Complete Python Pro Bootcamp for 2021/C) Intermediate +/Course/Web Scraping & Automation/7) Selenium Webdriver Browser and Game Playing Bot/Chrome Driver 115/chromedriver-linux64/chromedriver"
brave_browser_path = '/usr/bin/brave-browser'


INSTAGRAM_LOGIN_PAGE = "https://www.instagram.com/"
TARGET_ACCOUNT = "Type here the followers target account"

EMAIL = "Type here your email"
PASSWORD = "Type here your password"


class InstaFollower:
    def __init__(self) -> None:
        chrome_service = Service(executable_path=chrome_driver_path)
        chrome_options = Options()
        chrome_options.binary_location = brave_browser_path
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(
            service=chrome_service, options=chrome_options)

    def login(self):
        self.driver.get(INSTAGRAM_LOGIN_PAGE)
        time.sleep(3)
        email_input = self.driver.find_element(
            By.CSS_SELECTOR, 'input[aria-label="Phone number, username, or email"]')
        email_input.send_keys(EMAIL)
        time.sleep(1)

        password_input = self.driver.find_element(
            By.CSS_SELECTOR, 'input[aria-label="Password"]')
        password_input.send_keys(PASSWORD)
        time.sleep(2)

        login_btn = self.driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]')
        login_btn.click()
        time.sleep(4)

    def find_followers(self) -> list:
        self.driver.get(TARGET_ACCOUNT)
        time.sleep(3)

        followers_btn = self.driver.find_element(
            By.CSS_SELECTOR, 'a[href="/casacapmaroc.ma/followers/"]')
        followers_btn.click()
        time.sleep(2)

        i = 0
        while (i < 10):
            # as the website is dyanamic so updating the follwers list and also the webelement
            followers_group = self.driver.find_element(By.CSS_SELECTOR,
                                                       'div._aano')
            followers = followers_group.find_elements(By.CSS_SELECTOR,
                                                      'div.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3')
            # 'div._aano div[class="_ab8w  _ab94 _ab97 _ab9f _ab9k _ab9p  _ab9- _aba8 _abcm"]'
            # executing scroll into view script to view the element and thats gonna load the next element(follower ) ..ultimately your scrolling achived
            # self.driver.execute_script(
            #     "arguments[0].scrollIntoView(true);", followers[i])
            # print(followers)
            scroll_down = ActionChains(
                self.driver).scroll_to_element(followers[len(followers)-1])
            scroll_down.perform()

            time.sleep(2)
            print(i)
            i = i+1

        print("Number of targeted followers is {}".format(len(followers)))
        return followers

    def follow(self, followers):
        for follower in followers:

            try:
                follow_btn = follower.find_element(
                    By.CSS_SELECTOR, 'button[class="_acan _acap _acas _aj1-"]')
                follow_btn.click()
                time.sleep(2)
            except:
                # I prefer skiping the iteration than the commented code
                continue
                # follow_btn = follower.find_element(
                #     By.CSS_SELECTOR, 'button[class="_acan _aiit _acap _aijb _acat _aj1-"]')
                # follow_btn.click()
                # time.sleep(2)
                # cancel_btn = self.driver.find_element(
                #     By.CSS_SELECTOR, 'button[class="_a9-- _a9_1"]')
                # cancel_btn.click()
                # time.sleep(2)


#############################################################################
bot = InstaFollower()


bot.login()
followers = bot.find_followers()
bot.follow(followers)
