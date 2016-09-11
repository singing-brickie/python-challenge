import pickle, urllib.request

handle = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(handle)
handle.close()


for line in data:
    str=''
    for x in line:
        str+=x[0]*x[1]
    print(str)
