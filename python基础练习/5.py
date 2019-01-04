# 有红、黄、蓝三种颜色的球，其中红球3个，黄球3个绿球6个，
# 先将这12个球混合放在一个盒子中，
# 从中任意摸出8个球，编程计算摸出球的各种颜色搭配。


for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red + yellow + green == 8:
                print("red:{}".format(red))
                print("yellow:{}".format(yellow))
                print("green:{}".format(green))
