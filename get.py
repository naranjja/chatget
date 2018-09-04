from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as remote_webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

import csv
import re


def attach_to_session(executor_url, session_id):
    original_execute = remote_webdriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            return { "success": 0, "value": None, "sessionId": session_id }
        return original_execute(self, command, params)
    remote_webdriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    remote_webdriver.execute = original_execute
    return driver


if __name__ == '__main__':

    print("Please enter the information for an existing web driver connection positioned over a Facebook Page Inbox.")
    executor_url = input("Command Executor URL: ")
    session_id = input("Session ID: ")

    while True:
        print("\nPlease scroll up and down to load the entire conversation.")
        user_said = input("To download conversation say 'get', to exit say 'bye': ")

        if (user_said.lower() == "get"):
            driver = attach_to_session(executor_url, session_id)
            conversation = driver.find_element_by_xpath("//div[@class='uiScrollableAreaContent']").text

            with open("conversations/{}.txt".format(time()), "w", encoding="utf8") as f:
                f.write(conversation)
                f.close()

            print("Conversation saved!")

        if (user_said.lower() == "bye"):
            print("Bye!")
            raise SystemExit