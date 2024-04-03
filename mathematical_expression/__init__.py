"""
从1.12版本开始，该库开始支持通过 mathematical-expression 包进行各个组件的获取
您只需要调用该包中所有子文件的 get_instance 函数获取到计算组件。

Starting from version 1.12, the library supports the acquisition of various components through the
mathematical-expression package You only need to call get of all sub-files in the package_ The instance function
obtains the calculation component.
"""
# 布尔比较运算表达式计算组件
from mathematical_expression.core.calculation.bool import booleanCalculation2
# 括号表达式计算组件
from mathematical_expression.core.calculation.number import bracketsCalculation2
# 区间内累加求和计算组件
from mathematical_expression.core.calculation.number import cumulativeCalculation
# 区间内快速累乘计算组件
from mathematical_expression.core.calculation.number import fastMultiplyOfIntervalsBrackets
# 区间内快速累加计算组件
from mathematical_expression.core.calculation.number import fastSumOfIntervalsBrackets
# 自定义单形参函数表达式计算组件
from mathematical_expression.core.calculation.number import functionFormulaCalculation
# 自定义多形参函数表达式计算组件
from mathematical_expression.core.calculation.number import functionFormulaCalculation2
# 无括号数学表达式计算组件
from mathematical_expression.core.calculation.number import prefixExpressionOperation
# 计算组件管理者对象
from mathematical_expression.core.manager import CalculationManagement


def get_instance(calculation, calculation_name):
    """
    使用类似Java的方式获取到一个计算组件
    Get a computing component in a Java-like way
    :param calculation: 需要被实例化的计算组件类
    Calculation component class to be instantiated
    :param calculation_name: 实例化使用的计算组件名称
    Calculation component name used for instantiation
    :return: 获取到的计算组件对象，可直接引用其中的所有函数。
    The obtained calculation component object can directly reference all functions in it.
    """
    return calculation.get_instance(calculation_name)


def register_function(fun):
    """
    注册一个函数到管理者函数库中
    :param fun: 需要被注册的函数实现类对象
    """
    CalculationManagement.register_function(fun)


def register_function_expression(fun):
    """
    注册一个函数到管理者函数库中
    :param fun: 需要被注册的函数实现类对象
    """
    CalculationManagement.register_function_expression(fun)


def unregister_function(fun):
    """
    取消注册一个函数
    :param fun: 需要被取消注册的函数对象
    """
    CalculationManagement.unregister_function(fun)
