# -*- coding: utf-8 -*-
# @Time : 2022/11/12 12:45
# @Author : zhao
# @Email : liming7887@qq.com
# @File : AbnormalOperation.py
# @Project : mathematical-expression-py

class AbnormalOperation(Exception):
    """
    在发生运算异常的时候会排除该异常信息
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()
