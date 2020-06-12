import time

def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('haha.txt','a+') as f:
        f.write('%s I Love You\n' %time_current)

def test1():
    print('----------')
logger()

def test2():
    print('>>>>>>>>>>')
logger()

