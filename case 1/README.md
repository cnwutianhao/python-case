### 判断是工作日还是休息日

1. 使用轮子 `chinese_calendar`
2. 获取当前日期：```datetime.datetime.now().date()```
</br>指定某个日期：```datetime.datetime(2022, 12, 6)```
3. 使用轮子提供的方法`is_workday`来判断是工作日还是休息日
