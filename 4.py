import re
import urllib.request

num='822'

count = 0
while count < 400:
    myUrl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + num
    source = str(urllib.request.urlopen(myUrl).read())
    print(source)
    num= ''.join((re.findall('[0-9]+',source)))
    print(num)
    count+=1
