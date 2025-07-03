# 建立一個描述人的字典
person_1 = {
    "name":"小明",
    "age": 25,
    "city": "台北"
    }

print(
f"""名字: {person_1['name']},
年齡: {person_1['age']},
居住地: {person_1['city']}""")

person_1['sexual'] = "男"
"""
因為 sexaul 不在 person_1 字典的 key 裡面
所以會直接新增 'sexaul': "男" 到 person_1
"""

person_1["city"] = "台中"
"""
因為 city 在 person_1 字典的 key 裡面
所以會直接把"台北"修改成"台中"
"""
# print(person_1)

# 用 get() 取資料的方式
age_1 = person_1.get("age", '這筆資料沒有 age 的 key')
# height_1 = person_1["height"]  # KeyError: 'height' 字典沒有 'height'
height_1 = person_1.get('height', '這筆資料沒有 height 的 key')
# print(age_1)
# print(height_1)

# 用 keys() 取得所有 key
print(list(person_1.keys()))
# 用 values() 取得所有 value
print(list(person_1.values()))
# 用 items() 取得所有 (key, value)
person_1_items = list(person_1.items())
print(person_1_items)
print(len(person_1))

for i in person_1: # 如果直接變數迭代字典
    print(i)  # 只會接到 key
    print(person_1[i])  # 再代回字典呼叫 value

for key, value in person_1_items:
    print(key, value)