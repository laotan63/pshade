def fib(max):
    n,a,b = 0,0,1
    while n< max:
        yield b
        a,b = b,a+b
        n+=1
    return '>>>>>>>hello-------'

f = fib(10)
while True:
    try:
        x = next(f)
        print('f:',x)
    except StopIteration as e:
        print('Error:',e.value)
        break