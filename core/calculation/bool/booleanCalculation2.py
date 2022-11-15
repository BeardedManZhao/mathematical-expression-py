# -*- coding: utf-8 -*-
# @Time : 2022/11/14 13:01
# @Author : zhao
# @Email : liming7887@qq.com
# @File : booleanCalculation2.py
# @Project : mathematical-expression-py
import re

from core.calculation.bool.booleanCalculation import BooleanCalculation
from core.container.CalculationBooleanResults import CalculationBooleanResults
from core.container.CalculationNumberResults import CalculationNumberResults
from core.manager import CalculationManagement
from exceptional.ExtractException import ExtractException
from utils import NumberUtils


class BooleanCalculation2(BooleanCalculation):
    """
    计算一个布尔返回值的表达式，该组件针对两个表达式或数值之间的比较来计算结果数值，用于比较表达式是否成立
    An expression that calculates a Boolean return value.
    This component calculates the result value for the comparison between two expressions or values,
    and is used to compare whether the expression is valid
    """

    def calculation(self, formula: str, format_param: bool = True):
        """
        计算一个比较表达式是否成立，如果成立返回的结果对象中的结果字段应为True
        :param formula: 需要被计算的表达式
        :param format_param: 设置为true会被格式化
        :return:计算出来的结果数据对象
        """
        new_formula: str
        if format_param:
            new_formula = ''.join(self.format_str(formula))
        else:
            new_formula = formula
        # 将左右数据获取到
        split = re.split("<=|>=|!=|<>|==|[<=>]", new_formula)
        s1 = split[0]
        s2 = split[1]
        # 进行比较运算符的提取，这里是先获取到索引
        start = len(s1)
        end = start + 1
        while new_formula[end:] != s2:
            end += 1
        s: str = new_formula[start:end]
        # 判断左右是否有一个null
        if re.match("^null$", s1):
            if re.match("^null$", s2):
                # 如果左边为null ，同时右边为null就代表两个值相同，在这里直接将两个值赋值0
                return CalculationBooleanResults(1, NumberUtils.comparison_operation(s, 0, 0), self.get_name())
            else:
                # 如果左边为null ，同时右边不为null就代表两个值不同，在这里直接将左赋值为0 右边赋值为1
                return CalculationBooleanResults(1, NumberUtils.comparison_operation(s, 0, 1), self.get_name())
        elif re.match("^null$", s2):
            # 如果右 为null 左不为null，代表两个值不同 直接进行1 与 0 的比较
            return CalculationBooleanResults(1, NumberUtils.comparison_operation(s, 1, 0), self.get_name())
        # 没有null就进行左右值的运算
        left: CalculationNumberResults = self.BRACKETS_CALCULATION_2.calculation(s1, format_param)
        right: CalculationNumberResults = self.BRACKETS_CALCULATION_2.calculation(s2, format_param)
        # 返回结果值
        return CalculationBooleanResults(
            left.result_layers + right.result_layers,
            NumberUtils.comparison_operation(s, left.result, right.result),
            self.get_name()
        )


def get_instance(name: str):
    """
    从管理者中获取到一个组件，请注意类型哦！！！因为这里没有提供类型判断
    :param name: 组件的名称
    :return: 组件的对象
    """
    res = CalculationManagement.get_calculation_by_name(name)
    if res is not None:
        return res
    else:
        res = BooleanCalculation2(name)
        if CalculationManagement.register(res, True):
            return res
        else:
            raise ExtractException("您提取的组件不属于BooleanCalculation2，请您更换一个组件名称吧！\n"
                                   "The component you extracted does not belong to BooleanCalculation2, "
                                   "please change a component name!\n "
                                   "ERROR NAME => " + name)
