from collections import namedtuple #导入 namedtuple
"""
#通过namedtuple 快速的创建Class
"""
Car=namedtuple('Car','color mileage')
#通过namedtuple 创建 Car 工厂 ，在工厂创建 color（颜色）,mileage（里程） 参数 （**个人理解**）

my_car=Car('red',3812.4)
#实例化 赋值Car


#通过my_car实例化对象打印
print(my_car.color)
print(my_car.mileage)

#namedtuple 和 tuple 元组一样不可变
# my_car.color='blue'    #AttributeError: can't set attribute  
