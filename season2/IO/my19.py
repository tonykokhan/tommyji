# 【示例 3-22】使用递归求 n!
# 测试递归


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)     # 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1


a = factorial(10)
print(a)
