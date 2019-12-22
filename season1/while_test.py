# 利用while循环打印从0-10的数字

num = 0
while num <= 10:
    print(num)
    # print(num, end="\t")
    num += 1


# 计算1-100之间数字的累加和

num2 = 0
sum_all = 0

while num2 <= 100:
    sum_all = sum_all + num2
    num2 += 1

print("1-100所有数的累加和：", sum_all)
