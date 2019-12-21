# 内置函数reversed()也支持进行逆序排列，与列表对象reverse()方法不同的是，内置函数reversed()不对原列表做任何修改
# 只是返回一个逆序排列的迭代器对象。

a = [20, 10, 30, 40]
c = reversed(a)
print(c)
print(list(c))
print(list(c))

# 我们打印输出c发现提示：list_reverseiterator。也就是一个迭代对象。同时，我们使用list(c)进行输出，发现只能使用一次。
# 第一次输出了元素，第二次为空。那是因为迭代对象在第一次时已经遍历结束了，第二次不能再使用。

