# # 导入 mathematical-expression 解析库
# import mathematical_expression as mathematical
#
# # 构建需要计算的两种表达式
# s1, s2 = "1 + 20 - 2 + 4", "1 + 20 - (2 + 4)"
# # 通过库获取到无括号表达式计算组件
# prefixExpressionOperation = mathematical.prefixExpressionOperation.get_instance("prefixExpressionOperation")
# # 通过库获取到有括号表达式计算组件
# # bracketsCalculation2 = mathematical.bracketsCalculation2.get_instance("bracketsCalculation2")
# # 另一种方式获取到计算组件对象 这种方式更加类似Java中的写法
# bracketsCalculation2 = mathematical.get_instance(mathematical.booleanCalculation2, "bracketsCalculation2")
# # 将第一种公式传递给无括号表达式计算组件检查与计算 该公式也允许传递给有括号表达式计算
# prefixExpressionOperation.check(s1)
# calculation = prefixExpressionOperation.calculation(s1)
# # 打印出第一个表达式的计算结果
# print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
#       "\n计算来源：" + calculation.get_calculation_source_name())
#
# # 将第二种公式传递给有括号表达式计算组件进行检查与计算
# bracketsCalculation2.check(s2)
# calculation2 = bracketsCalculation2.calculation(s2)
# # 打印出第二个表达式的计算结果
# print("计算层数：" + str(calculation2.get_result_layers()) + "\n计算结果：" + str(calculation2.get_result()) +
#       "\n计算来源：" + calculation2.get_calculation_source_name())
