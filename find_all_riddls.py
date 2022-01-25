import os
import requests

URL = 'http://www.pythonchallenge.com/pc/def/'

def infinite_sequence():
    num = int()
    if not os.path.exists('index.txt'):
        with open('index.txt', 'w') as f:
            f.write('1')

    with open('index.txt', 'r') as f:
        #print(f.read(), 'hereee',f.readlines())
        num = f.read()
    num = int(num)
    with open('index.txt', 'w') as f:
        while True:
            yield num
            num += 1
            f.seek(0)
            f.write(str(num))
            f.truncate()

for number in infinite_sequence():
    #print('number :',number)
    res = requests.get(f"{URL}{number}.html")
    if res.status_code != 404:
        print(res.status_code)
        print(f"{URL}{number}.html")

