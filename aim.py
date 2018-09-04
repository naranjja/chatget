from selenium import webdriver

if __name__ == '__main__':
    print("Opening Chromedriver...")
    chrome_options = webdriver.ChromeOptions()
    prefs = { "profile.default_content_setting_values.notifications" : 2 }
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    executor_url = driver.command_executor._url
    session_id = driver.session_id 
    print("Please visit the Facebook Page Inbox that you want to download.")
    print("Command Executor URL: ", executor_url)
    print("Session ID: ", session_id)