import re

temp = open("3.txt",'r').read().splitlines()
x=list(temp)
s="".join(x)


print("".join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',s)))
