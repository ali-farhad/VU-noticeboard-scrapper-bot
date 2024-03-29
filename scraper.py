# coded by alifahad
# scrapes  last msg from vu noticeboard and alerts in vu chat space

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
message = items[0].find(class_="newstext").text
if message != previous_message:
    print(message)
    payload = {
        'text': "<users/all> : NoticeBoard Alert",
        # 'text': "<users/>",

                'cards': [
                    {
                        'header': {
                            'title': '⚠️NoticeBoard Alert⚠️',
                            # 'title': '❌Under Maintenance ❌'

                        },
                        'sections': [
                            {
                                'widgets': [
                                    {
                                        'textParagraph': {
                                            'text':  message + '<br><a href=\"https://vulms.vu.edu.pk/NoticeBoard/NoticeBoard2.aspx\">Link</a>'
                                            # 'text': ''

                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
    }
    response = requests.post(WEBHOOK_URL, json=payload)
    response.raise_for_status()

    # Save the current message as the previous message
    with open('previous_message.txt', 'w') as f:
        f.write(message)
