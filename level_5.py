import re
import urllib.request


params_pattern = re.compile(r"the next nothing is\s*(\d+)")
devide_pattern = re.compile(r"Divide by (\w+)\s")
param = 12345
counter = 0

while counter < 400:
    response = urllib.request.urlopen(f"http://www.pythonchallenge.com/pc/def/linkedlist.php/?nothing={param}")
    result = str(response.read())
    print(result)
    devid = devide_pattern.findall(result)
    if devid:
        param = param/2
        continue
    param = int(params_pattern.findall(result)[0])
    counter += 1
    print(counter)
