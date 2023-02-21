# -*- coding: utf-8 -*-
# @Time : 2022/11/15 14:05
# @Author : zhao
# @Email : liming7887@qq.com
# @File : Function.py
# @Project : mathematical_expression-py
class Function:
    """
    函数对象，需要实现，在实现好一个函数之后，这个函数可以被其它组件使用
    Function object needs to be implemented. After a function is implemented, it can be used by other components
    """
    name: str

    def __init__(self, name: str):
        """
        函数构造，需要一个名字作为函数名称，这个名称就是在数学表达式中可以使用的名称
        :param name: 函数的名称，是自定义的
        """
        self.name = name

    def run(self, floats):
        """
        函数的运行逻辑，需要实现，在该方法中就是函数的主要作用
        :param floats: 函数的形参，这是一个多参函数，函数的实参在这里被传递进来，其中每一个元素都是在表达式中的一个函数形参
        :return: 运算结果，这个函数的返回值是一个多近一出的函数。
        """
        pass

    def get_name(self) -> str:
        return self.name
