# -*- coding: utf-8 -*-
# @Time : 2022/11/12 12:13
# @Author : zhao
# @Email : liming7887@qq.com
# @File : numberCalculation.py
# @Project : mathematical_expression-py

from mathematical_expression.core.calculation.Calculation import Calculation
from mathematical_expression.core.manager import ConstantRegion
from mathematical_expression.exceptional.WrongFormat import WrongFormat
from mathematical_expression.utils import NumberUtils


class NumberCalculation(Calculation):
    """
    计算结果为数值的数学表达式结果，其中提供了数学表达式的计算函数
    The calculation result is the numerical mathematical expression result,
    in which the calculation function of the mathematical expression is provided
    """

    def calculation(self, formula: str, format_param: bool = True):
        """
        :param formula 被计算的表达式，要求返回值是一个数值。
               The returned value of the evaluated expression is required to be a numeric value.
        :param format_param: 是否要在计算之前对公式进行一个格式化，如果设置为True 那么会先进行一个格式化，然后在进行数学计算
        :return:表达式计算结果

        计算一个数学表达式，并将计算细节与计算结果存储到数值结果集中。
        Compute a mathematical expression and store the calculation details and results in the numerical result set.
        """
        pass

    def check(self, string: str):
        last = len(string) - 1
        while string[last] == ConstantRegion.EMPTY:
            last -= 1
        if string is None:
            raise WrongFormat("您传入的表达式为null 无法进行计算。")
        elif string[last] not in ConstantRegion.NUMBER_SET:
            raise WrongFormat("您传入的表达式格式有误，最后一个字符不是一个数值！！！")
        # 左括号出现数量
        left: int = 0
        # 右括号出现数量
        right: int = 0
        for c in string[:last]:
            if c == ConstantRegion.LEFT_BRACKET:
                left += 1
            elif c == ConstantRegion.RIGHT_BRACKET:
                right += 1
            elif c not in ConstantRegion.LEGAL_CHARACTERS:
                raise WrongFormat("您的格式不正确，出现了数学表达式中不应该存在的字符。\n"
                                  "Your format is incorrect. There are characters that should not exist in the "
                                  "mathematical expression.\n"
                                  f"Wrong character [{c}] from [{string}]")
        if left != right:
            abs_value = NumberUtils.absolute_value(left - right)
            return WrongFormat(
                f"您的格式不正确，出现了数学表达式中不正确的括号对数，请您检查是否缺少或者多出了[{abs_value}]个括号。\n"
                "Your format is incorrect. There are incorrect parenthesis logarithms in the mathematical "
                "expression. Please check whether [{abs_value}] parentheses are missing or extra.\n "
                f"Wrong from [{string}]"
            )
