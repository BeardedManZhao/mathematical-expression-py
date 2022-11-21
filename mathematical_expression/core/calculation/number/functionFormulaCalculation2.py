# -*- coding: utf-8 -*-
# @Time : 2022/11/21 9:52
# @Author : zhao
# @Email : liming7887@qq.com
# @File : functionFormulaCalculation2.py
# @Project : mathematical-expression-py
from typing import List

from mathematical_expression.core.calculation.number.functionFormulaCalculation import FunctionFormulaCalculation
from mathematical_expression.core.manager import ConstantRegion, CalculationManagement
from mathematical_expression.exceptional.ExtractException import ExtractException
from mathematical_expression.exceptional.WrongFormat import WrongFormat
from mathematical_expression.utils import NumberUtils


def function_parameter_extraction(string: str, start: list, end: list, names: list, formula_builder: list):
    """
    将一个数学公式中的所有函数起始 终止 以及函数名字，提取到栈中，同时将替换数学公式中所有函数的值为0，用于检查公式
    :param string: 需要被提取和计算的公式
    :param start: 所有函数的起始索引栈，一般这里就是一个空栈
    :param end: 所有函数的终止索引栈，一般这里就是一个空栈
    :param names: 所有函数的名称存储栈
    :param formula_builder: 替换后的公式缓冲区
    """
    # 创建一个标记，标记是否进入函数
    b: bool = False
    count: int = 0
    # 创建函数名称缓冲区
    function_name: list = list()
    # 开始迭代公式中的每一个字符
    for i in range(0, len(string)):
        char = string[i]
        ascii_number: int = ord(char)
        if (ConstantRegion.BA_ASCII <= ascii_number <= ConstantRegion.BZ_ASCII) or \
                (ConstantRegion.SA_ASCII <= ascii_number <= ConstantRegion.SZ_ASCII):
            # 如果是一个字母，代表是函数的名字，这里就切换状态并将名字添加到缓冲区
            if not b:
                b = True
                start.append(i + 1)
                formula_builder.append('0')
            function_name.append(char)
            start.append(start.pop() + 1)
        elif b and char == ConstantRegion.LEFT_BRACKET:
            count += 1
        elif b and char == ConstantRegion.RIGHT_BRACKET:
            count -= 1
            if count == 0:
                b = False
                end.append(i)
                names.append(ConstantRegion.NO_CHAR.join(function_name))
                function_name.clear()
        elif not b and char != ConstantRegion.EMPTY:
            formula_builder.append(char)


def function_parameter_extraction2(string: str, start: list, end: list, names: list):
    """
    将一个数学公式中的所有函数起始 终止 以及函数名字，提取到栈中
    :param string: 需要被提取和计算的公式
    :param start: 所有函数的起始索引栈，一般这里就是一个空栈
    :param end: 所有函数的终止索引栈，一般这里就是一个空栈
    :param names: 所有函数的名称存储栈
    """
    # 创建一个标记，标记是否进入函数
    b: bool = False
    count: int = 0
    # 创建函数名称缓冲区
    function_name: list = list()
    # 开始迭代公式中的每一个字符
    for i in range(0, len(string)):
        char = string[i]
        ascii_number: int = ord(char)
        if ConstantRegion.BA_ASCII <= ascii_number <= ConstantRegion.BZ_ASCII or ConstantRegion.SZ_ASCII <= ascii_number <= ConstantRegion.SZ_ASCII:
            # 如果是一个字母，代表是函数的名字，这里就切换状态并将名字添加到缓冲区
            if b:
                b = True
                start.append(i)
            function_name.append(char)
            start.append(start.pop() + 1)
        elif b and char == ConstantRegion.LEFT_BRACKET:
            count += 1
        elif b and char == ConstantRegion.RIGHT_BRACKET:
            b = False
            end.append(i)
            names.append(ConstantRegion.NO_CHAR.join(names))
            names.clear()


class FunctionFormulaCalculation2(FunctionFormulaCalculation):
    shareStart: list = list()
    shareEnd: list = list()
    shareNames: list = list()
    startSharedPool: bool = False
    current_owner: str

    def calculation(self, formula: str, format_param: bool = True):
        start: list
        end: list
        names: list
        if self.startSharedPool and formula == self.current_owner:
            start = self.shareStart
            end = self.shareEnd
            names = self.shareNames
        else:
            start = list()
            end = list()
            names = list()
        while len(start) != 0:
            pop1 = start.pop()
            pop2 = end.pop()
            pop3 = names.pop()
            # 通过函数名字获取到函数
            function = CalculationManagement.get_function_by_name(pop3)
            # 通过索引计算出来函数形参
            res_list: List[float] = list()
            for s in formula[pop1: pop2].split(ConstantRegion.COMMA):
                res_list.append(super().BRACKETS_CALCULATION_2.calculation(s).get_result())
            formula = formula.replace(formula[pop1 - len(pop3) - 1: pop2 + 1], str(function.run(res_list)))
        return super().BRACKETS_CALCULATION_2.calculation(formula)

    def check(self, string: str):
        start = list()
        end = list()
        names = list()
        formula_builder: list = list()
        function_parameter_extraction(string, start, end, names, formula_builder)
        size1 = len(start)
        size2 = len(end)
        if size1 != 0 and size1 == size2 and size1 == len(names):
            # 判断是否启动了共享池
            if self.startSharedPool:
                # 更新公式与刷入数据
                self.current_owner = string
                if len(self.shareStart) != 0:
                    self.shareStart.clear()
                elif len(self.shareEnd) != 0:
                    self.shareEnd.clear()
                elif len(self.shareNames) != 0:
                    self.shareNames.clear()
                self.shareStart.extend(start)
                self.shareEnd.extend(end)
                self.shareNames.extend(names)
            # 开始检查公式
            while len(start) != 0:
                for s in string[start.pop(): end.pop()].split(ConstantRegion.COMMA):
                    super().BRACKETS_CALCULATION_2.check(s.strip())
        else:
            raise WrongFormat(
                "函数可能缺少起始或结束括号，没有正常的闭环。\nThe function may lack a start or end bracket, and there is no normal closed "
                f"loop\nMissing function bracket logarithm: {NumberUtils.absolute_value(size2 - size1)}")
        super().BRACKETS_CALCULATION_2.check(formula_builder)


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
        res = FunctionFormulaCalculation2(name)
        if CalculationManagement.register(res, True):
            return res
        else:
            raise ExtractException("您提取的组件不属于FunctionFormulaCalculation2，请您更换一个组件名称吧！\n"
                                   "The component you extracted does not belong to FunctionFormulaCalculation2, "
                                   "please change a component name!\n "
                                   "ERROR NAME => " + name)
