# -*- coding: utf-8 -*-
# @Time : 2022/11/15 7:47
# @Author : zhao
# @Email : liming7887@qq.com
# @File : cumulativeCalculation.py
# @Project : mathematical_expression-py
import re

from mathematical_expression.core.calculation.number.bracketsCalculation2 import BracketsCalculation2
from mathematical_expression.core.manager import CalculationManagement, ConstantRegion
from mathematical_expression.exceptional.ExtractException import ExtractException
from mathematical_expression.exceptional.WrongFormat import WrongFormat
from mathematical_expression.utils import StrUtils

INTERVAL_EXTRACTION_PATTERN = re.compile("[\\[\\]]")


class CumulativeCalculation(BracketsCalculation2):
    """
    累加计算公式解析组件，支持使用未知形参，以及其区间作为公式进行累加加过的计算
    例如传入公式 “n [0, 10, 2] (1 + n * n)” 就是 (1 + 0 * 0) + (1 + 2 * 2) + ... + (1 + 10 * 10)
    The cumulative calculation formula analysis component supports the use of unknown formal parameters
    and their intervals as formulas for cumulative calculation.
    For example, the formula "n [0, 10, 2] (1+n * n)" passed in is (1+0 * 0)+(1+2 * 2)+...+(1+10 * 10)
    """

    def format_str(self, string: str) -> str:
        split = INTERVAL_EXTRACTION_PATTERN.split(string)
        # 获取到累加的符号
        f = split[0]
        # 获取到区间中的起始终止与步长数值
        s = split[1].split(',')
        start = StrUtils.string_to_double(s[0])
        end = StrUtils.string_to_double(s[1])
        equal_difference = StrUtils.string_to_double(s[2])
        # 获取公式位
        format1 = split[2]
        # 构造累加公式
        new_formula: list = []
        number: int = start
        while number <= end:
            new_formula.append(ConstantRegion.LEFT_BRACKET)
            new_formula.append(format1.replace(f, str(number)))
            new_formula.append(ConstantRegion.RIGHT_BRACKET)
            new_formula.append(ConstantRegion.PLUS_SIGN)
            number += equal_difference
        return super().format_str(
            ConstantRegion.EMPTY.join(new_formula).strip(ConstantRegion.ARITHMETIC_OPERATOR_STRING))

    def calculation(self, formula: str, format_param: bool = True):
        return super().calculation(self.format_str(formula) if format_param else formula, False)

    def check(self, string: str):
        split = INTERVAL_EXTRACTION_PATTERN.split(string)
        if len(split) == 3:
            if len(split[1].split(',')) == 3:
                super().check(split[2].replace(split[0], '0'))
            else:
                raise WrongFormat(
                    "检查到公式的错误，区间的配置不正确哦！正确的区间配置：自变量名称[起始值，终止值，等差值]\nThe formula error is detected, and the interval "
                    "configuration is incorrect! Correct interval configuration: argument name [start, end, "
                    "equalDifference]"
                    "Wrong interval configuration => " + split[1])
        else:
            raise WrongFormat(
                "检查到公式的错误，公式的格式似乎不正确，正确示例：n[0,10,1](1+(n)*n)\nAn error is detected in the formula. The format of the "
                "formula seems incorrect. A correct example: n[0,10,1](1+(n)*n)\n"
                "Wrong interval configuration => " + string)


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
        res = CumulativeCalculation(name)
        if CalculationManagement.register(res, True):
            return res
        else:
            raise ExtractException("您提取的组件不属于CumulativeCalculation，请您更换一个组件名称吧！\n"
                                   "The component you extracted does not belong to CumulativeCalculation, "
                                   "please change a component name!\n "
                                   "ERROR NAME => " + name)
