# -*- coding: utf-8 -*-
# @Time : 2022/12/24 12:57
# @Author : zhao
# @Email : liming7887@qq.com
# @File : fastMultiplyOfIntervalsBrackets.py
# @Project : mathematical-expression-py
from mathematical_expression.core.calculation.number.fastSumOfIntervalsBrackets import FastSumOfIntervalsBrackets
from mathematical_expression.core.container.CalculationNumberResults import CalculationNumberResults
from mathematical_expression.core.manager import CalculationManagement
from mathematical_expression.exceptional.ExtractException import ExtractException
from mathematical_expression.utils import NumberUtils


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
        res = FastMultiplyOfIntervalsBrackets(name)
        if CalculationManagement.register(res, True):
            return res
        else:
            raise ExtractException("您提取的组件不属于FastMultiplyOfIntervalsBrackets，请您更换一个组件名称吧！\n"
                                   "The component you extracted does not belong to FastMultiplyOfIntervalsBrackets, "
                                   "please change a component name!\n "
                                   "ERROR NAME => " + name)


class FastMultiplyOfIntervalsBrackets(FastSumOfIntervalsBrackets):

    def calculation_by_number_results(self, start: CalculationNumberResults, end: CalculationNumberResults):
        """
        根据区间起始与终止数值结果计算出区间的汇总计算数值
        :param start: 区间起始数值
        :param end: 区间终止数值
        :return: 一个区间内所有元素的累乘数值结果
        """
        return CalculationNumberResults(
            result_layers=start.result_layers + end.result_layers,
            result=NumberUtils.multiply_of_range(start.result, end.result, self.step),
            calculation_source_name=self.get_name()
        )
