# mathematical-expression

- 切换至 [中文文档](https://github.com/BeardedManZhao/mathematical-expression-py/blob/main/README-Chinese.md)

## introduce

This framework is an effective tool for mathematical formula analysis. It can analyze mathematical formulas including
nested functions, including functions, and step accumulation of series. The return value is a numerical result object.
At the same time, it can also be used for comparison operations. When comparing again, the return value is a Boolean
result object.

- pip Get Command

```shell
pip install mathematical_expression_py
```

## Framework

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

  The operators supported by this component are： a+b a-b a*b a/b a%b

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

<hr>

More information

- date: 2022-11-14
- 切换至 [中文文档](https://github.com/BeardedManZhao/mathematical-expression-py/blob/main/README-Chinese.md)
- [mathematical-expression-Java](https://github.com/BeardedManZhao/mathematical-expression)
