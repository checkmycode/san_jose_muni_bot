from selenium_project.html_scraper import Parser
import time


def main():
    with Parser() as bot:
        bot.login_link()
        bot.goto_tee_time_page()
        bot.get_info()
        bot.check_for_availability(bot.get_info())
        bot.land_final_page(bot.check_for_availability(bot.get_info()))
        time.sleep(30)


if __name__ == '__main__':
    main()
