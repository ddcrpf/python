
import re
n = input("enter number ")
m = re.fullmatch("[7-9]\d{9}",n)
if m!= None:
  print("valid mob no")
else :
  print("in valid mob no")""")
