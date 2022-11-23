# -*- coding: utf-8 -*-
# @Time : 2022/11/12 15:23
# @Author : zhao
# @Email : liming7887@qq.com
# @File : StrUtils.py
# @Project : mathematical_expression-py
from typing import Optional

from mathematical_expression.core.manager import ConstantRegion
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
        int_size = 0
        float_size = 0
        is_int: bool = True
        for c in string:
            if c != ConstantRegion.DECIMAL_POINT and c != ConstantRegion.EMPTY:
                if is_int:
                    int_res = NumberUtils.tenfold(int_res) + char_to_integer(c)
                    int_size += 1
                else:
                    float_res = NumberUtils.tenfold(float_res) + char_to_integer(c)
                    float_size += 1
            elif c == ConstantRegion.DECIMAL_POINT:
                if not is_int:
                    raise AbnormalOperation(f"数值的浮点符号出现次数过多，无法计算{string}")
                is_int = False
        res = int_res + float_res / NumberUtils.power_of_ten(10, float_size)
        return res if string[0] != ConstantRegion.MINUS_SIGN else -res
    else:
        raise AbnormalOperation("运算出现错误，在进行字符串转数值的时候，字符串的长度为 0，导致错误的发生。")


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
