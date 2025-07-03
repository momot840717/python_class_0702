# account_data = ['abc123', 'star213', 'a1234567', 'qwer1234']
# account = input("請輸入帳號:")

# print(account in account_data)

# if account in account_data:
#     print("有此帳號")
# else:
#     print("無此帳號，請註冊")


# for 迴圈 in range()

# for i in range(0,5,1):
#     print(i)

# for account in ['abc123', 'star213', 'a1234567', 'qwer1234']:
#     print(account)

# number_list = []
# for i in range(1, 101):
#     number_list.append(i)
#     # print(number_list)
# print(number_list)

# total = 0
# for num in number_list:
#     print(f"目前 total: {total}, num: {num}")
#     total += num  # total = total + num
#     print(f"目前總和: {total}")

# for num in number_list:
#     if (num <=30) or (num >=70):
#         print("第一組")
#     else:
#         print("第二組")

# even_list = []
# odd_list = []
# for num in number_list:
#     if num % 2 == 0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)

# print(even_list,'\n', odd_list)
# even_list = [num for num in number_list if num%2==0]

# for i in range(1,10):
#     if i == 3:
#         continue
#     elif i == 7:
#         break
#     print(i)

# print("break 跳出來了")

# count = 0
# while count < 6:
#     if count == 0:
#         print('從0開始囉')
#     else:
#         print(f'現在數到 {count} 次')
#     count += 1

# 波浪動畫
# import time

# style = '=====~~~====='
# width = 20
# step  = 0
# direction = 1

# while True:
#     print(' '*step+style)
#     step += direction
#     if (step >= width) or (step <= 0):
#         direction *= -1
#     time.sleep(0.05)


# # tuple 不可以被改變 會 error
# tuple_1 = (2,3,4)
# # tuple_1[1] = 5  --> 不能改變
# for i in tuple_1:
#     print(i)

# zip() 並排合併
a = [1,2,3,4]
b = ['apple', 'banana', 'cat', 'dog']
zip_ab = zip(a, b)
print(zip_ab)
"""
<zip object at 0x0000021575B6B800>
zip 物件 在某個記憶體位置
"""
list_ab = list(zip_ab)  # 一定要存進變數!!!
for num, word in list_ab:
    print(f"編號: {num}, 單字: {word}")