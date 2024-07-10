#!/usr/bin/python3
"""Module for fetching data from url."""
import urllib.request


def fetch(url):
    """Method for fetching data from url."""
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print("Body response:")
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
            print(f"\t- utf8 content: {content.decode()}")
if __name__ == "__main__":
    fetch('https://alx-intranet.hbtn.io/status')
