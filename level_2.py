import re
import requests

response = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
context = response.content # This context is byte type
context = str(context).replace(r'\n','') # Converting to str type and remove all \n
context = context.replace(r'_','')

# regex patterns
string_pattern = re.compile(r"below:(.*)-->")
result_pattern = re.compile(r"\w")

main_string = string_pattern.findall(context)[0]
result = result_pattern.findall(main_string)
print(''.join(result))


