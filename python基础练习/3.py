
# 设计一个简单的用户密码验证

password = "abc012"
times = 3
while times:
    input_password = input("请输入用户密码：")
    if "*" in input_password:
        print("密码中不能含有*号")
    elif input_password == password:
        print("密码正确")
        break
    else:
        print("密码错误")
        times -= 1