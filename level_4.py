import re
import requests

response = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
context = response.content # This context is byte type
context = str(context).replace(r'\n','') # Converting to str type and remove all \n
print(context)

 regex patterns
result_pattern = re.compile(r"\w")

main_string = string_pattern.findall(context)[0]
result = result_pattern.findall(main_string)
print(''.join(result))


