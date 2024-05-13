import mathematical_expression

mathematical_expression.register_function_expression("f(x) = x ^ 2")
c = mathematical_expression.functionFormulaCalculation2.get_instance("zhao")
print(c.calculation("1 + f(1 + 2)"))
