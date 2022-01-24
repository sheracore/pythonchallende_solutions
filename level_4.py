import re
import requests

response = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
context = response.content # This context is byte type
context = str(context).replace(r'\n','') # Converting to str type and remove all \n
#print(context)

#regex patterns
#result_pattern = re.compile(r"([A-Z])\1\1([a-z])([A-Z])\1\1")
#result_pattern = re.compile(r"([A-Z])\1([a-z])([A-Z])\1")
#result_pattern = re.compile(r"([A-Z])\1\1([a-z])")
result_pattern = re.compile(r"[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]")
result = result_pattern.findall(context)
print("".join(result))
