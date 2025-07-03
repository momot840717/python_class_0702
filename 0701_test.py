# 練習取從混合型態資料取資料
mixed_data = {
    "name": "小明",                      
    "age": 25,                          
    "height": 172.5,                   
    "hobbies": ["閱讀", "打球"],         
    "scores": {"math": 90, "eng": 85}, 
    "birthday": (1999, 7, 1)
}

# 1. 取得 mixed_data 的名字、身高
print(mixed_data["name"], mixed_data['height'])

# 2. 取得 mixed_data 的第二個興趣(hobby)
hobby = mixed_data["hobbies"]  # ["閱讀", "打球"]
print(hobby[1])  # ["閱讀", "打球"][1] --> "打球"
# 2-1 興趣裡的閱讀改成唱歌，並新增 "R.A.P"
hobby[0] = "唱歌"
hobby.append("R.A.P")
print(mixed_data)

# 3. 取得英文分數
eng_score = mixed_data['scores']['eng']  # {"math": 90, "eng": 85}['eng'] -->85
print(eng_score)
# 3-1 新增總分到字典裡 -> {"math": 90, "eng": 85, "total": 175}
total = mixed_data['scores']['eng'] + mixed_data['scores']['math']
mixed_data['scores']['total'] = total
print(mixed_data)

# 4 用一行程式 獲得生日的年月日 一次存在3個變數(year, month, day)
year, month, day = mixed_data['birthday']  # (1999, 7, 1)
print(year, month, day)