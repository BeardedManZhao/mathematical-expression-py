# -*- coding: utf-8 -*-
# @Time : 2022/11/12 14:55
# @Author : zhao
# @Email : liming7887@qq.com
# @File : CalculationNumberResults.py
# @Project : mathematical-expression-py
from core.container.CalculationResults import CalculationResults


class CalculationNumberResults(CalculationResults):
    """
    数值计算结果存储对象，在该类中存储的都是来自计算组件的计算结果，以及运算级别层数等信息
    Numerical calculation result storage object. In this class, the calculation results from calculation components,
    as well as the number of operation levels and other information are stored
    """
    result_layers: int
    calculation_source_name: str
    result: float

    def __init__(self, result_layers: int, result: float, calculation_source_name: str):
        """
        构造一个结果对象
        :param result_layers: 已经计算出结果数值的情况下，使用该形参进行赋值
        :param calculation_source_name: 来源，表明该结果对象的计算来源。
        """
        self.result_layers = result_layers
        self.result = result
        self.calculation_source_name = calculation_source_name

    def get_result_layers(self) -> int:
        return self.result_layers

    def get_calculation_source_name(self) -> str:
        return self.calculation_source_name

    def get_result(self) -> float:
        """
        :return: 该类中存储的结果数据
        """
        return self.result

    def __str__(self): return str(self.result)

    def __lt__(self, other):
        """小于"""
        return self.result < other.result

    def __le__(self, other):
        """小于等于"""
        return self.result <= other.result

    def __gt__(self, other):
        """大于"""
        return self.result > other.result

    def __ge__(self, other):
        """大于等于"""
        return self.result >= other.result

    def __eq__(self, other):
        """等于"""
        return self.result == other.result

    def __ne__(self, other):
        """不等于"""
        return self.result != other.result
