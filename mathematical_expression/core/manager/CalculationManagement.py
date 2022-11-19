# -*- coding: utf-8 -*-
# @Time : 2022/11/12 16:52
# @Author : zhao
# @Email : liming7887@qq.com
# @File : CalculationManagement.py
# @Project : mathematical_expression-py

import logging

from mathematical_expression.core.calculation import Calculation
from mathematical_expression.core.calculation.function.Function import Function
from mathematical_expression.core.manager import ConstantRegion
from mathematical_expression.exceptional.ExtractException import ExtractException

PREFIX_EXPRESSION_OPERATION_NAME: str = "PrefixExpressionOperation"
BRACKETS_CALCULATION_2_NAME: str = "BracketsCalculation2"
STRING_CALCULATION_HASH_MAP: dict = dict()
STRING_FUNCTION_HASH_MAP: dict = dict()


def get_calculation_by_name(calculation_name: str) -> Calculation:
    """
    根据名字，在哈希集合中获取到一个以该名称命名的计算组件
    :param calculation_name: 目标组件的名字
    :return: 目标组件的对象
    """
    logging.info(ConstantRegion.LOG_INFO_GET_COMPONENT + calculation_name)
    return STRING_CALCULATION_HASH_MAP.get(calculation_name)


def get_function_by_name(function_name: str) -> Function:
    """
    根据名字，在哈希集合中获取到一个以该名称命名的函数组件
    :param function_name: 目标函数的名字
    :return: 目标函数的对象
    """
    logging.info(ConstantRegion.LOG_INFO_GET_FUNCTION + function_name)
    function = STRING_FUNCTION_HASH_MAP.get(function_name)
    if function is not None:
        return function
    else:
        raise ExtractException(
            "您想要提取的函数似乎没有被注册到管理者中，请您先使用“register”进行函数的注册！\nIt seems that the function you want to extract has not "
            "been registered with the manager. Please use \"register\" to register the function first!\nERROR "
            "FUNCTION => " + function_name)


def register(calculation: Calculation, judge) -> bool:
    """
    将一个计算组件注册到管理者中，如果注册成功会返回true，不允许重复注册
    Register a calculation component to the administrator. If the registration is successful, true will be returned.
    Repeated registration is not allowed
    :param calculation: 需要被注册的计算组件
    :param judge: 是否在注册之前进行一次该名称已经被使用的判断
    :return: 注册情况，返回True 代表注册成功
    """
    name: str = calculation.get_name()
    if judge and name in STRING_CALCULATION_HASH_MAP.keys():
        logging.warning(
            "An error occurred while registering the component, because the [" + name + "] component has already been "
                                                                                        "registered")
        return False
    else:
        logging.info(ConstantRegion.LOG_INFO_REGISTER_COMPONENT + name)
        STRING_CALCULATION_HASH_MAP[name] = calculation
        return True


def register_function(function: Function) -> bool:
    """
    将一个函数注册到管理者中
    :param function: 需要注册的函数
    :return: 注册是否顺利，如果返回True代表注册成功！
    """
    name = function.get_name()
    if function in STRING_FUNCTION_HASH_MAP:
        logging.warning("An error occurred when registering a function named [" + name + "], because the function "
                                                                                         "name conflicts")
        return False
    else:
        logging.info(ConstantRegion.LOG_INFO_register_FUNCTION + name)
        STRING_FUNCTION_HASH_MAP[name] = function
        return True


def unregister_function(function_name: str):
    """
    注销一个函数的注册，通过函数的名字对函数进行注销
    :param function_name: 需要注销的函数的名称
    :return: 注销成功的函数对象
    """
    logging.info(ConstantRegion.LOG_INFO_UNREGISTER_FUNCTION + function_name)
    return STRING_FUNCTION_HASH_MAP.pop(function_name)


def unregister(calculation_name: str):
    """
    注销一个组件的注册，通过组件的名字对组件进行注销
    :param calculation_name: 需要注销的组件名称
    :return: 注销成功的组件
    """
    logging.info(ConstantRegion.LOG_INFO_UNREGISTER_COMPONENT + calculation_name)
    return STRING_CALCULATION_HASH_MAP.pop(calculation_name)
