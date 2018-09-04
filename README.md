# 👇 chatget

A simple Python3 Selenium script that downloads conversations from Facebook Page Inbox.
It hooks after normal login and usage *to avoid Facebook blocks*.

## Installation
1. Install requirements with `pip install -r requirements.txt`
2. Download [Chromedriver](http://chromedriver.chromium.org/downloads) and add it to PATH.

## Usage
1. Run `aim.py` and go to a Facebook Page Inbox conversation.
2. Copy the values of **Command Executor URL** and **Session ID**.
3. Run `get_conversations.py` and enter the copied values.
4. Scroll a conversation up and down to load it completely.
5. Enter `get` to parse conversation and save it to a timestamped file within the `conversations/` folder.

## Planned features
- Modifiable User Agent string
- Automatic scrolling
- Automatic download of all conversations in an inbox