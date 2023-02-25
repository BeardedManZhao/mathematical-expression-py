# -*- coding: utf-8 -*-
# @Time : 2022/11/19 9:23
# @Author : zhao
# @Email : liming7887@qq.com
# @File : ConstantRegion.py
# @Project : mathematical-expression-py
# 这里是框架的常量数据池，不建议更改，如果更改了的话，很可能造成运行混乱
# 如果针对具有固定格式要求的数学公式需要对此处的参数进行配置，请在修改之后进行re_fresh函数的调用
import logging
from typing import List

VERSION: float = 1.2
STRING_NULL: str = "null"
LEFT_BRACKET: str = '('
RIGHT_BRACKET: str = ')'
DECIMAL_POINT: str = '.'
EMPTY: str = ' '
NO_CHAR: str = ''
COMMA = ','
BA_ASCII: int = 0b1000001
BZ_ASCII: int = 0b1011010
SA_ASCII: int = 0b1100001
SZ_ASCII: int = 0b1111010
PLUS_SIGN: str = '+'
MINUS_SIGN: str = '-'
MULTIPLICATION_SIGN: str = '*'
DIVISION_SIGN: str = '/'
REMAINDER_SIGN: str = '%'
GREATER_THAN_SIGN: str = ">"
LESS_THAN_SIGN: str = "<"
EQUAL_SIGN1: str = "="
EQUAL_SIGN2: str = EQUAL_SIGN1 + EQUAL_SIGN1
NEGATE_SIGN: str = "!"
NOT_EQUAL_SIGN1: str = NEGATE_SIGN + EQUAL_SIGN1
NOT_EQUAL_SIGN2: str = LESS_THAN_SIGN + GREATER_THAN_SIGN
GREATER_THAN_OR_EQUAL_TO_SIGN: str = GREATER_THAN_SIGN + EQUAL_SIGN1
LESS_THAN_OR_EQUAL_TO_SIGN: str = LESS_THAN_SIGN + EQUAL_SIGN1
REGULAR_COMPARISON_OPERATOR: str = "{0}|{1}|{2}|{3}|{4}|[{5}{6}{7}]".format(LESS_THAN_OR_EQUAL_TO_SIGN,
                                                                            GREATER_THAN_OR_EQUAL_TO_SIGN,
                                                                            NOT_EQUAL_SIGN1, NOT_EQUAL_SIGN2,
                                                                            EQUAL_SIGN2, LESS_THAN_SIGN,
                                                                            EQUAL_SIGN1,
                                                                            GREATER_THAN_SIGN)
REGULAR_PURE_LETTER: str = "[a-zA-Z]+"
LOG_INFO_GET_FUNCTION: str = "Get a function component from the manager. => "
LOG_INFO_GET_COMPONENT: str = "Get a computing component from the manager. => "
LOG_INFO_FIND_FUNCTION: str = "Find and prepare the startup function: "
LOG_INFO_REGISTER_COMPONENT: str = "A computing component is registered "
LOG_INFO_register_FUNCTION: str = "A function is registered "
LOG_INFO_UNREGISTER_COMPONENT: str = "Preparing to unregister the compute component. Component name:"
LOG_INFO_UNREGISTER_FUNCTION: str = "Prepare the logoff of a function. Function name:"
LOG_INFO_SHARED_POOL: str = "Use shared pool data. The identity of the data is: "
# python特有的常量数据
LOG_LEVEL: int = logging.INFO
REGULAR_CONTAINS_ADDSUB: str = "\\+" + MINUS_SIGN + "|" + MINUS_SIGN + "\\+" \
    if PLUS_SIGN == '+' else \
    PLUS_SIGN + MINUS_SIGN + '|' + MINUS_SIGN + PLUS_SIGN
ARITHMETIC_OPERATOR_STRING: str = PLUS_SIGN.join([MINUS_SIGN, MULTIPLICATION_SIGN, DIVISION_SIGN, REMAINDER_SIGN])

NUMBER_SET: List[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', RIGHT_BRACKET]

LEGAL_CHARACTERS: set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                         EMPTY, PLUS_SIGN, MINUS_SIGN,
                         MULTIPLICATION_SIGN, DIVISION_SIGN,
                         REMAINDER_SIGN,
                         LEFT_BRACKET, RIGHT_BRACKET, DECIMAL_POINT}


def re_fresh():
    """
    刷新常量配置
    """
    global REGULAR_CONTAINS_ADDSUB, ARITHMETIC_OPERATOR_STRING, EQUAL_SIGN2, NOT_EQUAL_SIGN1, NOT_EQUAL_SIGN2
    global GREATER_THAN_OR_EQUAL_TO_SIGN, LESS_THAN_OR_EQUAL_TO_SIGN
    global REGULAR_COMPARISON_OPERATOR, LEGAL_CHARACTERS
    REGULAR_CONTAINS_ADDSUB = "\\+" + MINUS_SIGN + "|" + MINUS_SIGN + "\\+" \
        if PLUS_SIGN == '+' else \
        PLUS_SIGN + MINUS_SIGN + '|' + MINUS_SIGN + PLUS_SIGN
    ARITHMETIC_OPERATOR_STRING = PLUS_SIGN.join([MINUS_SIGN, MULTIPLICATION_SIGN, DIVISION_SIGN, REMAINDER_SIGN])
    EQUAL_SIGN2 = EQUAL_SIGN1 + EQUAL_SIGN1
    NOT_EQUAL_SIGN1 = NEGATE_SIGN + EQUAL_SIGN1
    NOT_EQUAL_SIGN2 = LESS_THAN_SIGN + GREATER_THAN_SIGN
    GREATER_THAN_OR_EQUAL_TO_SIGN = GREATER_THAN_SIGN + EQUAL_SIGN1
    LESS_THAN_OR_EQUAL_TO_SIGN = LESS_THAN_SIGN + EQUAL_SIGN1
    REGULAR_COMPARISON_OPERATOR = "{0}|{1}|{2}|{3}|{4}|[{5}{6}{7}]".format(LESS_THAN_OR_EQUAL_TO_SIGN,
                                                                           GREATER_THAN_OR_EQUAL_TO_SIGN,
                                                                           NOT_EQUAL_SIGN1, NOT_EQUAL_SIGN2,
                                                                           EQUAL_SIGN2, LESS_THAN_SIGN,
                                                                           EQUAL_SIGN1,
                                                                           GREATER_THAN_SIGN)
    LEGAL_CHARACTERS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        EMPTY, PLUS_SIGN, MINUS_SIGN,
                        MULTIPLICATION_SIGN, DIVISION_SIGN,
                        REMAINDER_SIGN,
                        LEFT_BRACKET, RIGHT_BRACKET, DECIMAL_POINT}
