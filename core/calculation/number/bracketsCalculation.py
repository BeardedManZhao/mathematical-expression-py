# -*- coding: utf-8 -*-
# @Time : 2022/11/12 13:08
# @Author : zhao
# @Email : liming7887@qq.com
# @File : bracketsCalculation.py
# @Project : mathematical-expression-py

from core.calculation.number.numberCalculation import NumberCalculation


class BracketsCalculation(NumberCalculation):
    """
    括号解析算法计算一个公式的计算组件的父类，其中的计算具体实现是一个抽象，等待实现 The bracket parsing algorithm calculates the parent class of the
    calculation component of a formula, in which the specific implementation of the calculation is an abstract,
    waiting to be implemented
    """

    def format_str(self, string: str) -> str:
        """
        格式化一个公式 使得其可以被该计算组件进行运算，这里是将字符串格式化成为能够被括号解析组件计算的公式 Format a formula so that it can be calculated by the
        calculation component. Here is to format the string into a formula that can be calculated by the bracket
        resolution component
        :param string:需要被格式化的数学公式
        :return:格式化之后的顺序额表达式
        """
        # data: str = ''
        # # 按照括号将所有的公式提取出来
        # split: list = re.split("[()]+", string.replace(" ", ''))
        # # 构建括号偏移量
        # end_b_count: list = []
        # # 迭代每一个字符串，使用正则匹配
        # for s in split:
        #     if re.match("\\d+[+\\-*/]\\d+", s):
        #         # 如果是一个两个操作数一个操作符的公式，就直接将这个公式两边加上括号，提供到结果字符串
        #         data = data.join(['(', s, ')'])
        #     elif re.match("[+\\-*/]\\d+[+\\-*/]\\d+", s):
        #         # 如果是一个运算符和一个两操作数的公式，就直接将公式加括号，提供字符串
        #         data = data.join([s[0], '(', s[1:], ')'])
        #     elif re.match("\\d+[+\\-*/]\\d+[+\\-*/]", s):
        #         # 如果是一个运算符和一个两操作数的公式，就直接将公式加括号，提供字符串
        #         length = len(s)
        #         data = data.join(['(', s[:length], ')', s[length - 1]])
        #     elif re.match("\\d+[+\\-*/]", s):
        #         # 如果是一个运算符和数值，就直接将这个数值的右边加上括号，同时左边由于不知道有什么，所以左边先不加括号，直接计数
        #         data = data.join(['(', s])
        #         end_b_count.append(')')
        #     elif re.match("[+\\-*/]\\d+", s):
        #         # 如果是一个运算符和数值，就直接将这个数值的右边加上括号，同时左边由于不知道有什么，所以左边先不加括号，直接计数
        #         data = data.join([s, ')'])
        #     else:
        #         # 其它情况就直接添加
        #         data = data.join(s)
        # # 最后进行一个结束括号的补充
        # data = data.join(end_b_count)
        # # 返回格式化之后的字符串
        return string.replace(' ', '').strip('+-*/%')
