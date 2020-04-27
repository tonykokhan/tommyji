# 【操作】将对象序列化到文件中
import pickle
with open(r"data.dat", "wb") as f:
    a1 = "开源"
    a2 = 234
    a3 = [20, 30, 40]
    pickle.dump(a1, f)
    pickle.dump(a2, f)
    pickle.dump(a3, f)
