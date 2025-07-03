# fruits = ['apple', 'banana', 'coconut', 'dragon fruit']

# index = int(input('輸入0~3: '))  # input會輸出字串 所以再轉成 int

# fruit = fruits[index]

# if fruit == 'apple':
#     print('這是蘋果')
# elif fruit == 'coconut':
#     print('這是椰子')
# else:
#     print('這是其他水果')


prices = [25, 50, 80, 120]  # 水果價格表
index = 2  # 可以自己改
price = prices[index]

if price <= 30:
    print("便宜水果")
elif price <= 100:
    print("中等價位")
else:
    print("昂貴水果")
