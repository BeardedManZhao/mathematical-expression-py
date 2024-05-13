# -*- coding: utf-8 -*-
# @Time : 2022/11/12 12:32
# @Author : zhao
# @Email : liming7887@qq.com
# @File : NumberUtils.py
# @Project : mathematical_expression-py
import math

from mathematical_expression.core.manager import ConstantRegion
from mathematical_expression.exceptional.AbnormalOperation import AbnormalOperation

NumericalDictionary: dict = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}


def absolute_value(number):
    """
    获取到一个数值的绝对值
    :param number: 需要被转换成为绝对值的数值
    :return: number 的绝对值
    """
    return number if number > 1 else -number


def tenfold(number: int) -> int:
    """
    将一个数值乘10，并返回结果
    :param number: 需要被做十倍乘法的数值
    :return: 数值 * 10
    """
    return (number << 3) + (number << 1)


def divide_ten(number: int) -> float:
    """
    将一个数值除以10，并返回结果
    :param number: 需要被做十倍除法的数值
    :return: 数值 / 10
    """
    return (number >> 1) / 5


def power_of_ten(number: int, n: int) -> int:
    """
    将一个数值乘以10的n次方
    :param number 需要被做乘法的数值
    :param n 次方数量
    :return: number 乘以10的 n 次方结果数值
    """
    res: int = number
    for i in range(1, n):
        res = tenfold(res)
    return res


def priority_comparison(c1: str, c2: str):
    """
    将两个运算符的优先级进行比较
    :param c1: 运算符1
    :param c2: 运算符2
    :return: 运算符1的优先级如果小于运算符2，那么该函数返回True
    """
    return (c1 == ConstantRegion.PLUS_SIGN or c1 == ConstantRegion.MINUS_SIGN) and \
           (c2 == ConstantRegion.MULTIPLICATION_SIGN or c2 == ConstantRegion.DIVISION_SIGN or
            c2 == ConstantRegion.REMAINDER_SIGN)


# 计算函数 每个操作符都对应了一个计算函数
calculation_function = {
    ConstantRegion.PLUS_SIGN: lambda an, bn: an + bn,
    ConstantRegion.MINUS_SIGN: lambda an, bn: an - bn,
    ConstantRegion.MULTIPLICATION_SIGN: lambda an, bn: an * bn,
    ConstantRegion.DIVISION_SIGN: lambda an, bn: an / bn,
    ConstantRegion.REMAINDER_SIGN: lambda an, bn: an % bn,
    ConstantRegion.POW_SIGN: lambda an, bn: math.pow(an, bn),
}


def calculation(calculation_char: str, an: float, bn: float) -> float:
    """
    使用不同的字符，计算两个数值
    :param calculation_char: 运算符
    :param an: 数值1
    :param bn: 数值2
    :return: 数值1与数值2之间进行运算的结果数值，如果运算符错误，则抛出异常
    """
    if calculation_char in calculation_function:
        return calculation_function[calculation_char](an, bn)
    else:
        raise AbnormalOperation(
            "操作数计算异常，您的计算模式不存在，错误的计算模式 = [" + calculation_char +
            "]\nOperand calculation "
            "exception. Your calculation "
            "mode does not exist. Wrong "
            "calculation mode "
            "= [" + calculation_char + "]")


# 比较函数 每个操作符都对应了一个比较操作
comparison_function = {
    ConstantRegion.GREATER_THAN_SIGN: lambda left, r: left > r,
    ConstantRegion.LESS_THAN_SIGN: lambda left, r: left < r,
    ConstantRegion.GREATER_THAN_OR_EQUAL_TO_SIGN: lambda left, r: left >= r,
    ConstantRegion.LESS_THAN_OR_EQUAL_TO_SIGN: lambda left, r: left <= r,
    ConstantRegion.EQUAL_SIGN1: lambda left, r: left == r,
    ConstantRegion.EQUAL_SIGN2: lambda left, r: left == r,
    ConstantRegion.NOT_EQUAL_SIGN1: lambda left, r: left != r,
    ConstantRegion.NOT_EQUAL_SIGN2: lambda left, r: left != r,
}


def comparison_operation(calculation_char: str, left: float, right: float) -> bool:
    """
    将两个数值进行比较运算
    :param calculation_char: 比较运算符号
    :param left: 左值
    :param right:右值
    :return:左值 与 右值 之间是否符合比较运算符的关系
            Whether the left value and right value conform to the comparison operator
    """
    if calculation_char in comparison_function:
        return comparison_function[calculation_char](left, right)
    else:
        raise AbnormalOperation("无法进行比较运算，因为有错误的运算符。\n"
                                "The comparison operation cannot be performed because there is an incorrect operator.\n"
                                "Bad comparison operator => " + calculation_char)


def sum_of_range(start: float, end: float, step=1) -> float:
    """
    计算一个区间内所有数值的累加结果数值
    :param step: 累加区间的区间元素步长
    :param start: 区间的左起始区间
    :param end: 区间的右终止区间
    :return: 区间内所有数值的累加数值结果
    """
    if start == end:
        return start
    if step == 1:
        if float == int(end) and start == int(start):
            return float(int((start + end) * (absolute_value(end - start) + 1)) >> 1)
        else:
            return ((start + end) * (absolute_value(int(end) - int(start)) + 1)) / 2
    else:
        abs_value = absolute_value(end - start)
        end -= abs_value % step
        abs_value = absolute_value(end - start)
        n = 1 + (abs_value / step)
        return n * start + n * (n - 1) * (max(step, 2)) / 2


def multiply_of_range(start: float, end: float, step: float):
    """
    计算一个区间内所有数值的累乘结果数值
    :param start: 区间内左起始区间
    :param end: 区间内右终止区间
    :param step: 区间内元素之间的步长
    :return: 区间内所有数值的累乘结果数值
    """
    if start == end:
        return start
    else:
        res: float = start
        temp = start + step
        while temp <= end:
            res *= temp
            temp += step
        return res
