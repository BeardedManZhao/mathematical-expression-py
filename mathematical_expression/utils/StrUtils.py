# -*- coding: utf-8 -*-
# @Time : 2022/11/12 15:23
# @Author : zhao
# @Email : liming7887@qq.com
# @File : StrUtils.py
# @Project : mathematical_expression-py
from typing import Optional

from mathematical_expression.exceptional.AbnormalOperation import AbnormalOperation
from mathematical_expression.utils import NumberUtils


def string_to_double(string: str):
    """
    将一个字符串转换成为一个浮点数值
    :param string: 需要被转换的字符串
    :return: 转换之后的浮点数值
    """
    if len(string) > 0:
        int_res: int = 0
        float_res: int = 0
        is_int: bool = True
        for c in string:
            if c != '.' and c != ' ':
                if is_int:
                    int_res = NumberUtils.tenfold(int_res) + char_to_integer(c)
                else:
                    float_res = NumberUtils.tenfold(float_res) + char_to_integer(c)
            elif c == '.':
                is_int = False
        res = int_res + float_res / NumberUtils.power_of_ten(10, int(0 if float_res == 0 else NumberUtils.divide_ten(
            int(float_res - NumberUtils.divide_ten(float_res))
        )))
        return res if string[0] != '-' else -res
    else:
        raise AbnormalOperation("比较运算出现错误，在进行字符串转数值的时候，字符串的长度为 0，导致错误的发生。")


def char_to_integer(c: str):
    """
    将一个字符转换成为一个数值
    :param c: 需要被转换的字符
    :return: 转换之后的数值
    """
    if len(c) == 1:
        a: Optional[int] = NumberUtils.NumericalDictionary.get(c)
        if a is not None:
            return a
        else:
            raise AbnormalOperation("转换失败，因为这是不属于数值的字符。\n"
                                    "Conversion failed because this is a character that is not a numeric value.\n"
                                    "ERROR => " + c)
    else:
        raise AbnormalOperation("在进行 charToInteger 函数的调用时，您传入的不是一个字符，而是一个字符串，因此发生了错误。\n"
                                "When calling the charToInteger function, you passed in a string instead of a "
                                "character, so an error occurred.\n "
                                "ERROR => " + c)
