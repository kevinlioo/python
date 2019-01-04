'''
#返回简单值   formatted_name.py
def get_formatted_name(first_name, last_name):
    #返回整洁的姓名
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print("")
print("")
print("")

#让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('john', 'hooker', "lee")
print(musician)

print("")
print("")
print("")

#返回字典  person.py
def build_person(first_name, last_name):
    #返回一个字典，其中包含有管一个人的信息
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

print("")
print("")
print("")

def build_person(first_name, last_name, age=""):
    #返回一个字典，其中包含有管一个人的信息
    person = {'first': first_name, 'last': last_name}
    if age:
        person["age"] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

print("")
print("")
print("")


#结合使用函数和while循环   greeter.py
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

#这是一个无限循环！
while 1:
    print("\nPlease tell me your name:")
    #添加一条消息来告诉用户如何退出，然后在每次提示用户输入时，都检查他输入的是否是退出值，如果是，就退出循环。
    print("(enter 'q' at any time to quit)")
    f_name = input("First name：")
    if f_name =='q':
        break

    l_name = input("Last name：")
    if l_name =='q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


print("")
print("")
print("")



#传递列表  greet_users.py
def greet_users(names):
    #向列表中的每位用户都发出简单的问候
    for name in names:
        msg = "Hello," + name.title() + "！"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

'''

# 在函数中修改列表  printing_models.py

# 首先创建一个列表，其中包含一些要打印的设计
unprinted_desings = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其一道列表completed_models中
while unprinted_desings:
    current_design = unprinted_desings.pop()

    #模拟根据设计制作3D打印模型的过程
    print("Printing model：" + current_design)
    completed_models.append(current_design)

#显示打印好的所有模型
print("\nThe follwing models have been printed：")
for completed_models in completed_models:
    print(completed_models)



