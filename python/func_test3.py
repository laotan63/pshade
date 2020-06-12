
def test1():
    print('in the test1')

def test2() :
    print('in the test2')
    return 0  #return后面都不运行

def test3():
    print('in the test3')
    return 1,'hello',['pshade','songzuer'],{'name':'hhs'}

x = test1()
y = test2()
z = test3()
print(x)
print(y)
print(z)