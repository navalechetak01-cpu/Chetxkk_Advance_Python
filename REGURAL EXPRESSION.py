import re

text = "i have 100 apples, 20 bananas and 30 oranges."

result = re.findall(r"\d+",text)
print (result)
