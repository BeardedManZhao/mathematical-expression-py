# -*- coding: utf-8 -*-
# @Time : 2022/11/12 13:44
# @Author : zhao
# @Email : liming7887@qq.com
# @File : bracketsCalculation2.py
# @Project : mathematical_expression-py
from mathematical_expression.core.calculation.number import prefixExpressionOperation
from mathematical_expression.core.calculation.number.bracketsCalculation import BracketsCalculation
from mathematical_expression.core.container.CalculationNumberResults import CalculationNumberResults
from mathematical_expression.core.manager import CalculationManagement, ConstantRegion
from mathematical_expression.exceptional.ExtractException import ExtractException


class BracketsCalculation2(BracketsCalculation):
    """
    嵌套括号表达式解析组件，该组件可以解析一个带有嵌套括号的数学表达式，计算结果是一个数值，数值与计算过程会在结果对象中被包含
    Nested bracket expression resolution component, which can resolve a mathematical expression with nested brackets.
    The calculation result is a numerical value,
    and the numerical value and calculation process will be included in the result object
    """
    # 括号表达式解析组件所依赖的第三方组件
    PREFIX_EXPRESSION_OPERATION = prefixExpressionOperation.get_instance(
        CalculationManagement.PREFIX_EXPRESSION_OPERATION_NAME
    )

    def calculation(self, formula: str, format_param: bool = True):
        # 公式存储区 这里存储括号被替代之后的数据
        formula_builder: list = []
        # 当前表达式中的括号起始索引位置，在该函数中进行括号内表达式的提取，与递归
        start: int = 0
        # 在当前表达式中是否找到左括号，如果找到就返回true，直到找到右括号再变为false
        set_ok: bool = False
        # 括号内的括号均衡数量，为了确定是一对括号
        count: int = 0
        # 计算层数
        recursion: int = 1
        # 迭代每一个字符
        for i in range(0, len(formula)):
            c = formula[i]
            if c == ConstantRegion.LEFT_BRACKET:
                # 如果是左括号就判断是否需要进行索引的记录
                if not set_ok:
                    # 如果状态为False，代表现在还没有记录括号索引，在这里修改set_ok的状态，同时为start赋予值
                    set_ok = True
                    start = i
                count += 1
            elif c == ConstantRegion.RIGHT_BRACKET:
                count -= 1
                if count == 0:
                    set_ok = False
                    # 如果是右括号，并且是与起始括号相互对应的括号，就将当前位置作为括号内公式的结束索引，开始递归计算括号内部的值，并将结果返回
                    res: CalculationNumberResults = self.calculation(formula[start + 1: i], format_param)
                    formula_builder.append(str(res))
                    recursion += res.result_layers
            elif (not set_ok) and c != ConstantRegion.EMPTY:
                # 如果不是括号就将数据提供给缓冲区
                formula_builder.append(c)
        # 返回结果数据
        return CalculationNumberResults(
            recursion,
            self.PREFIX_EXPRESSION_OPERATION.calculation(''.join(formula_builder), format_param).result,
            self.get_name()
        )


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
        res = BracketsCalculation2(name)
        if CalculationManagement.register(res, True):
            return res
        else:
            raise ExtractException("您提取的组件不属于BracketsCalculation2，请您更换一个组件名称吧！\n"
                                   "The component you extracted does not belong to BracketsCalculation2, "
                                   "please change a component name!\n "
                                   "ERROR NAME => " + name)
