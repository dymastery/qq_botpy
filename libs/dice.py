import random

# 骰子类定义
class Dice:
    """
    定义骰子的类：
    face: 骰子面数
    `d_example = Dice(6)`: 创建一个六面骰
    `d_example()`: 骰d6的值
    """
    # 实例化
    def __init__(self, face):
        self.__face = face
    
    # 投骰子函数
    def __call__(self):
        return random.randint(1, self.__face)
    
