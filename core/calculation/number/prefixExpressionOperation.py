# -*- coding: utf-8 -*-
# @Time : 2022/11/12 15:05
# @Author : zhao
# @Email : liming7887@qq.com
# @File : prefixExpressionOperation.py
# @Project : mathematical-expression-py
import re

from core.calculation.number.numberCalculation import NumberCalculation
from core.container.CalculationNumberResults import CalculationNumberResults
from core.manager import CalculationManagement
from exceptional.ExtractException import ExtractException
from exceptional.WrongFormat import WrongFormat
from utils import StrUtils, NumberUtils


class PrefixExpressionOperation(NumberCalculation):
    """
    解析一个无括号的数学计算公式的组件，针对不含括号的计算公式，该组件可以提供计算支持
    Parse a component of mathematical calculation formula without brackets.
    This component can provide calculation support for calculation formula without brackets
    """

    def calculation(self, formula: str, format_param: bool = True):
        """
        计算一个数学表达式，并将计算细节与计算结果存储到数值结果集中。
        Compute a mathematical expression and store the calculation details and results in the numerical result set.
        :param formula: 需要计算的数学公式
        :param format_param:是否需要对公式进行格式化
        :return:数学表达式的计算结果，这里是一个包含数值结果的对象
        """
        if format_param:
            new_formula = self.format_str(formula)
        else:
            new_formula = formula
        # 创建操作数栈
        double_stack: list = []
        # 创建操作符栈
        str_stack: list = []
        # 创建临时字符串容器，用于存储每一个表达式的值
        temp: str = ''
        # 迭代表达式中的每一个字符
        for c in new_formula:
            if c == '+' or c == '-' or c == '*' or c == '/' or c == '%':
                length: int = len(str_stack)
                # 如果是运算符，就将上一个字符串缓冲转换成为数值，稍后用于栈的添加
                number: float = StrUtils.string_to_double(temp)
                # 清理所有缓冲区字符
                temp = ""
                if length == 0:
                    # 如果栈为空，就直接添加
                    double_stack.append(number)
                    str_stack.append(c)
                else:
                    # 如果栈不为空，就使用上一个运算符与当前运算符判断优先级
                    if not NumberUtils.priority_comparison(str_stack[length - 1], c):
                        # 如果当前运算符优先级小，那么就将上一个运算符与上一个数值取出，与当前的数值进行计算，并将运算结果添加到数值栈
                        double_stack.append(NumberUtils.calculation(str_stack.pop(), double_stack.pop(), number))
                        # 将当前运算符添加到栈
                        str_stack.append(c)
                    else:
                        # 如果当前运算符优先级大或相等，那么就直接将当前的值与运算符添加
                        double_stack.append(number)
                        str_stack.append(c)
            elif c == '.' or (c in NumberUtils.NumericalDictionary.keys()):
                # 如果当前是操作数，就直接将当前字符添加到缓冲区
                temp += c
        double_stack.append(StrUtils.string_to_double(temp))
        res: float = double_stack.pop()
        length = len(double_stack)
        # 栈汇总阶段
        i: int = 0
        while i < length:
            # 计算结果
            res = NumberUtils.calculation(str_stack.pop(), double_stack.pop(), res)
            i += 1
        # 返回结果
        return CalculationNumberResults(i, res, self.get_name())

    def check(self, string: str):
        if re.match(".*[()].*", string):
            raise WrongFormat(
                "本组件只能解析不包含括号的表达式！！！\nThis component can only parse expressions without parentheses!!!\nWrong format "
                "=> " + string)
        else:
            super().check(string)

    def format_str(self, string: str) -> str:
        return string.replace(' ', '')


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
        res = PrefixExpressionOperation(name)
        if CalculationManagement.register(res, True):
            return res
        else:
            raise ExtractException("您提取的组件不属于PrefixExpressionOperation，请您更换一个组件名称吧！\n"
                                   "The component you extracted does not belong to PrefixExpressionOperation, "
                                   "please change a component name!\n "
                                   "ERROR NAME => " + name)
