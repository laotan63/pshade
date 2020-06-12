import time
user,passwd = 'pshade','abc123'
def auth(func):
    def wrapper(*args,**kwargs):
        username = input('Username:').strip()
        password = input('Password:').strip()
        if user == username and passwd == password:
            print('\033[43;1mUser has passed authentication\033[0m')
            return func(*args,**kwargs)
        else:
            exit("\033[31;1mInvalid username or password\033[0m")
    return wrapper
def index():
    print('welcome to index page')
@auth
def home():
    print('welcome to home page')
    return "from home"
@auth
def bbs():
    print('welcome to bbs page')

index()
print(home())
bbs()