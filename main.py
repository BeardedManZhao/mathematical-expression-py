# 导入 mathematical-expression 解析库
import mathematical_expression as mathematical

# 通过库获取到无括号表达式计算组件
prefixExpressionOperation = mathematical.prefixExpressionOperation.get_instance("prefixExpressionOperation")
calculation = prefixExpressionOperation.calculation("2 * -1")
# 打印出第一个表达式的计算结果
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())
