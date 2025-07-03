"""
題目 5: 計算 BMI
說明：寫一個函數 calculate_bmi(weight, height)，計算 BMI 值（體重 / 身高平方）
"""
def calculate_bmi(weight, height):
    height /= 100  # height = height / 100
    bmi = weight / height**2
    return bmi

# print(calculate_bmi(65, 170))


# 匿名函數 lambda

# 2x+3
func_1 = lambda x: 2*x+3
print(func_1(5))

# 平方數
squared_num = lambda x: x**2
print(squared_num(55))

# 打招呼函數
say_hello = lambda name: f"Hello, {name}"
print(say_hello("John"))

# 判斷是否偶數
is_even = lambda x: x%2 == 0
print(is_even(10))

# 兩個以上參數
two_sum = lambda x, y: x+y
print(two_sum(2, 3))

# map(函數, 可迭代資料) 讓函數作用每個元素
squared_num = lambda x: x**2
data = [1,5,85,78,9,69,2]
print(list(map(squared_num, data)))

"""
題目: 設計匿名函數，功能是把攝氏溫度轉換成華氏溫度
華氏溫度 = 攝氏溫度 * 9/5 +32
"""
lambda x: x*9/5 + 32