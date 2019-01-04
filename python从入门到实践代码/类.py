class Dog():
    # 一次模拟小狗的简单尝试

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        # 模拟小狗被命时令蹲下
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        # 模拟小狗被命令时打滚
        print(self.name.title() + " rolled over!")

# 根据类创建实例
my_dog = Dog('willie', 6)

# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")


# 调用方法
# my_dog.sit()
# my_dog.roll_over()

# 创建多个实例
my_dog = Dog('willie', 6) 
your_dog = Dog('lucy', 3)
# print("My dog's name is " + my_dog.name.title() + ".") 
# print("My dog is " + str(my_dog.age) + " years old.")

# my_dog.sit()
# your_dog.sit()
# print("\nYour dog's name is " + your_dog.name.title() + ".") 
# print("Your dog is " + str(your_dog.age) + " years old.") 



# Car类

class Car():
    # 一次模拟汽车的简单尝试

    def __init__(self, make, model, year):
        # 初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):# 返回整洁的描述性信息
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()


    def read_odometer(self):# 打印一条指出汽车里程的消息
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    
    def update_odometer(self, mileage):# 通过方法修改属性的值
        self.odometer_reading = mileage# 将里程表读数设置为指定的值
        if mileage >= self.odometer_reading:# 将里程表读数设置为指定的值，禁止将里程表读数往回调
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):# 将里程表读数增加指定的量
        self.odometer_reading += miles

class Battery():
    # 一次模拟电动汽车的简单尝试
    def __init__(self, battery_size=70):
        #初始化电瓶的属性
        self.battery_size = battery_size

    def describe_battery(self):
        # 打印一条描述电瓶容量的消息
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        # 打印一条消息，指出电瓶的续航里程
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270   

        message = "This car can go approximately " + str(range) 
        message += " miles on a full charge."
        print(message)
         


# my_new_car = Car('audi', 'a4', 2016) 
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(23)

# my_used_car = Car('subaru', 'outback', 2013) 
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23500) 
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100) 
# my_used_car.read_odometer()

'''
注意 你可以使用类似于上面的方法来控制用户修改属性值（如里程表读数）的方式，
但能够访问程序的人都可以通过直接访问属性来将里程表修改为任何值。
要确保安全，除了进行类似于前面的基本检查外，还需特别注意细节。
'''



# 类继承

class ElectrioCar(Car):
    def __init__(self, make, model, year):
        # 初始化父类的属性
        # 初始化电动汽车特有的属性
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectrioCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()


