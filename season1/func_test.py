a = "False"     # 非空字符串，是True
if a:
    print("非空字符串，是True")

b = []  # 列表作为条件表达式，由于为空列表，是False
print(bool(b))
if not b:
    print("空的列表是false")

c = True
if c:
    print("c")

d = 10
if d:
    print("d")

if 3 < d < 100:
    print("3<d<100")
