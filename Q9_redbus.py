
  
from urllib import request
import re
reader = request.urlopen("https://www.redbus.in/info/redcare")
text = reader.read()
regex = "[0-9-]{9}[0-9-]+"
numbers = re.findall(regex, str(text), re.I)
for no in numbers:
  print(no)
o/p - 
65-31582888
2023-09-05
24595215509
