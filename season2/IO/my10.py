# 【操作】将获得的数据反序列化成对象
import pickle
with open(r"data.dat", "rb") as f:
    a1 = pickle.load(f)
    a2 = pickle.load(f)
    a3 = pickle.load(f)
    print(a1)
    print(a2)
    print(a3)
