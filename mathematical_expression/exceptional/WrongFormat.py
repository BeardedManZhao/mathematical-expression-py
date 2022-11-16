# -*- coding: utf-8 -*-
# @Time : 2022/11/12 12:25
# @Author : zhao
# @Email : liming7887@qq.com
# @File : WrongFormat.py
# @Project : mathematical_expression-py
class WrongFormat(Exception):
    """
    格式错误，在本框架中进行格式检查的时候，出现了格式类的错误的时候，将会抛出该异常
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()
