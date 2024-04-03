# -*- coding: utf-8 -*-
# @Time : 2024/4/3 15:25
# @Author : zhao
# @Email : liming7887@qq.com
# @File : ExpressionFunction.py
# @Project : mathematical-expression-py
import re

from mathematical_expression.core.calculation.function.Function import Function
from mathematical_expression.core.calculation.number.functionFormulaCalculation2 import FunctionFormulaCalculation2
from mathematical_expression.core.manager import ConstantRegion, CalculationManagement
from mathematical_expression.exceptional.UnsupportedOperationException import UnsupportedOperationException
from mathematical_expression.exceptional.WrongFormat import WrongFormat
from mathematical_expression.utils import StrUtils

pattern = re.compile(ConstantRegion.REGULAR_PURE_LETTER + "(?!\\()")


class ExpressionFunction(Function, FunctionFormulaCalculation2):

    def __init__(self, name: str, expression: list[str], param_size: int, index_list: list[int], f: str):
        super().__init__(name)
        self.f = f
        self.expression = expression
        self.paramSize = param_size
        self.indexList = index_list
        # 开始进行检查
        super().check(self.explain([0 for _ in range(0, param_size)]))

    def run(self, numbers):
        return super().calculation(self.explain(numbers), False).get_result()

    def get_name(self) -> str:
        return super().get_name()

    def explain(self, numbers: list) -> str:
        """
        解释计算表达式，我们可以在这里传递一些参数，这些参数将做为函数的输入参数，在这里返回的就是函数带有数值的内部表达式 Explain the calculation expression. We can pass
        some parameters here, which will be used as input parameters for the function. Here, we return the internal
        expression of the function with numerical values
        :param numbers: 这里是函数的数据输入对象，由框架向这里传递数据输入参数
        :return:这里是数据经过函数转换之后的带有参数的表达式数据，用于构建数学表达式的！
        """
        if len(numbers) != self.paramSize:
            raise UnsupportedOperationException(
                f"参数不正确，期望参数数量为：{self.paramSize}，实际参数数量为：{len(numbers)} error => {numbers}")
        stringBuilder = []
        index = 0
        for i in self.indexList:
            stringBuilder.append(self.expression[index])
            index += 1
            stringBuilder.append(str(numbers[i]))
        if len(self.expression) > index:
            stringBuilder.append(self.expression[index])
        return "".join(stringBuilder)

    def __str__(self):
        """
        :return: 当前函数的数学表达式
        """
        return self.f


def parse(expression: str) -> ExpressionFunction:
    """
     解析表达式，得到函数对象
    :param expression: 表达式字符串
    :return:解析出来的函数对象
    """
    #  获取到函数的形参部分 以及 函数的表达式部分
    arraylist: list[str] = expression.split('=')
    if len(arraylist) != 2:
        raise UnsupportedOperationException("您的表达式不属于函数，期望的格式：【函数名】(参数1,参数2) = 数学表达式")
    # 解析函数名
    functionName = None
    params = None
    # 获取参数名
    trim = arraylist[0].strip()
    trim_len = len(trim)
    last_index = trim_len - 1
    now_index = 0
    for c in trim:
        if c == ConstantRegion.LEFT_BRACKET:
            functionName = trim[0:now_index]
            continue
        if c == ConstantRegion.RIGHT_BRACKET:
            if functionName is None:
                raise WindowsError("请您将函数名字写上!!!")
            params = trim[len(functionName) + 1:last_index].split(',')
            for i in range(0, len(params)):
                params[i] = params[i].strip()
        now_index += 1
    # 检查表达式
    string = arraylist[1]
    # 准备表达式容器
    arrayList1 = []
    # 操作数容器
    arrayList2 = []
    backEnd = 0
    if params is not None:
        for match in pattern.finditer(string):
            g = match.group()
            try:
                i = params.index(g)
                sub_string = string[backEnd: match.start()].strip()
                backEnd = match.end()
                arrayList1.append(sub_string)
                arrayList2.append(i)
            except ValueError:
                # 代表没找到元素
                if not StrUtils.is_number(g):
                    # 代表不是数值
                    if match.end() >= len(string):
                        raise WrongFormat("Unknown formal parameter [" + g + "] comes from [" + string + "].")
                    s = g + string[match.end()]
                    if not CalculationManagement.is_function_exist(s):
                        raise WrongFormat(
                            "Unknown formal parameter [" + g + " or " + s + "] comes from [" + string + "].")
        arrayList1.append(string[backEnd:].strip())
    else:
        params = []
    if functionName is None:
        raise WrongFormat("您的函数名提取失败，可能是格式错误，正确的格式示例:sum(a, b)，您的格式：" + trim)
    return ExpressionFunction(functionName, arrayList1, len(params), arrayList2, expression)
