# 数学表达式

- Switch to [English Document](https://github.com/BeardedManZhao/mathematical-expression/blob/main/README.md)

## 介绍

本框架是一种针对数学公式解析的有效工具，能够解析包含嵌套函数，包含函数，数列步长累加等数学公式，返回值是一个数值的结果对象，同时也可以进行比较运算的操作，再进行比较的时候，返回值是一个布尔值结果对象。

- pip获取命令

```xml

```

## 框架架构

### 计算管理者

- 类组件：core.manager.CalculationManagement
- 介绍：

  管理者是一个为了同时使用单例与动态对象而设计的一个组件，管理者的存在可以使得每一个组件能够被名字所获取到，相同名字的组件，在内存中的存储地址也是一样的，避免了冗余组件的调用，同时针对需要使用到动态成员的组件，也可以通过一个新名字获取到一个新组件。
- API使用示例

```java

```

- 运行结果

  最后三行就是内存数据的比较，实例化出来的组件与管理者中的组件在内存中是一样的，但是不同名称的组件是不同的。

```

```

## 计算组件介绍

### 无括号表达式

- 类组件：core/calculation/number/prefixExpressionOperation.py
- 介绍

  针对一个没有括号，但是有加减乘除以及取余等运算操作的数学表达式而设计的组件，该组件可以实现带有优先级计算的功能，其中通过前缀表达式解析计算，将操作数与操作符一同存储到栈，在存储的同时配有计算优先级比较，如果当下的优先级较小，就先将上一个操作数与操作符与当前操作数进行运算，形成一个新的数值，然后再入栈。
- API使用示例

  该组件支持的运算符有： a+b a-b a*b a/b a%b

```python
# This is a sample Python script.
from core.calculation.number import prefixExpressionOperation
from core.calculation.number.prefixExpressionOperation import PrefixExpressionOperation
from core.container.CalculationNumberResults import CalculationNumberResults

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

- 运行结果

  在API调用中，对函数的运行结果进行了打印，可以看到，组件计算的返回值是一个结果集对象，在该对象中存储的就是很多有关计算结果相关的信息。

```
计算层数：2
计算结果：40.0
计算来源：p
```

### 嵌套括号表达式

- 类组件：core/calculation/number/bracketsCalculation2.py
- 介绍：

  嵌套括号表达式解析组件，能够针对带有多个括号的数学表达式进行解析与结果计算，针对嵌套括号进行优先级的解析与计算，该组件依赖于“core.calculation.number.PrefixExpressionOperation”，在该组件中采用递归进行括号的解析，然后将最内层面的表达式提供给“core.calculation.number.PrefixExpressionOperation”进行计算。
- API使用示例

  该组件支持的运算符有： a+b a-b a*b a/b a%b ( )

```python
# This is a sample Python script.
from core.calculation.number import bracketsCalculation2
from core.calculation.number.bracketsCalculation2 import BracketsCalculation2
from core.container.CalculationNumberResults import CalculationNumberResults

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

- 运行结果

  在API调用中，对表达式的计算结果进行了打印，可以看到，组件计算的返回值是一个数值结果对象，在该对象中存储的就是很多有关计算结果相关的信息。

```
计算层数：2
计算结果：31.0
计算来源：BracketsCalculation
```

### 数学比较表达式

- 类组件：core/calculation/bool/booleanCalculation2.py
- 介绍

  使用比较运算符两个括号表达式是否相互成立的一个组件，返回值是一个布尔类型的结果对象，该组件能够比较两个数值的大小等，也可以比较两个表达式之间的大小等关系，依赖于组件“core.calculation.bool.BooleanCalculation2”
- API使用示例

  该组件支持的运算符如API中演示

```python
# This is a sample Python script.
from core.calculation.bool import booleanCalculation2
from core.calculation.bool.booleanCalculation2 import BooleanCalculation2
from core.container.CalculationBooleanResults import CalculationBooleanResults


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

- 运行结果

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

### 区间累加表达式

- 类组件：core/calculation/number/cumulativeCalculation.py

- 介绍

在数学表达式中，往往有这样的一种公式，公式内容如下图所示，可以看到需要进行累加的数列操作，那么在这种公式的需求下，您可以通过上面的类组件去达到您所需要的目的。

![img_1](https://user-images.githubusercontent.com/113756063/201575828-5b76af88-6040-430d-a54c-61faf5905594.png)

- API使用示例

语法层面于其他组件几乎一致，数学表达式的撰写于组件的计算示例就如下面所示，在这里展示的就是一个累加数学公式的计算。

```python
# This is a sample Python script.
from core.calculation.number import cumulativeCalculation

# 获取到累加公式的计算组件
cumulativeCalculation = cumulativeCalculation.get_instance("cumulative")
# 构造一个数学表达式。这里，“n[1,10,1]”类似于数学中的累加符号。N
# 将在此间隔内持续增加。每增加一项都将纳入计算公式
# 其中，[1,10,1]中的最后一个1表示递增步长，可以实现不同等式的累加
# 间隔中的差值
s = "n[1,10,1] 2 * (n + 1)"
# 检查数学表达式
cumulativeCalculation.check(s)
# 计算结果
calculation = cumulativeCalculation.calculation(s)
# 打印结果数值
print(
    f"计算层数：{calculation.get_result_layers()}"
    f"\t计算结果：{calculation.get_result()}"
    f"\t计算来源：{calculation.get_calculation_source_name()}"
)
```

- 运行结果

```
计算层数：21	计算结果：130.0	计算来源：cumulative
```

### 函数运算表达式

- 类组件：core/calculation/number/functionFormulaCalculation.py

- 介绍

  针对一些函数的操作，在该框架中也有支持，可以使用上面的类进行这中需要函数的数学表达式的书写，需要注意的是，一切在表达式中使用到的函数都需要在“CalculationManagement”中进行逻辑注册，使得计算的时候可以访问到函数

- API使用示例

```python
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
```

- 运行结果

```
INFO:root:Find and prepare the startup function: DoubleValue
计算层数：1	计算结果：21.0	计算来源：BracketsCalculation2
```

<hr>

- date: 2022-11-14
- Switch to [English Document](https://github.com/BeardedManZhao/mathematical-expression/blob/main/README.md)
