empty_dict = {}  # 空字典
empty_set = set()  # 這個才是空集合

even_set = {2, 4, 6, 8}
odd_set = {1, 3, 5, 7}

word = 'letters'
print(set(word))
word_list = ['a', 'a', 'a','b','b','c','d', 'aaa']
print(set(word_list))
person_1 = {"name":"小明", "age": 25, "city": "台北"}
print(set(person_1))

even_set.add(10)
odd_set.add(9)
print(even_set, odd_set)

# 交集 &
# 聯集 |

Alice_hobbies = {"閱讀", "游泳", "旅行", "電影"}
Bob_hobbies = {"電影", "旅行", "籃球", "音樂"}
common_hobbies = Alice_hobbies & Bob_hobbies  # & shift + 7
print(common_hobbies)
all_hobbies = Alice_hobbies | Bob_hobbies  # | shift + \
print(all_hobbies)

# 差集(用減法)
only_Alice_hobbies = Alice_hobbies - Bob_hobbies
print(only_Alice_hobbies)
only_Bob_hobbies = Bob_hobbies - Alice_hobbies
print(only_Bob_hobbies)
