person_1 = {
    "name":"小明",
    "age": 25,
    "city": "台北"
    }

update_data = {
    "age": 26,
    "city": "新北",
    "job": "工程師"
}

# update() 更新
"""
如果新字典有原字典的 key, 新的 value 會覆蓋原有的
如果新字典沒有原字典的 key, 直接新增新的 key: value
"""
person_1.update(update_data)  # 沒有回傳值，直接改變原字典
# print(person_1)

# two sum

num_list = [2,5,7,8]
target = 9
index_list = []

# 暴力雙重迴圈
for i in range(0, len(num_list)):
    for j in range(i+1, len(num_list)):
        if num_list[i] + num_list[j] == target:
            index_list.append(i)
            index_list.append(j)

# print(index_list)  # [0, 2]

num_list = [2,5,7,8]
target = 9
index_list = []
# 搭配字典
num_dict = {}
for i in range(0, len(num_list)):
    diff = target - num_list[i]
    if num_list[i] in num_dict:
        index_list.append(num_dict[num_list[i]])
        index_list.append(i)
    num_dict[diff] = i  # {7:0, 4:1, ...}
print(index_list)





