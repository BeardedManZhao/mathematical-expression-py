# -*- coding: utf-8 -*-
# @Time : 2022/11/12 13:08
# @Author : zhao
# @Email : liming7887@qq.com
# @File : bracketsCalculation.py
# @Project : mathematical_expression-py
import re

from mathematical_expression.core.calculation.number.numberCalculation import NumberCalculation
from mathematical_expression.core.manager import ConstantRegion

"""正则表达式对象，用于将所有的不可见字符删除"""
ALL_INVISIBLE_CHARACTERS_PATTERN = re.compile("\\s+")


class BracketsCalculation(NumberCalculation):
    """
    括号解析算法计算一个公式的计算组件的父类，其中的计算具体实现是一个抽象，等待实现 The bracket parsing algorithm calculates the parent class of the
    calculation component of a formula, in which the specific implementation of the calculation is an abstract,
    waiting to be implemented
    """

    def format_str(self, string: str) -> str:
        """
        格式化一个公式 使得其可以被该计算组件进行运算，这里是将字符串格式化成为能够被括号解析组件计算的公式 Format a formula so that it can be calculated by the
        calculation component. Here is to format the string into a formula that can be calculated by the bracket
        resolution component
        :param string:需要被格式化的数学公式
        :return:格式化之后的顺序额表达式
        """
        return ALL_INVISIBLE_CHARACTERS_PATTERN.sub(
            ConstantRegion.EMPTY, string
        ).strip(ConstantRegion.ARITHMETIC_OPERATOR_STRING)
