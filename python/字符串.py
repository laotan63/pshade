name = 'my \tname is pshade'
name1 = 'my name is {name1} and I am {year} old'
print(name.capitalize()) #首字母大写
print(name.count('a')) # 统计a的个数
print(name.center(50,'-')) #打印50个字符，把字符串放中间，不足的用-补上
print(name.encode()) #把字符串转成二进制
print(name.endswith('d')) #判断以什么字符结尾
print(name.expandtabs(tabsize=30)) #把tab键转换成多少个空格
print(name.find('name')) #查找name的字符个数
print(name[name.find('name'):]) #从name开始切片
print(name1.format(name1='pshade',year=30))  #数据替换
print(name.isdigit()) #是否是数字
print('23abc'.isalnum()) #判断数字和阿拉伯语
print('abA'.isalpha()) #判断纯英文字符包含大写
print('1A'.isidentifier()) #判断是否是合法的变量名
print('My Name Is Pshade'.istitle()) #判断每个首字母是否大写
print('+'.join(['1','2','3'])) #把+加入到列表里
print(name.ljust(50,'*')) #打印50个字符，字符串放在左边，不足50的用*补
print('    ---'.lstrip()) # 去掉左边的空格和enter
print('my name is pshade'.replace('a','A',1)) #把a换成A，从左到右只换一个
print('my name is pshade'.rfind('a')) #从左到右找最后一个a的下标
print('1+2+3+4'.split('+')) # 以+作为分隔符分隔字符串
print('pSHADE'.swapcase()) #大小写互换
print('my name is pshade'.title())  #首字母大写
