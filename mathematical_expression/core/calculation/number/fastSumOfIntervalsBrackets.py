# -*- coding: utf-8 -*-
# @Time : 2022/12/2 17:49
# @Author : zhao
# @Email : liming7887@qq.com
# @File : fastSumOfIntervalsBrackets.py
# @Project : mathematical-expression-py
import logging
from typing import List

from mathematical_expression.core.calculation.SharedCalculation import SharedCalculation
from mathematical_expression.core.calculation.number import bracketsCalculation2
from mathematical_expression.core.calculation.number.bracketsCalculation2 import BracketsCalculation2
from mathematical_expression.core.container.CalculationNumberResults import CalculationNumberResults
from mathematical_expression.core.manager import CalculationManagement, ConstantRegion
from mathematical_expression.exceptional.ExtractException import ExtractException
from mathematical_expression.exceptional.WrongFormat import WrongFormat
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
        res = FastSumOfIntervalsBrackets(name)
        if CalculationManagement.register(res, True):
            return res
        else:
            raise ExtractException("您提取的组件不属于FastSumOfIntervalsBrackets，请您更换一个组件名称吧！\n"
                                   "The component you extracted does not belong to FastSumOfIntervalsBrackets, "
                                   "please change a component name!\n "
                                   "ERROR NAME => " + name)


class FastSumOfIntervalsBrackets(BracketsCalculation2, SharedCalculation):
    """
    快速的将一个等差区间中的所有数值之和计算出来，在该计算组件中的公式由两个组成，例如 "a+b,a+b+10"，会将a+b+1 + a+b+2 + a+b+3 +...+a+b+10 的结果计算出来。
    Quickly calculate the sum of all values in an isochromatic interval.
    The formula in this calculation component consists of two components, such as "a+b, a+b+10".
    The result of a+b+1+a+b+2+a+b+3+...+a+b+10 will be calculated.
    """
    BRACKETS_CALCULATION_2 = bracketsCalculation2.get_instance(
        CalculationManagement.BRACKETS_CALCULATION_2_NAME
    )

    left: str
    right: str
    step: int = 1
    shareNumberCalculation: CalculationNumberResults = None

    def calculation(self, formula: str, format_param: bool = True):
        left_temp: str
        right_temp: str
        # 判断是否需要提取出共享池中的数据
        is_ok = self.startSharedPool and formula == self.current_owner
        if is_ok:
            logging.info(
                ConstantRegion.LOG_INFO_SHARED_POOL + self.get_name() +
                ConstantRegion.DECIMAL_POINT + self.current_owner)
            # 如果共享池开启，同时共享池中数据所属没有错误，就使用共享池数据进行计算
            if self.shareNumberCalculation is not None:
                return self.shareNumberCalculation
            left_temp = self.left
            right_temp = self.right
        else:
            # 其他情况代表共享池不可用
            datas = formula.split(ConstantRegion.COMMA)
            left_temp = datas[0]
            right_temp = datas[1]
        # 开始计算
        calculation_number_results1 = self.BRACKETS_CALCULATION_2.calculation(left_temp)
        if left_temp == right_temp:
            return calculation_number_results1
        calculation_number_results2 = self.BRACKETS_CALCULATION_2.calculation(right_temp)
        calculation_number_results3 = self.calculation_by_number_results(calculation_number_results1,
                                                                         calculation_number_results2)
        if is_ok:
            self.shareNumberCalculation = calculation_number_results3
        return calculation_number_results3

    def format_str(self, string: str) -> str:
        return string.strip()

    def check(self, string: str):
        # 如果启动了共享池，同时还匹配共享池身份，就直接返回，不再检查
        if self.startSharedPool and string == self.get_current_owner():
            return
        # 其他情况需要进行检查 首先获取到前后两个公式
        datas: List[str] = string.split(ConstantRegion.COMMA)
        length = len(datas)
        if length == 2:
            # 如果确认公式是两个，一前一后没有缺失，就直接将两个公式提供给括号组件去检查
            left_temp, right_temp = datas[0], datas[1]
            self.BRACKETS_CALCULATION_2.check(left_temp)
            if left_temp != right_temp:
                self.BRACKETS_CALCULATION_2.check(right_temp)
            # 确定没有问题，就直接将数据提供到共享池（如果开启了共享池的话）
            if self.startSharedPool:
                self.current_owner = string
                self.left = left_temp
                self.right = right_temp
        else:
            raise WrongFormat(
                "区间求和表达式解析错误，在该组件中的表达式，需要两个以逗号分割的表达式组成累加区间中的两个边界值。\n"
                "Error parsing the interval summation expression. The expression in this component needs two "
                "expressions separated by commas to form two boundary values in the cumulative interval."
                "Number of expressions you provide => " + str(length))

    def calculation_by_number_results(self, start: CalculationNumberResults, end: CalculationNumberResults):
        """
        根据区间起始与终止数值结果计算出区间的汇总计算数值
        :param start: 区间起始数值
        :param end: 区间终止数值
        :return: 一个区间内所有元素的累加数值结果
        """
        return CalculationNumberResults(
            result_layers=start.result_layers + end.result_layers,
            result=NumberUtils.sum_of_range(start.result, end.result, self.step),
            calculation_source_name=self.get_name()
        )
