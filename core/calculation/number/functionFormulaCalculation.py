# -*- coding: utf-8 -*-
# @Time : 2022/11/15 14:08
# @Author : zhao
# @Email : liming7887@qq.com
# @File : functionFormulaCalculation.py
# @Project : mathematical-expression-py
from core.calculation.number import bracketsCalculation2
from core.calculation.number.numberCalculation import NumberCalculation
from core.manager import CalculationManagement
from exceptional.ExtractException import ExtractException
from exceptional.WrongFormat import WrongFormat
from utils import NumberUtils


class FunctionFormulaCalculation(NumberCalculation):
    BRACKETS_CALCULATION_2 = bracketsCalculation2.get_instance(
        CalculationManagement.BRACKETS_CALCULATION_2_NAME
    )

    def calculation(self, formula: str, format_param: bool = True):
        # 创建公式存储区
        string_builder: list = []
        # 创建函数起始点记录变量
        start = 0
        # 创建括号计数器
        count = 0
        # 创建一个布尔变量，记录是否有进入函数
        set_ok = False
        # 创建一个函数名称缓冲区
        name: str = ''
        # 迭代公式找到函数的起始索引值
        for i in range(0, len(formula)):
            a_char: str = formula[i]
            ascii_number = ord(a_char)
            if (65 <= ascii_number <= 90) or (97 <= ascii_number <= 122):
                # 如果是字母，就将当前的索引作为函数名，首先先判断是否为起始索引
                if not set_ok:
                    start = i
                    set_ok = True
                name += a_char
            elif set_ok and a_char == '(':
                # 如果是函数的左括号，就为括号计数器 加1
                count += 1
            elif set_ok and a_char == ')' and count == 1:
                count -= 1
                # 如果当前区域是函数内，同时当前是一个右括号，而且该括号是与起始括号相对应的，代表函数结束
                set_ok = False
                # 获取到函数对象
                function = CalculationManagement.get_function_by_name(name)
                CalculationManagement.logging.info("Find and prepare the startup function: " + name)
                # 使用括号计算组件计算出函数的实参，并将计算结果传递给函数计算，并将结果追加到缓冲区
                string_builder.append(
                    str(function.run(
                        self.BRACKETS_CALCULATION_2.calculation(formula[start + len(name) + 1: i]).result)))
                name = ''
            elif not set_ok and a_char != ' ':
                string_builder.append(a_char)
        # 计算结果
        return self.BRACKETS_CALCULATION_2.calculation(''.join(string_builder), format_param)

    def check(self, string: str):
        # 创建两个栈，用来存储每一个函数的起始与终止索引
        starts: list = []
        ends: list = []
        data: list = []
        # 创建括号计数器
        count = 0
        # 创建一个布尔变量，记录是否有进入函数
        set_ok = False
        # 迭代公式，找到函数起始与终止索引
        for i in range(0, len(string)):
            a_char: str = string[i]
            ascii_number = ord(a_char)
            if (65 <= ascii_number <= 90) or (97 <= ascii_number <= 122):
                # 如果是字母，就将当前的索引作为起始索引
                if not set_ok:
                    starts.append(i)
                    set_ok = True
                starts.append(starts.pop() + 1)
            elif set_ok and a_char == '(':
                count += 1
            elif set_ok and a_char == ')' and count == 1:
                count -= 1
                set_ok = False
                ends.append(i)
            elif not set_ok and a_char != ' ':
                data.append(a_char)
        # 判断起始索引数量与终止索引数量是相同，如果不同代表有错误
        length = len(starts)
        length1 = len(ends)
        if length == length1:
            # 如果没有错误就将所有函数实参的计算公式直接提供给父类检查
            for start in starts:
                super().check(string[start + 2: ends.pop()])
                data.append('0')
            super().check(''.join(data))
        else:
            raise WrongFormat("函数可能缺少起始或结束括号，没有正常的闭环。\nThe function may lack a start or end bracket, and there is no "
                              "normal closed loop\nMissing function bracket logarithm: " +
                              NumberUtils.absolute_value(length - length1))

    def format_str(self, string: str) -> str:
        return string.strip('+-*/%').replace(' ', '')


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
        res = FunctionFormulaCalculation(name)
        if CalculationManagement.register(res, True):
            return res
        else:
            raise ExtractException("您提取的组件不属于FunctionFormulaCalculation，请您更换一个组件名称吧！\n"
                                   "The component you extracted does not belong to FunctionFormulaCalculation, "
                                   "please change a component name!\n "
                                   "ERROR NAME => " + name)
