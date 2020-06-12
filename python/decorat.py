import time
user,passwd = 'pshade','abc123'
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            print("wrapper args func:", *args, **kwargs)
            if auth_type == "local":
                username = input('Username:').strip()
                password = input('Password:').strip()
                if user == username and passwd == password:
                    print('\033[43;1mUser has passed authentication\033[0m')
                    return func(*args, **kwargs)
                else:
                    exit("\033[31;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print('>>>>>>>>>>>>>exit')
        return wrapper
    return outer_wrapper
def index():
    print('welcome to index page')
@auth(auth_type="local")
def home():
    print('welcome to home page')
    return "from home"
@auth(auth_type="ldap")
def bbs():
    print('welcome to bbs page')

index()
print(home())
bbs()