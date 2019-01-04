import random

secert = random.randint(1,100) # 计算生成一个随机数

times = 3 # 初始化用户的次数是3次

while times:
    num = input("请输入数字：")
    if num.isdigit():
        tmp = int(num)
        if tmp == secert:
            print("你猜对了!!")
            break
        elif tmp < secert:
            print("你的数字太小了！")
            times = times - 1
        else:
            print("你的数字太大了！")
            times = times - 1
    else:
        print("叫你输入数字")
print("你的机会用完了")