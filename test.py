# coded by alifahad
# scrapes vu noticeboard and alerts in vu chat space

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Set up the webhook URL
WEBHOOK_URL = 'https://chat.googleapis.com/v1/spaces/AAAAnyLsD1Y/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=dGZK00EMyrlMj0n3ms_oeYrQkvBpyvxHPk1nHMGrRic'

# Scrape the HTML page
# while True:
url = "https://vulms.vu.edu.pk/NoticeBoard/NoticeBoard2.aspx"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get the previous message
with open('previous_message.txt', 'r') as f:
    previous_message = f.read().strip("")
    # print(previous_message)

# Find the relevant items
items = soup.find_all(class_="m-timeline-3__item m-timeline-3__item--info")

for item in items:
    date_str = item.find(class_="m-timeline-3__item-link").text
    date = datetime.strptime(date_str, '%B %d, %Y').strftime('%Y-%m-%d')

    if date >= datetime.now().strftime('%Y-%m-%d'):
        message = item.find(class_="m-timeline-3__item-text")
        if (len(message) > 1):
            print(message[-1].text)
        else:
            if message != previous_message:
                print(message)

         # Save the current message as the previous message
            with open('previous_message.txt', 'w') as f:
                f.write(message)

    # time.sleep(60)
