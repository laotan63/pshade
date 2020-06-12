product_list = [
    ('iphone',5000),
    ('ipad',2000),
    ('watch',510),
    ('bycle',300),
    ('water',10),
]
salary = input("请输入你的工资:")
shopping_list = []
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):    # enumerate提取下标
            print(index,item)
        user_choice = input('你想买什么?>>>:')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice>=0:  # 判断选择的商品在列表里，len（）表示长度
                p_item = product_list[user_choice]
                if p_item[1] <= salary: # 买得起
                    shopping_list.append(p_item)
                    salary -=p_item[1]                              #\033[31;1m  \033[0m 把字变成红色41背景红
                    print('Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m'%(p_item,salary))
                else:
                    print('\033[41;1m买不起，您的余额不足,只剩下%s了\033[0m'%(salary))
            else:
                print('\033[33;1mproduct code [%s] is not exit!\033[0m'% user_choice)
        elif user_choice == 'q':
            print('------shopping list------')
            for p in shopping_list:
                print(p)
            print('your current balance is :',salary)
            exit()
        else:
            print('invalid option')

