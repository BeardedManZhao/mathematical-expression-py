# -*- coding: utf-8 -*-
# @Time : 2022/11/12 12:17
# @Author : zhao
# @Email : liming7887@qq.com
# @File : ExtractException.py
# @Project : mathematical_expression-py
class ExtractException(Exception):
    """
    提取计算组件时发生了错误会抛出该异常信息
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()
