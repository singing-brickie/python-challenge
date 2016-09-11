temp = open("2.txt",'r').read().splitlines()
x=list(temp)
s=list("".join(x))
str=''
for j in range(0,len(s)):
   y =s[j]
   s[j]=''
   if y not in s:
       str+=y
   s[j]=y



print(str)
