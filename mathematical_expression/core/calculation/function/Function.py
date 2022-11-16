# -*- coding: utf-8 -*-
# @Time : 2022/11/15 14:05
# @Author : zhao
# @Email : liming7887@qq.com
# @File : Function.py
# @Project : mathematical_expression-py
class Function:
    name: str

    def __init__(self, name: str):
        self.name = name

    def run(self, *floats: float):
        pass

    def get_name(self) -> str:
        return self.name
