![logo](https://private-user-images.githubusercontent.com/113756063/348286406-cbf100a1-93c3-4842-80e6-776582d9a761.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI5MTQ2MzAsIm5iZiI6MTcyMjkxNDMzMCwicGF0aCI6Ii8xMTM3NTYwNjMvMzQ4Mjg2NDA2LWNiZjEwMGExLTkzYzMtNDg0Mi04MGU2LTc3NjU4MmQ5YTc2MS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODA2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgwNlQwMzE4NTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xY2EzOTNiYWMyNGY4N2E5NDUzZDAyMDY2NzEyMjc1N2Q3MTE0YjUzYWNjZGU3OTJmYWEzNmRhZTY3ODNiYzIyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.UEMOmmwjKUw33-79NdQQr3sgCitGTzhC2DMvixaq5WM)

# mathematical-expression-py

- 切换至 [中文文档](https://github.com/BeardedManZhao/mathematical-expression-py/blob/main/README-Chinese.md)

## introduce

This framework is an effective tool for mathematical formula analysis. It can analyze mathematical formulas including
nested functions, including functions, and step accumulation of series. The return value is a numerical result object.
At the same time, it can also be used for comparison operations. When comparing again, the return value is a Boolean
result object.

- pip Get Command

```shell
pip install mathematical-expression-py
```

## Framework

### Use mathematical_ Expression package

After version 1.2, the use of mathematical is supported_ The expression package obtains various computing components to
reduce the amount of code and the difficulty of library calls.

```python
# import mathematical expression parsing library
import mathematical_expression as mathematical

# Build two expressions to be evaluated
s1, s2 = "1 + 20 - 2 + 4", "1 + 20 - (2 + 4)"
# Obtaining an expression evaluation component without parentheses through the library
prefixExpressionOperation = mathematical.prefixExpressionOperation.get_instance("prefixExpressionOperation")
# Obtain the bracketed expression calculation component through the library
bracketsCalculation2 = mathematical.bracketsCalculation2.get_instance("bracketsCalculation2")
# Another way is to get the calculation component object, which is more similar to the writing method in Java
# bracketsCalculation2 = mathematical.get_instance(mathematical.booleanCalculation2, "bracketsCalculation2")

# Pass the first formula to the parenthesis expression calculation component Check and calculate the formula can also be passed to the parenthesis expression calculation
prefixExpressionOperation.check(s1)
calculation = prefixExpressionOperation.calculation(s1)
# Print the calculation result of the first expression
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())

# Pass the second formula to the bracketed expression calculation component for check and calculation
bracketsCalculation2.check(s2)
calculation2 = bracketsCalculation2.calculation(s2)
# Print the calculation result of the second expression
print("计算层数：" + str(calculation2.get_result_layers()) + "\n计算结果：" + str(calculation2.get_result()) +
      "\n计算来源：" + calculation2.get_calculation_source_name())
```

- Running results
  The module objects of each calculation component can be obtained by importing the package, which can effectively
  reduce the package guide code.

```
计算层数：1
计算结果：23.0
计算来源：prefixExpressionOperation
计算层数：2
计算结果：15.0
计算来源：bracketsCalculation2
```

### Calculation Manager

- Full class name：mathematical_expression/core/manager/CalculationManagement.py
- introduce：

  The manager is a component designed to use both singletons and dynamic objects. The existence of the manager enables
  each component to be obtained by name. Components with the same name have the same storage address in memory, avoiding
  the use of redundant components. At the same time, for components that need to use dynamic members, a new component
  can also be obtained by a new name.
- API Usage Example

```python
from mathematical_expression.core.calculation.number import bracketsCalculation2, functionFormulaCalculation
from mathematical_expression.core.manager import CalculationManagement

# Create two parenthesis expression parsing components and a function expression parsing component
br1 = bracketsCalculation2.get_instance("br1")
br2 = bracketsCalculation2.get_instance("br2")
fu1 = functionFormulaCalculation.get_instance("fu1")
# Get the components with these three names from the manager
m_br1 = CalculationManagement.get_calculation_by_name("br1")
m_br2 = CalculationManagement.get_calculation_by_name("br2")
m_fu1 = CalculationManagement.get_calculation_by_name("fu1")
# Through get_ Instance and the manager extract the components obtained by these two methods. In the case of the same name, the two are one object
print(br1 == m_br1)
print(br2 == m_br2)
print(fu1 == m_fu1)
print(br1 == br2)
```

- Running results

  The last three lines are the comparison of memory data. The instantiated components are the same as the components in
  the manager, but the components with different names are different.

```
INFO:root:+============================== Welcome to [mathematical expression] ==============================+
INFO:root:+ 	Start time 2022-11-16 16:29:07.660044
INFO:root:+ 	Calculation component manager initialized successfully
INFO:root:+ 	For more information, see: https://github.com/BeardedManZhao/mathematical-expression-py
INFO:root:+--------------------------------------------------------------------------------------------------+
INFO:root:A computing component is registered PrefixExpressionOperation
INFO:root:A computing component is registered BracketsCalculation2
INFO:root:A computing component is registered br1
INFO:root:A computing component is registered br2
INFO:root:A computing component is registered fu1
True
True
True
False
```

### Operational rule redefinition

- Full class name：mathematical_expression/core/manager/ConstantRegion.py
- introduce：

  There is a constant pool in the framework that stores data that needs to be reused frequently. This data can be
  modified in the python version of the framework. Modifying this data can often add more flexibility, but it is
  important to note that the modification here may also cause some strange exceptions, so it is up to you to decide if
  you want to use redefinition technology.

  Next, see an example of using redefinition

```python
# This is a sample Python script.
from mathematical_expression.core.calculation.number import bracketsCalculation2
from mathematical_expression.core.calculation.number.bracketsCalculation2 import BracketsCalculation2
from mathematical_expression.core.container.CalculationNumberResults import CalculationNumberResults
from mathematical_expression.core.manager import ConstantRegion

# Redefine the sign of the plus sign
ConstantRegion.PLUS_SIGN = '$'
# Redefine the sign of the multiplication sign
ConstantRegion.MULTIPLICATION_SIGN = '@'
# Refresh constant area configuration
ConstantRegion.re_fresh()

# Get a calculation component that evaluates nested parenthesis expressions
bracketsCalculation2: BracketsCalculation2 = bracketsCalculation2.get_instance("BracketsCalculation")
# Create an expression
# s: str = "1 + 2 + 4 * (10 - 3)" 
# TODO The plus sign and multiplication sign here are redefined and can be replaced by new characters
s: str = "1 $ 2 $ 4 @ (10 - 3)"
# Check the expression for errors
bracketsCalculation2.check(s)
# Start calculating results
calculation: CalculationNumberResults = bracketsCalculation2.calculation(s)
# Print result value
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())

```

- Running results

  It can be seen that the operation here is smooth. In the formula, the symbol is redefined

```
计算层数：2
计算结果：31.0
计算来源：BracketsCalculation
```

## Calculation component introduce

### Bracketed expression

- Full class name：mathematical_expression/core/calculation/number/prefixExpressionOperation.py
- introduce

  This component is designed for a mathematical expression without parentheses, but with operations such as addition,
  subtraction, multiplication, division and remainder. This component can realize the function with priority
  calculation, in which the prefix expression is used to parse and calculate, and the operand and operator are stored on
  the stack together with the calculation priority comparison If the current priority is low, first operate the previous
  operand and operator with the current operand to form a new value, and then put it on the stack.
- API Usage Example

  The operators supported by this component are： `a+b` `a-b` `a*b` `a/b` `a%b` `a^b`

```python
# This is a sample Python script.
from mathematical_expression.core.calculation.number import prefixExpressionOperation
from mathematical_expression.core.calculation.number.prefixExpressionOperation import PrefixExpressionOperation
from mathematical_expression.core.container.CalculationNumberResults import CalculationNumberResults

# Gets the calculation component of a function that evaluates an expression without parentheses
prefixExpressionOperation: PrefixExpressionOperation = prefixExpressionOperation.get_instance("p")
# Create an expression
s: str = "1 + 2 + 4 * 10 - 3"
# Check the expression for errors
prefixExpressionOperation.check(s)
# Start calculating results
calculation: CalculationNumberResults = prefixExpressionOperation.calculation(s)
# Print result value
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())
```

- Running results

  In the API call, the Running results of the function are printed. It can be seen that the returned value calculated by
  the component is a result set object, in which a lot of information about the calculation results is stored.

```
计算层数：2
计算结果：40.0
计算来源：p
```

### Nested parenthesis expression

- Full class name：core/calculation/number/bracketsCalculation2.py
- introduce：

  Nested parenthesis expression parsing component, which can parse and calculate the results of mathematical expressions
  with multiple parentheses, and parse and calculate the priority of nested parentheses. This component relies on "core.
  calculation. number. PrefixExpressionOperation", and uses recursion to parse parentheses in this component, Then
  provide the innermost expression to "core. calculation. number. PrefixExpressionOperation" for calculation.

- API Usage Example

  The operators supported by this component are： a+b a-b a*b a/b a%b ( )

```python
# This is a sample Python script.
from mathematical_expression.core.calculation.number import bracketsCalculation2
from mathematical_expression.core.calculation.number.bracketsCalculation2 import BracketsCalculation2
from mathematical_expression.core.container.CalculationNumberResults import CalculationNumberResults

# Get a calculation component that evaluates nested parenthesis expressions
bracketsCalculation2: BracketsCalculation2 = bracketsCalculation2.get_instance("BracketsCalculation")
# Create an expression
s: str = "1 + 2 + 4 * (10 - 3)"
# Check the expression for errors
bracketsCalculation2.check(s)
# Start calculating results
calculation: CalculationNumberResults = bracketsCalculation2.calculation(s)
# Print result value
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())
```

- Running results

  In the API call, the calculation result of the expression is printed. It can be seen that the return value of the
  component calculation is a numerical result object, in which a lot of information about the calculation result is
  stored.

```
计算层数：2
计算结果：31.0
计算来源：BracketsCalculation
```

### Mathematical comparison expression

- Full class name：core/calculation/bool/booleanCalculation2.py
- introduce

  A component that uses the comparison operator to determine whether two parenthesis expressions are mutually valid. The
  return value is a Boolean result object. This component can compare the size of two numeric values, or the
  relationship between two expressions, depending on the component "core. calculation. bool. BooleanCalculation2"
- API Usage Example

  The operators supported by this component are shown in the API

```python
# This is a sample Python script.
from mathematical_expression.core.calculation.bool import booleanCalculation2
from mathematical_expression.core.calculation.bool.booleanCalculation2 import BooleanCalculation2
from mathematical_expression.core.container.CalculationBooleanResults import CalculationBooleanResults


def extracted(boolean_calculation2: BooleanCalculation2, s: str):
    # Check the expression for errors
    boolean_calculation2.check(s)
    # Start calculating results
    calculation: CalculationBooleanResults = boolean_calculation2.calculation(s)
    # Print result value
    print(
        f"计算层数：{calculation.get_result_layers()}"
        f"\t计算结果：{calculation.get_result()}"
        f"\t计算来源：{calculation.get_calculation_source_name()}"
    )


# Get a component that calculates mathematical comparison expressions
booleanCalculation2: BooleanCalculation2 = booleanCalculation2.get_instance("Bool")
# Create 3 expressions
s1 = "1 + 2 + 4 * (10 - 3)"
s2 = "2 + 30 + (2 * 3) - 1"
s3 = "1 + 3 * 10"
extracted(booleanCalculation2, s1 + " > " + s2)  # false
extracted(booleanCalculation2, s1 + " < " + s2)  # true
extracted(booleanCalculation2, s1 + " = " + s3)  # true
extracted(booleanCalculation2, s1 + " == " + s3)  # true
extracted(booleanCalculation2, s1 + " != " + s3)  # false
extracted(booleanCalculation2, s1 + " <> " + s3)  # false
extracted(booleanCalculation2, s1 + " <= " + s3)  # true
extracted(booleanCalculation2, s1 + " >= " + s3)  # true
extracted(booleanCalculation2, s1 + " != " + s2)  # true
extracted(booleanCalculation2, s1 + " <> " + s2)  # true
```

- Running results

```
计算层数：4	计算结果：False	计算来源：Bool
计算层数：4	计算结果：True	计算来源：Bool
计算层数：3	计算结果：True	计算来源：Bool
计算层数：3	计算结果：True	计算来源：Bool
计算层数：3	计算结果：False	计算来源：Bool
计算层数：3	计算结果：False	计算来源：Bool
计算层数：3	计算结果：True	计算来源：Bool
计算层数：3	计算结果：True	计算来源：Bool
计算层数：4	计算结果：True	计算来源：Bool
计算层数：4	计算结果：True	计算来源：Bool
```

### Interval accumulation expression

- Full class name：core/calculation/number/cumulativeCalculation.py

- introduce

In mathematical expressions, there is often such a formula. The content of the formula is shown in the following

figure. You can see the number sequence operations that need to be accumulated.

Then, you can use the Full class name above to achieve the purpose you need.

![img_1](https://user-images.githubusercontent.com/113756063/201575828-5b76af88-6040-430d-a54c-61faf5905594.png)

- API Usage Example

The syntax level is almost the same as that of other components. The calculation example of the mathematical

expression written in the component is shown below. What is shown here is the calculation of an accumulative

mathematical formula.

```python
# This is a sample Python script.
from mathematical_expression.core.calculation.number import cumulativeCalculation

# Get the calculation component of the accumulation formula
cumulativeCalculation = cumulativeCalculation.get_instance("cumulative")
# Construct a mathematical expression. Here, "n [1,10,1]" is similar to the accumulation symbol in mathematics. N
# will increase continuously in this interval. Every increase will be brought into the formula for calculation
# Wherein, the last 1 in [1,10,1] represents the increase step, which can realize the accumulation of different equal
# difference values in the interval
s = "n[1,10,1] 2 * (n + 1)"
# Check mathematical expressions
cumulativeCalculation.check(s)
# Calculation results
calculation = cumulativeCalculation.calculation(s)
# Print result value
print(
    f"计算层数：{calculation.get_result_layers()}"
    f"\t计算结果：{calculation.get_result()}"
    f"\t计算来源：{calculation.get_calculation_source_name()}"
)
```

- Running results

```
计算层数：21	计算结果：130.0	计算来源：cumulative
```

### Function operation expression

- Full class name:core/calculation/number/functionFormulaCalculation.py

- introduce

  The framework also supports the operation of some functions. You can use the above classes to write mathematical
  expressions that require functions. It should be noted that all functions used in expressions need to be logically
  registered in "Calculation Management" so that functions can be accessed during calculation
- API Usage Example

```python
# This is a sample Python script.
from mathematical_expression.core.calculation.function.Function import Function
from mathematical_expression.core.calculation.number import functionFormulaCalculation
from mathematical_expression.core.manager import CalculationManagement


# 实现一个函数
class Function1(Function):
    def run(self, *floats: float):
        return floats[0] * 2


# Register the implemented function to the manager
CalculationManagement.register_function(Function1("DoubleValue"))
# Get the function calculation component
functionFormulaCalculation = functionFormulaCalculation.get_instance("zhao")
# Build an expression
s = "2 * DoubleValue(2 + 3) + 1"
# Check expression format
functionFormulaCalculation.check(s)
# Start evaluating expression
result = functionFormulaCalculation.calculation(s)
print(
    f"计算层数：{result.get_result_layers()}"
    f"\t计算结果：{result.get_result()}"
    f"\t计算来源：{result.get_calculation_source_name()}"
)
```

- Running results

```
INFO:root:Find and prepare the startup function: DoubleValue
计算层数：1	计算结果：21.0	计算来源：BracketsCalculation2
```

### Multi parameter function operation expression

- Full class name: mathematical_expression/core/calculation/number/functionFormulaCalculation2.py
- introduce

  For some expression calculations that use functions in expressions, the above class can be used for operations. It is
  an upgraded version of the "core. calculation. number. FunctionFormulaCalculation" class, which has appeared since
  version 1.1, is also an extended implementation of its subclass.

  Compared with the parent class, this component makes up for the deficiency that the parent class can only parse the
  function expression with one parameter. In this component, you can use many real parameters for function operations,
  such as sum (1,2,3)

  This type of function is a multiparameter function. Next, let's look at the API usage example, in which the
  calculation and results of the multiparameter function expression are shown.

```python
from mathematical_expression.core.calculation.function.Function import Function
from mathematical_expression.core.calculation.number import functionFormulaCalculation2
from mathematical_expression.core.manager import CalculationManagement


# Implement a function
class Sum(Function):
    def run(self, floats: list):
        res = 0
        for d in floats:
            res += d
        return res


# Start to create the function and register it with the manager
CalculationManagement.register_function(Sum("sum"))
# Get the calculation component that can parse the mathematical expression of multi parameter function
functionFormulaCalculation2 = functionFormulaCalculation2.get_instance("zhao")
# Enable shared pool
functionFormulaCalculation2.startSharedPool = True
# Build the mathematical expression to be calculated 
# TODO More than one function parameter is used in the following mathematical expression
s = "2 * (200 - sum(1 + 10.1, 2, 3)) + sum(10, 20)"
# Check the mathematical expression for errors
functionFormulaCalculation2.check(s)
# Calculate the expression and get the result
result = functionFormulaCalculation2.calculation(s)
print(
    f"计算层数：{result.get_result_layers()}"
    f"\t计算结果：{result.get_result()}"
    f"\t计算来源：{result.get_calculation_source_name()}"
)
```

- Running results

```
计算层数：2	计算结果：397.8	计算来源：BracketsCalculation2
```

### Fast interval sum calculation component (based on parenthesis expression)

- Full class name：mathematical_expression/core/calculation/number/fastSumOfIntervalsBrackets.py
- introduce

  The new product of version 1.15, the interval fast sum component, is a fast component that sums all elements of an
  interval with an equal difference of n. It logically simulates an interval into a mathematical sequence and quickly
  sums it through the sum formula.

  This component implements the shared pool computing function. It will check, calculate, and record the results of the
  last time, which can speed up computing. The specific API calls are shown below.

```python
from mathematical_expression.core.calculation.number import fastSumOfIntervalsBrackets

# Get the quick sum calculation component of the interval
fastSumOfIntervalsBrackets = fastSumOfIntervalsBrackets.get_instance("fastSumOfIntervalsBrackets")
# Build the interval expression we need to calculate. 
# The expression is composed of the left and right boundaries of the interval. 
# The double formulas are separated by commas
s = "1 + 10, 20 - (5 + 2)"
# Check the expression. The shared pool has been enabled by default since version 1.2! No need to set manually
# fastSumOfIntervalsBrackets.set_start_shared_pool(True)
fastSumOfIntervalsBrackets.check(s)
# The step size of each element in the interval can be set after version 1.15
fastSumOfIntervalsBrackets.step = 2
# Calculation result value
calculation = fastSumOfIntervalsBrackets.calculation(s)
# Print result value
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())
```

- Running results

  From the above code, we can see that the formula for quick interval summation is composed of two parenthesis
  expressions separated by commas

```
计算层数：3
计算结果：36.0
计算来源：fastSumOfIntervalsBrackets
```

### Fast interval cumulative calculation component (based on parenthesis expression)

- Full class name: mathematical_expression/core/calculation/number/fastSumOfIntervalsBrackets.py

- Introduction

  A new product of version 1.1.5, the interval fast accumulation component, is a fast component that accumulates all
  elements of an interval with an equal difference of n. It logically simulates an interval into a mathematical sequence
  and performs fast accumulation through the sum formula.

  This component implements the shared pool computing function. It will check, calculate, and record the results of the
  last time, which can speed up computing. The specific API calls are shown below.

```python
from mathematical_expression.core.calculation.number import fastMultiplyOfIntervalsBrackets

# Get interval fast cumulative calculation component
fastMultiplyOfIntervalsBrackets = fastMultiplyOfIntervalsBrackets.get_instance("fastMultiplyOfIntervalsBrackets")
# Build the interval expression we need to calculate. The expression is composed of the left and right boundaries of the interval. The double formulas are separated by commas
s = "1 + 10, 20 - (5 + 2)"
# Check the expression. The shared pool has been enabled by default since version 1.15! No need to set manually
# fastSumOfIntervalsBrackets.set_start_shared_pool(True)
fastMultiplyOfIntervalsBrackets.check(s)
# The step size of each element in the interval can be set after version 1.15
fastMultiplyOfIntervalsBrackets.step = 2
# Calculation result value
calculation = fastMultiplyOfIntervalsBrackets.calculation(s)
# Print result value
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())
```

- Running results

  From the above code, we can see that the formula for quick interval summation is composed of two parenthesis
  expressions separated by commas

```
计算层数：3
计算结果：143.0
计算来源：fastMultiplyOfIntervalsBrackets
```

## Advanced Operations

### Registration and use of mathematical function expressions

```python
import mathematical_expression as me

# 实现一个函数 TODO 这个是数学表达式
f = "f(x, y) = y + x * x"
# 开始创建出来函数，并将其注册到管理者中
me.register_function_expression(f)
# 将新版函数计算组件获取到
functionFormulaCalculation2 = me.functionFormulaCalculation2.get_instance("zhao")
# 启用共享池
functionFormulaCalculation2.startSharedPool = True
# 构建需要被计算的数学表达式
s = "2 * f(1 + 1, 3 - 1)"
# 检查表达式
functionFormulaCalculation2.check(s)
# 计算表达式，并获取结果
result = functionFormulaCalculation2.calculation(s)
print(
    f"计算层数：{result.get_result_layers()}"
    f"\t计算结果：{result.get_result()}"
    f"\t计算来源：{result.get_calculation_source_name()}"
)
```

<hr>

## More information

- date: 2022-11-14
- 切换至 [中文文档](https://github.com/BeardedManZhao/mathematical-expression-py/blob/main/README-Chinese.md)
- [mathematical-expression-Java](https://github.com/BeardedManZhao/mathematical-expression)
