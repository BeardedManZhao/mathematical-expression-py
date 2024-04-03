# -*- coding: utf-8 -*-
# @Time : 2024/4/3 15:32
# @Author : zhao
# @Email : liming7887@qq.com
# @File : UnsupportedOperationException.py
# @Project : mathematical-expression-py
class UnsupportedOperationException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()
