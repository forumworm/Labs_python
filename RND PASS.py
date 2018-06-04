import random
#короткий вариант: psw=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)]))
str1 = '0123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()
str4 = str1+str2+str3
ls = list(str4)
random.shuffle(ls)
psw = ''.join([random.choice(ls) for x in range(12)])
file = open("file.txt", "w")
file.write(psw)
file.close()
#print(psw)


