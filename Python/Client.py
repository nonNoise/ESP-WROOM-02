import struct
import requests
import datetime
import time


if __name__ == "__main__":
    d = datetime.datetime.today()
    url = "https://ja.wikipedia.org/wiki/Hello_world"
    r = requests.get(url)
    print r.text
    

