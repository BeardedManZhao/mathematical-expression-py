# 导入 mathematical-expression 解析库
import mathematical_expression as mathematical
# 导入需要被实现的函数对象
from mathematical_expression.core.calculation.function.Function import Function


# 实现一个函数
class Function1(Function):
    def run(self, floats: list):
        res1 = 0
        for d in floats:
            res1 += d
        return res1


# 将函数注册
mathematical.register_function(Function1("myFun"))
# 获取到函数计算组件
functionFormulaCalculation2 = mathematical.functionFormulaCalculation2.get_instance("fun")
# 构建需要计算的表达式
s = "1 + myFun(10, 20) * 2"
# 检查计算
functionFormulaCalculation2.check(s)
res = functionFormulaCalculation2.calculation(s)
print(res)
