# -*- coding: utf-8 -*-
# @Time : 2022/11/12 16:52
# @Author : zhao
# @Email : liming7887@qq.com
# @File : CalculationManagement.py
# @Project : mathematical-expression-py
from core.calculation import Calculation

PREFIX_EXPRESSION_OPERATION_NAME: str = "PrefixExpressionOperation"
BRACKETS_CALCULATION_2_NAME: str = "BracketsCalculation2"
STRING_CALCULATION_HASH_MAP: dict = dict()


def get_calculation_by_name(calculation_name: str) -> Calculation:
    """
    根据名字，在哈希集合中获取到一个以该名称命名的计算组件
    :param calculation_name: 目标组件的名字
    :return: 目标组件的对象
    """
    return STRING_CALCULATION_HASH_MAP.get(calculation_name)


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
        return False
    else:
        STRING_CALCULATION_HASH_MAP[name] = calculation
        return True


def unregister(calculation_name: str):
    """
    注销一个组件的注册，通过组件的名字对组件进行注销
    :param calculation_name: 需要注销的组件名称
    :return: 注销成功的组件
    """
    return STRING_CALCULATION_HASH_MAP.pop(calculation_name)
