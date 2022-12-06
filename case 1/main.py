# 判断是工作日还是休息日

from chinese_calendar import is_workday
import datetime

date = datetime.datetime.now().date()
# date = datetime.datetime(2022, 11, 18)
print(date)

if is_workday(date):
    print("是工作日")
else:
    print("是休息日")
