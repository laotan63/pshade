# 替换交互
info = '''
---------- info of {name} -----------
name:{name}
age:{age}
job:(job)
'''.format(name=name,age=age,job=job)
info1 = '''name1:%s
age:%s
job:%s
'''%(name,age,job)
print(info)

# 2的10次方
type(2**10)

import copy
person=['name',['saving',100]]
p1=copy.copy(person)
p2=person[:]
p3=list(person)


import getpass
# 密文
password = getpass.getpass(password)

#while循环
guess_of_age = 56
count = 0
while count <3:
    guess_age = int(input('age:'))
    if guess_age == guess_of_age:
        print('you got it!')
        break
    elif guess_age > guess_of_age:
        print('think smaller!')
    else:

        print('think lager!')
    count+=1
else:
    print('you have tried too many times..fuck off!')    
    \033[31;1m%s\033[0m'  #换颜色31红色 32绿色 33黄色