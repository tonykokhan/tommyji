# 测试多分支选择结构

score = int(input("请输入分数："))
grade = ""

if score < 60:
    grade = "不及格"
elif score < 80:    # 60-80之间
    grade = "及格"
elif score < 90:
    grade = "良好"
else:
    grade = "优秀"

print("分数是{0}，等级是{1}".format(score, grade))
