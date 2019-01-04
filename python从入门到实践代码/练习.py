'''

模块 random 包含以各种方式生成随机数的函数，
其中的 randint()返回一个位于指定范围内的整数，例如，下面的代码返回一个 1~6 内的整数：

from random import randint x = randint(1, 6)

请创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。
编写一个名为 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数。创建一个 6 面的骰
子，再掷 10 次。
创建一个 10 面的骰子和一个 20 面的骰子，并将它们都掷 10 次。

'''

import random

class Die():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die():
        

