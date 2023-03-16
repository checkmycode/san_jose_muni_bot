from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium_project.constants as const
from bs4 import BeautifulSoup
import requests
import time
import os


class Parser(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Parser, self).__init__()
        self.implicitly_wait(15)
        self.new_links = []
        self.new_times = []

    def login_link(self):
        self.get('https://sanjosemuni.quick18.com/Account/LogOn?ReturnUrl=%2faccount')
        self.find_element(By.ID, "EmailAddress").send_keys(const.USER_NAME)
        self.find_element(By.ID, "Password").send_keys(const.PASSWORD)
        time.sleep(1)
        self.find_element(
            By.XPATH, '//*[@id="be_content_account"]/div[2]/div/div[8]/div[1]/button'
        ).click()

    def goto_tee_time_page(self):
        self.get(const.FULL_URL)

    def get_info(self):
        # Start bs4 to begin parsing website
        response = requests.get(const.FULL_URL)
        website_html = response.text

        soup = BeautifulSoup(website_html, 'html.parser')

        # Find all available tee times
        tee_times = soup.find_all(name='td', class_='mtrxTeeTimes')
        times = [tee_time.getText().strip() for tee_time in tee_times]

        # Find all maximum players for available tee time
        player_availability = soup.find_all(name='td', class_='matrixPlayers')
        players = [player.getText() for player in player_availability]

        # Find all links to go to final sign up page
        muni = 'https://sanjosemuni.quick18.com'
        link_to_signup = soup.find_all(name='a', class_='sexybutton teebutton')
        links = [link.get("href") for link in link_to_signup]
        for char in links:
            if 'psid=736' in char or '?teedate' in char:
                links.remove(char)

        # Find all prices for available tee times
        prices = soup.find_all(class_='mtrxPrice')
        price = [price.getText() for price in prices]
        for char in price:
            if char == '$30.00':
                price.remove('$30.00')

        full_link = [muni + link for link in links]

        for index, row in enumerate(players):
            if row == '2 to 4 players':
                self.new_times.append(times[index])
                self.new_links.append(full_link[1:][index])

        return self.new_times, self.new_links

    # User input for time > Check if available > if not available, take nearest available time
    def check_for_availability(self):
        looper = True
        idx = const.tee_time_list.index(const.WANTED_TIME)
        while looper:
            if const.tee_time_list[idx] in self.new_times:
                print(const.tee_time_list[idx])
                print(self.new_links)
                print(self.new_times)
                href_idx = self.new_times.index(const.tee_time_list[idx])
                print(href_idx)
                final_url = self.new_links[href_idx]
                return final_url
            else:
                idx += 1

    # Final checkout page
    def land_final_page(self, final_url):
        self.get(final_url)

        if const.PLAYER_COUNT == 4:
            self.find_element(By.ID, 'Players2_label').click()
        elif const.PLAYER_COUNT == 3:
            self.find_element(By.ID, 'Players1_label').click()
        elif const.PLAYER_COUNT == 2:
            self.find_element(By.ID, 'Players0_label').click()

        self.find_element(By.XPATH, '//*[@id="be_detail_details"]/b/b/div[6]/button').click()
        time.sleep(1)
        self.find_element(By.XPATH, '//*[@id="submitButton"]').click()
