# 動物叫聲
def animal_sound(animal):
    if animal == '狗':
        print('汪汪')
    elif animal == '貓':
        print('喵喵')
    elif animal == '鳥':
        print('啾啾')
    elif animal == '兔子':
        print('蛤')
    else:
        print('沒有此動物')


# while True:
#     animal = input('輸入動物, 或是輸入 X 結束迴圈: ')
#     if animal in 'Xx':
#         print('退出迴圈')
#         break
#     animal_sound(animal)

# 判斷三角形
def triangle_type(a, b, c):
    # 把 a,b,c 加入列表 然後用 sorted()排序 再重新賦值給 a,b,c
    a, b, c = sorted([a, b, c])
    print(a, b, c)
    # 檢查是否為有效三角形
    if a + b <= c:
        return "這不是一個三角形！（不符合三角形不等式）"
    elif a == b == c:
        return "這是正三角形"
    elif a**2 + b**2 == c**2:
        return "這是直角三角形"
    elif a**2 + b**2 < c**2:
        return "這是鈍角三角形"
    elif a**2 + b**2 > c**2:
        return "這是銳角三角形"

# while True:
#     a = int(input('輸入第一條邊長: '))
#     b = int(input('輸入第二條邊長: '))
#     c = int(input('輸入第三條邊長: '))
#     print(triangle_type(a, b, c))

# 猜數字
import random
def guess_the_number(start=1, end=100):  # 預設 start=1, end=100, 但是你還是可以代入參數改變預設值
    print(f"終極密碼開始, 範圍是 {start} ~ {end}")
    target = random.randint(start, end)  # 從 1~100 隨機選一個數字
    while True:
        guess_num = int(input('輸入你要猜的整數:'))
        if guess_num == target:
            print('恭喜猜對✨')  # win + >
            break  # 猜對後結束迴圈
        elif guess_num > target:
            print(f'範圍是 {start} ~ {guess_num}')
            end = guess_num  # 猜的數字比較大，猜的數字當新範圍終點
        elif guess_num < target:
            print(f'範圍是 {guess_num} ~ {end}')
            start = guess_num  # 猜的數字比較小，猜的數字當新範圍起點

# guess_the_number()  # 範圍 1~100
# guess_the_number(start=100, end=200)  # 範圍修改成 100~200


# 點餐資料蒐集
def add_to_order(item, result=None):
    if result == None:
        result = []
    result.append(item)
    return result

# menu = None
# while True:
#     meal = input('要點甚麼: ')
#     if meal == '結束':
#         break
#     menu = add_to_order(meal, menu)
#     print(menu)


# TEST
"""
題目 1: 打招呼函數
題目說明：
請設計一個函數 say_hello(name)，輸入一個名字，輸出 Hello, {名字}!
"""
def say_hello(name):
    return f"Hello, {name}"
# print(say_hello('小明'))

"""
題目 2: 計算平方
題目說明：
設計函數 square(x)，傳入一個數字 x，回傳它的平方值。
"""
def square(x):
    return x**2

"""
題目 3: 偶數判斷
題目說明：
請寫一個函數 is_even(number)，判斷傳入的 number 是否為偶數，如果是，回傳 True，否則回傳 False。
"""
def is_even_1(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def is_even_2(number):
    if number % 2 == 0:
        return True
    return False

def is_even_3(number):
    return number%2 == 0


# *args
def print_args(arg1, *args):
    print(arg1)
    print(args)

# print_args(1,1,4,4,8,4,4,4,"a","2","bbb","c","d")

# *kwargs
def print_kwargs(**kwargs):
    print(kwargs)

# print_kwargs(name='小名', age=18, city='台北')  
# {'name': '小名', 'age': 18, 'city': '台北'}


# 函數裡面有for迴圈，資料迭代回傳
# def num_generate(times):
#     for i in range(times):
#         print(f'內部 {i}')
#         yield i  # return 換成 yield 就可以把所有迭代資料送出去

# for i in num_generate(10):
#     print(f'外部 {i}')

