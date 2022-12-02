# -*- coding: utf-8 -*-
# @Time : 2022/11/12 12:32
# @Author : zhao
# @Email : liming7887@qq.com
# @File : NumberUtils.py
# @Project : mathematical_expression-py
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


def calculation(calculation_char: str, an: float, bn: float) -> float:
    """
    使用不同的字符，计算两个数值
    :param calculation_char: 运算符
    :param an: 数值1
    :param bn: 数值2
    :return: 数值1与数值2之间进行运算的结果数值，如果运算符错误，则抛出异常
    """
    if calculation_char == ConstantRegion.PLUS_SIGN:
        return an + bn
    elif calculation_char == ConstantRegion.MINUS_SIGN:
        return an - bn
    elif calculation_char == ConstantRegion.MULTIPLICATION_SIGN:
        return an * bn
    elif calculation_char == ConstantRegion.DIVISION_SIGN:
        return an / bn
    elif calculation_char == ConstantRegion.REMAINDER_SIGN:
        return an % bn
    else:
        raise AbnormalOperation(
            "操作数计算异常，您的计算模式不存在，错误的计算模式 = [" + calculation_char + "]\n"
                                                                                        "Operand calculation "
                                                                                        "exception. Your calculation "
                                                                                        "mode does not exist. Wrong "
                                                                                        "calculation mode "
                                                                                        "= [" + calculation_char + "]")


def comparison_operation(calculation_char: str, left: float, right: float) -> bool:
    """
    将两个数值进行比较运算
    :param calculation_char: 比较运算符号
    :param left: 左值
    :param right:右值
    :return:左值 与 右值 之间是否符合比较运算符的关系
            Whether the left value and right value conform to the comparison operator
    """
    if calculation_char == ConstantRegion.GREATER_THAN_SIGN:
        return left > right
    elif calculation_char == ConstantRegion.LESS_THAN_SIGN:
        return left < right
    elif calculation_char == ConstantRegion.GREATER_THAN_OR_EQUAL_TO_SIGN:
        return left >= right
    elif calculation_char == ConstantRegion.LESS_THAN_OR_EQUAL_TO_SIGN:
        return left <= right
    elif calculation_char == ConstantRegion.EQUAL_SIGN1 or calculation_char == ConstantRegion.EQUAL_SIGN2:
        return left == right
    elif calculation_char == ConstantRegion.NOT_EQUAL_SIGN1 or calculation_char == ConstantRegion.NOT_EQUAL_SIGN2:
        return left != right
    else:
        raise AbnormalOperation("无法进行比较运算，因为有错误的运算符。\n"
                                "The comparison operation cannot be performed because there is an incorrect operator.\n"
                                "Bad comparison operator => " + calculation_char)


def sum_of_range(start: float, end: float) -> float:
    if start == end:
        return start
    if float == int(end) and start == int(start):
        return float(int((start + end) * (absolute_value(end - start) + 1)) >> 1)
    else:
        return ((start + end) * (absolute_value(int(end) - int(start)) + 1)) / 2
