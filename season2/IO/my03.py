s = ["计开源\n", "计老三\n", "计老五\n"]
with open(r"e:\bb.txt", "w", encoding="utf-8") as f:
    f.writelines(s)

with open(r"e:\bb.txt", "r", encoding="utf-8") as f:
    print(f.read())
    # print(f.read(4))
    # print(f.readlines())


