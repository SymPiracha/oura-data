import requests
from dotenv import load_dotenv
import os
import json


load_dotenv()  # take environment variables from .env
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


def get_basic_info():
    x = requests.get(f'https://api.ouraring.com/v1/userinfo?access_token={ACCESS_TOKEN}')
    basic_info = json.loads(x.text)

def main():
    get_basic_info()

if __name__ == '__main__':
    main()