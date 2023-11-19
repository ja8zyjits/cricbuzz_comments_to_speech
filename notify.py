from bs4 import BeautifulSoup
import requests
import os
import time
from collections import deque


already_called = deque([0]*10, maxlen=50)


def check_wicket():
    res = requests.get("https://www.cricbuzz.com/live-cricket-scores/75651/ind-vs-aus-final-icc-cricket-world-cup-2023")
    soup = BeautifulSoup(res.text, features="html.parser")
    soup.find_all("p", class_="cb-com-ln")
    for each in soup.find_all("p", class_="cb-com-ln")[::-1]:
        if len(list(each.children)) > 1:
            shout_out(each.text)


def shout_out(text):
    global already_called
    if text not in already_called:
        os.system(f'say "{text}"')
        already_called.appendleft(text)
        time.sleep(2)

if __name__ == "__main__":
    while True:
        check_wicket()
        time.sleep(15)
