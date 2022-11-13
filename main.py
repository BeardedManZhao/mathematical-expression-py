# This is a sample Python script.
from core.calculation.number import bracketsCalculation2

# 获取一个名称为 zhao1 的嵌套括号表达式计算组件
zhao1 = bracketsCalculation2.get_instance("zhao1")
# 构建一个表达式
s1 = "1 * 2 - (1 + (3 * 2)) + 2 * 3 + 1"
# 检查该表达式
zhao1.check(s1)
# 计算该表达式
res = zhao1.calculation(s1)
# 打印结果
print(res.result)
