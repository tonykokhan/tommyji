f = open(r"e:\bb.txt", "w", encoding="utf-8")
s = ["计开源\n", "计老三\n", "计老四\n"]
f.writelines(s)
f.close()
