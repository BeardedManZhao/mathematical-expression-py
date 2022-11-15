# This is a sample Python script.
from core.calculation.function.Function import Function
from core.calculation.number import functionFormulaCalculation
from core.manager import CalculationManagement


# 实现一个函数
class Function1(Function):
    def run(self, *floats: float):
        return floats[0] * 2


# 将实现的函数注册到管理者
CalculationManagement.register_function(Function1("DoubleValue"))
# 获取到函数计算组件
functionFormulaCalculation = functionFormulaCalculation.get_instance("zhao")
# 构建一个表达式
s = "2 * DoubleValue(2 + 3) + 1"
# 检查表达式格式
functionFormulaCalculation.check(s)
# 开始计算表达式
result = functionFormulaCalculation.calculation(s)
print(
    f"计算层数：{result.get_result_layers()}"
    f"\t计算结果：{result.get_result()}"
    f"\t计算来源：{result.get_calculation_source_name()}"
)

# # 获取到累加公式的计算组件
# cumulativeCalculation = cumulativeCalculation.get_instance("cumulative")
# # Construct a mathematical expression. Here, "n [1,10,1]" is similar to the accumulation symbol in mathematics. N
# # will increase continuously in this interval. Every increase will be brought into the formula for calculation
# # Wherein, the last 1 in [1,10,1] represents the increase step, which can realize the accumulation of different equal
# # difference values in the interval
# s = "n[1,10,1] 2 * (n + 1)"
# # Check mathematical expressions
# cumulativeCalculation.check(s)
# # Calculation results
# calculation = cumulativeCalculation.calculation(s)
# # Print result value
# print(
#     f"计算层数：{calculation.get_result_layers()}"
#     f"\t计算结果：{calculation.get_result()}"
#     f"\t计算来源：{calculation.get_calculation_source_name()}"
# )
# def extracted(boolean_calculation2: BooleanCalculation2, s: str):
#     # Check the expression for errors
#     boolean_calculation2.check(s)
#     # Start calculating results
#     calculation: CalculationBooleanResults = boolean_calculation2.calculation(s)
#     # Print result value
#     print(
#         f"计算层数：{calculation.get_result_layers()}"
#         f"\t计算结果：{calculation.get_result()}"
#         f"\t计算来源：{calculation.get_calculation_source_name()}"
#     )
#
#
# # Get a component that calculates mathematical comparison expressions
# booleanCalculation2: BooleanCalculation2 = booleanCalculation2.get_instance("Bool")
# # Create 3 expressions
# s1 = "1 + 2 + 4 * (10 - 3)"
# s2 = "2 + 30 + (2 * 3) - 1"
# s3 = "1 + 3 * 10"
# extracted(booleanCalculation2, s1 + " > " + s2)  # false
# extracted(booleanCalculation2, s1 + " < " + s2)  # true
# extracted(booleanCalculation2, s1 + " = " + s3)  # true
# extracted(booleanCalculation2, s1 + " == " + s3)  # true
# extracted(booleanCalculation2, s1 + " != " + s3)  # false
# extracted(booleanCalculation2, s1 + " <> " + s3)  # false
# extracted(booleanCalculation2, s1 + " <= " + s3)  # true
# extracted(booleanCalculation2, s1 + " >= " + s3)  # true
# extracted(booleanCalculation2, s1 + " != " + s2)  # true
# extracted(booleanCalculation2, s1 + " <> " + s2)  # true

#
# # 获取一个名称为 zhao1 的嵌套括号表达式计算组件
# zhao1 = bracketsCalculation2.get_instance("zhao1")
# # 构建一个表达式
# s1 = "1 * 2 - (1 + (3 * 2)) + 2 * 3 + 1"
# # 检查该表达式
# zhao1.check(s1)
# # 计算该表达式
# res = zhao1.calculation(s1)
# # 打印结果
# print(res.result)
# #
# # 获取一个名称为bool1的数学比较表达式计算组件
# bool1 = booleanCalculation2.get_instance("bool1")
# # 构建一个表达式
# s1 = "1 + (2 - 3) <> 1 + 2"
# # 检查该表达式
# bool1.check(s1)
# # 计算该表达式
# res = bool1.calculation(s1)
# # 打印结果
# print(res.result)
