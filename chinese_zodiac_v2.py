# 记录生肖，根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# year = 2018
year = int(input('请用户输入出生年份：'))

# print(chinese_zodiac[year % 12])

if(chinese_zodiac[year % 12]) == '狗':
    print('狗年运势。。。')

# for cz in chinese_zodiac:
#     print(cz)
#
# for i in range(1, 13):
#     print(i)

for year in range(2000, 2069):
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

# import time
# num = 5
# while True:
#     num = num + 1
#
#     if num == 10:
#         continue    # 跳过当前这次循环
#
#     print(num)
#     # time.sleep(1)
