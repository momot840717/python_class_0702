list_a = [1,2,3,4,'5','6','7']
# index   0 1 2 3  4   5   6
# 倒過來  -7-6-5-4 -3  -2  -1  <<<
# print(list_a[5])
# print(list_a[0]+list_a[1])  # 1+2 ->3
# print(list_a[4]+list_a[5]) 

# print(list_a[-1], list_a[-2])
# print(list_a[0:4])  # 0~3
# print(list_a[2:5])  # 2~4
# print(list_a[:])
# print(list_a[0:4:2])
# print(list_a[::-1])
# print(list_a[3::-1])


# list 可以改變自己列表的長度、資料
list_b = [1,2,3]
# list_c = list_b  # 把 list_b 賦值給 list_c (這樣會共享記憶體)

# 如果不想共享記憶
# list_c = list_b[:]  # 先切片後賦值

# import copy  # 導入複製模組
# list_c = copy.deepcopy(list_b)

# list_b.append(4)
# list_b.append([4,5,6])
# print(list_b)
# print(list_b[4], list_b[4][0])
# print(list_c)  # 觀察list_c有沒有改變

# 切片不能完全取消共享記憶體
# list_d = [1,2,3,[7,8,9]]
# list_e = list_d[:]
# list_d[1] = 4
# list_d.append(10)
# print(list_d, list_e)
# list_d[3].append(10)
# print(list_d, list_e)
# list_d.insert(1,87)
# print(list_d)

# 用 extend 合併 list
list_1 = ['apple', 'banana']
list_2 = ['coconut', 'dragon fruit']
list_1.extend(list_2)
# print(list_1)
# del list_1[2]
# print(list_1)
# list_1.remove('apple')
# print(list_1)

pop_thing = list_1.pop()  # 預設-1，刪除最後元素
print(list_1, pop_thing)