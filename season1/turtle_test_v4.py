# 绘制不同颜色的多个同心圆
import turtle

t = turtle.Pen()

# t.goto(0, 0)
# t.circle(100)
#
# t.goto(0, -100)
# t.circle(200)
#
# t.goto(0, -200)
# t.circle(300)

my_colors = ("red", "yellow", "blue", "green")

t.width(4)
t.speed(0)

for i in range(100):
    t.penup()
    t.goto(0, -i * 10)
    t.pendown()
    t.color(my_colors[i % len(my_colors)])
    t.circle(15 + i * 10)

turtle.done()   # 程序执行完，窗口依然在
