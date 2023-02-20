"""
从1.12版本开始，该库开始支持通过 mathematical-expression 包进行各个组件的获取
您只需要调用该包中所有子文件的 get_instance 函数获取到计算组件。

Starting from version 1.12, the library supports the acquisition of various components through the
mathematical-expression package You only need to call get of all sub-files in the package_ The instance function
obtains the calculation component.
"""
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


def register_function(fun):
    """
    注册一个函数到管理者函数库中
    :param fun: 需要被注册的函数实现类对象
    """
    CalculationManagement.register_function(fun)
