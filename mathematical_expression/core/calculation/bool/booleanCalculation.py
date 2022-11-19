# -*- coding: utf-8 -*-
# @Time : 2022/11/14 12:50
# @Author : zhao
# @Email : liming7887@qq.com
# @File : booleanCalculation.py
# @Project : mathematical_expression-py
import re
from typing import List, Union, Any

from mathematical_expression.core.calculation.Calculation import Calculation
from mathematical_expression.core.calculation.number import bracketsCalculation2
from mathematical_expression.core.manager import CalculationManagement, ConstantRegion
from mathematical_expression.exceptional.WrongFormat import WrongFormat


class BooleanCalculation(Calculation):
    """
    计算一个比较表达式的计算组件的父类，计算结果一般都是包含布尔值结果的对象
    Compute the parent class of the calculation component of a comparison expression.
    The calculation result is generally an object containing Boolean results
    """

    # 比较表达式计算所依赖的第三方组件
    BRACKETS_CALCULATION_2: bracketsCalculation2 = bracketsCalculation2.get_instance(
        CalculationManagement.BRACKETS_CALCULATION_2_NAME
    )

    def format_str(self, string: str) -> str:
        return string.replace(ConstantRegion.EMPTY, ConstantRegion.NO_CHAR)

    def check(self, string: str) -> None:
        """
        :param string: 需要被检查的公式
        """
        split: List[Union[str, Any]] = re.split(ConstantRegion.REGULAR_COMPARISON_OPERATOR, string)
        length = len(split)
        # 判断是否属于布尔表达式
        if length == 2:
            # 检查表达式两边是否符合条件
            left = split[0]
            right = split[1]
            if left is not None:
                self.BRACKETS_CALCULATION_2.check(left)
            if right is not None:
                self.BRACKETS_CALCULATION_2.check(right)
        else:
            # 如果比较运算符两边的表达式不是2个，说明不是一个布尔表达式
            raise WrongFormat("发生了错误，您的布尔表达式中，存在着数量不正确的比较运算符\n" +
                              "An error has occurred. There is an incorrect number of comparison operators in your "
                              "Boolean "
                              "expression\n"
                              "Number of comparison operators [" + str(length - 1) + "]")

    def calculation(self, formula: str, format_param: bool = True):
        """
        计算一个数学表达式，并将计算细节与计算结果存储到数值结果集中。
        Compute a mathematical expression and store the calculation details and results in the numerical result set.
        :param formula: 需要被计算的公式
        :param format_param: 如果设置为true 代表需要格式化
        :return:数值结果集对象，其中保存着每一步的操作数据，以及最终结果数值
                Numerical result set object, which stores the operation data of each step and the final result value
        """
        pass
