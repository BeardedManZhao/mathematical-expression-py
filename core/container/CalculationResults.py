# -*- coding: utf-8 -*-
# @Time : 2022/11/12 12:52
# @Author : zhao
# @Email : liming7887@qq.com
# @File : CalculationResults.py
# @Project : mathematical-expression-py
class CalculationResults:
    """
    计算结果接口，其中一般用来存储有关计算结果的数据，结果数据不一定是一个数值，具体的操作请查阅子类实现

    Calculation result interface, which is generally used to store
    data related to calculation results. The result data may not be a numerical value. Please refer to the subclass
    implementation for specific operations
    """

    def get_result_layers(self):
        """
        计算结果中是经历了很多层计算才获得到的，这个函数可以获取到计算结果的层数量，也可以说是计算结果的计算次数。 The calculation result is obtained after many layers of
        calculation. This function can obtain the number of layers of the calculation result, or the number of
        calculations of the calculation result.
        :return: 计算出这个结果，共计算了约多少层公式
        """
        pass

    def get_calculation_source_name(self):
        """
        结果是被计算组件计算出来的，在这里可以查询到计算该结果的组件名称，需要注意的是，这里返回的名称不会随着管理者中注册表的更改而变化

        The result is calculated by the calculation component. You can query the name of the component that calculates the result here. Note that the name returned here will not change with the change of the registry in the administrator
        :return: 是哪个计算组件将这个结果计算出来的
        """
        pass
