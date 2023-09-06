
import re
n = input("enter email id")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail.com", n)
if m!= None:
  print("valid gmail")
else :
  print("invalid gmail")
