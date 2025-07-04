# 介紹日期模組
from datetime import datetime, date, timedelta
halloween = date(2025,10,31)
print(halloween, type(halloween))
print(halloween.year)
print(halloween.month)
print(halloween.day)
print(halloween.isoformat(), type(halloween.isoformat()))

now_date = date.today()
print(now_date.isoformat())
print(now_date + timedelta(days=1))  # 天數加1
print(now_date + timedelta(days=30))  # 天數加30

some_day = datetime(2025, 1, 2, 3, 4, 5, 6)
print(some_day)
print(some_day.isoformat())
now_dt = datetime.now()
print(now_dt)
print(now_dt.year)
print(now_dt.month)
print(now_dt.day)
print(now_dt.hour)
print(now_dt.date())
print(now_dt.time())

# strftime 時間轉成文字(可指定格式)
"""
| 格式碼| 意義                   | 範例輸出  |
| ---- | ---------------------- | -------- |
| `%Y` | 年（四位數）            | `2025`   |
| `%m` | 月（01–12）            | `07`     |
| `%d` | 日（01–31）            | `04`     |
| `%H` | 小時（00–23，24 小時）  | `15`     |
| `%M` | 分（00–59）            | `42`     |
| `%S` | 秒（00–59）            | `08`     |
| `%p` | AM/PM（上下午）        | `PM`     |
"""

now_dt = datetime.now()
fmt = "現在是%Y年%m月%d日"
now_string: str = datetime.strftime(now_dt, fmt)  # now_string: str  註解變數是 str 物件
print(now_string)

# strptime — 解析字串為日期
date_str = "2025-07-04 14:30:00"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt, type(dt))

import time
# print(1)
# time.sleep(2)
# print(2)
now_time = time.time()  # 從1970 年 1 月 1 日 00:00:00開始計時
print(now_time)
print(time.ctime(now_time))

# 計算程式效率
now_time = time.time()
for i in range(1000000):
    i
print(time.time()-now_time)
