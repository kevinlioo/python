
# 传递任意数量的实参
def make_pizza(*toppings):
    # 打印顾客点的所有配料
    print(toppings)
make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


def make_pizza(*toppings):
    # 概述要制作的披萨
    print("\nMaking a pizza with the fllowing toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    # 概述要制作的披萨
    print("\nMaking a " + str(size) + "-inch pizza with the follwing toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# 8-5-2
def build_profile(first, last, **user_info):
        # 创建一个字典，其中包含我们知道的有关用户的一切
        profile = {}
        profile['first_name'] = first
        profile['last_name'] = last
        for key, value in user_info.items():
                profile[key] = value
        return profile
user_profile = build_profile('albert', 'einstrin', locals='princeton', field='physics')
print(user_profile)