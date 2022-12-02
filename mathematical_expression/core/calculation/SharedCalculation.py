# -*- coding: utf-8 -*-
# @Time : 2022/12/2 17:44
# @Author : zhao
# @Email : liming7887@qq.com
# @File : SharedCalculation.py
# @Project : mathematical-expression-py
from mathematical_expression.core.manager import ConstantRegion


class SharedCalculation:
    """
    共享池计算组件的抽象父类
    """
    startSharedPool: bool = True
    current_owner: str = ConstantRegion.STRING_NULL

    def get_current_owner(self):
        return self.current_owner

    def is_start_shared_pool(self):
        """
        :return: 是否启动了共享池
        """
        return self.startSharedPool

    def set_start_shared_pool(self, st: bool):
        """
        设置共享池是否开启
        :param st: 如果设置为True，代表启动共享池
        """
        self.startSharedPool = st
