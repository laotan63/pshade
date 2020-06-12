
def test(x,y):
    print(x)
    print(y)
test(1,2)  #关键参数不能卸载位置参数前面

def test1(a,b=2):
    print(a)
    print(b)
test1(3)
#默认参数特点：调用函数的时候，默认参数非必须传递