# ![image](https://user-images.githubusercontent.com/113756063/203919312-dcec4a61-2136-4af2-a361-66b2ed4e6a54.png)  数学表达式

- Switch to [English Document](https://github.com/BeardedManZhao/mathematical-expression-py/blob/main/README.md)

## 介绍

本框架是一种针对数学公式解析的有效工具，能够解析包含嵌套函数，包含函数，数列步长累加等数学公式，返回值是一个数值的结果对象，同时也可以进行比较运算的操作，再进行比较的时候，返回值是一个布尔值结果对象。

- pip获取命令

```shell
pip install mathematical_expression_py
```

## 框架架构

### 使用 mathematical_expression 包

```python
# 导入 mathematical-expression 解析库
import mathematical_expression as mathematical

# 构建需要计算的两种表达式
s1, s2 = "1 + 20 - 2 + 4", "1 + 20 - (2 + 4)"
# 通过库获取到无括号表达式计算组件
prefixExpressionOperation = mathematical.prefixExpressionOperation.get_instance("prefixExpressionOperation")
# 通过库获取到有括号表达式计算组件
bracketsCalculation2 = mathematical.bracketsCalculation2.get_instance("bracketsCalculation2")

# 将第一种公式传递给无括号表达式计算组件检查与计算 该公式也允许传递给有括号表达式计算
prefixExpressionOperation.check(s1)
calculation = prefixExpressionOperation.calculation(s1)
# 打印出第一个表达式的计算结果
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())

# 将第二种公式传递给有括号表达式计算组件进行检查与计算
bracketsCalculation2.check(s2)
calculation2 = bracketsCalculation2.calculation(s2)
# 打印出第二个表达式的计算结果
print("计算层数：" + str(calculation2.get_result_layers()) + "\n计算结果：" + str(calculation2.get_result()) +
      "\n计算来源：" + calculation2.get_calculation_source_name())
```

- 运行结果
  通过导入包可以获取到各个计算组件的模块对象，能够有效的减少代码导包代码。

```
计算层数：1
计算结果：23.0
计算来源：prefixExpressionOperation
计算层数：2
计算结果：15.0
计算来源：bracketsCalculation2
```

### 计算管理者

- 类组件：mathematical_expression/core/manager/CalculationManagement.py
- 介绍：

  管理者是一个为了同时使用单例与动态对象而设计的一个组件，管理者的存在可以使得每一个组件能够被名字所获取到，相同名字的组件，在内存中的存储地址也是一样的，避免了冗余组件的调用，同时针对需要使用到动态成员的组件，也可以通过一个新名字获取到一个新组件。
- API使用示例

```python
from mathematical_expression.core.calculation.number import bracketsCalculation2, functionFormulaCalculation
from mathematical_expression.core.manager import CalculationManagement

# 创建两个括号表达式解析组件与一个函数表达式解析组件
br1 = bracketsCalculation2.get_instance("br1")
br2 = bracketsCalculation2.get_instance("br2")
fu1 = functionFormulaCalculation.get_instance("fu1")
# 从管理者中获取到这三个名字的组件
m_br1 = CalculationManagement.get_calculation_by_name("br1")
m_br2 = CalculationManagement.get_calculation_by_name("br2")
m_fu1 = CalculationManagement.get_calculation_by_name("fu1")
# 通过 get_instance 与 管理者提取 这两种方式获取到的组件，在相同名字的情况下，两者是一个对象
print(br1 == m_br1)
print(br2 == m_br2)
print(fu1 == m_fu1)
print(br1 == br2)
```

- 运行结果

  最后三行就是内存数据的比较，实例化出来的组件与管理者中的组件在内存中是一样的，但是不同名称的组件是不同的。

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

### 运算符重定义

- 类组件：mathematical_expression/core/manager/ConstantRegion.py
- 介绍

  在框架中有一个常量池，其中存储着需要经常复用的数据，这些数据在python版本的框架中是可以进行修改的，通常修改这些数据可以增加更大的灵活性，但是需要注意的是，此处的修改操作也可能引发一些奇怪的异常，所以需要根据情况决定是否要使用重定义技术。

  接下来请查阅重定义的使用示例

```python
# This is a sample Python script.
from mathematical_expression.core.calculation.number import bracketsCalculation2
from mathematical_expression.core.calculation.number.bracketsCalculation2 import BracketsCalculation2
from mathematical_expression.core.container.CalculationNumberResults import CalculationNumberResults
from mathematical_expression.core.manager import ConstantRegion

# 重定义加号的符号
ConstantRegion.PLUS_SIGN = '$'
# 重定义乘号的符号
ConstantRegion.MULTIPLICATION_SIGN = '@'
# 刷新常量区配置
ConstantRegion.re_fresh()

# Get a calculation component that evaluates nested parenthesis expressions
bracketsCalculation2: BracketsCalculation2 = bracketsCalculation2.get_instance("BracketsCalculation")
# Create an expression
# s: str = "1 + 2 + 4 * (10 - 3)" TODO 这里的加号与乘号被重定义了，可以使用新的字符替代
s: str = "1 $ 2 $ 4 @ (10 - 3)"
# Check the expression for errors
bracketsCalculation2.check(s)
# Start calculating results
calculation: CalculationNumberResults = bracketsCalculation2.calculation(s)
# Print result value
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())
```

- 运行结果

  可以看到这里的运行很顺利，在公式中，对符号进行了重定义

```
计算层数：2
计算结果：31.0
计算来源：BracketsCalculation
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

  嵌套括号表达式解析组件，能够针对带有多个括号的数学表达式进行解析与结果计算，针对嵌套括号进行优先级的解析与计算，该组件依赖于“mathematical_expression.core.calculation.number.PrefixExpressionOperation”，在该组件中采用递归进行括号的解析，然后将最内层面的表达式提供给“mathematical_expression.core.calculation.number.PrefixExpressionOperation”进行计算。
- API使用示例

  该组件支持的运算符有： a+b a-b a*b a/b a%b ( )

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

  使用比较运算符两个括号表达式是否相互成立的一个组件，返回值是一个布尔类型的结果对象，该组件能够比较两个数值的大小等，也可以比较两个表达式之间的大小等关系，依赖于组件“mathematical_expression.core.calculation.bool.BooleanCalculation2”
- API使用示例

  该组件支持的运算符如API中演示

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
from mathematical_expression.core.calculation.number import cumulativeCalculation

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
from mathematical_expression.core.calculation.function.Function import Function
from mathematical_expression.core.calculation.number import functionFormulaCalculation
from mathematical_expression.core.manager import CalculationManagement


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

### 多参函数运算表达式

- 类组件：mathematical_expression/core/calculation/number/functionFormulaCalculation2.py
- 介绍

  针对一些在表达式中使用了函数的表达式计算，可以使用上面的类进行操作，它是“core.calculation.number.FunctionFormulaCalculation”类的升级版，从1.1版本开始出现，同时也是它的一个子类拓展实现。

  相较于父类，本组件弥补了父类只能解析带有一个参数函数表达式的不足，在该组件中，可以使用很多的实参进行函数的运算，例如sum(
  1,2,3)
  这类函数，就是一个多参函数，接下来请看API的使用示例，在此示例中，展示了多惨函数表达式的计算与结果。

```python
from mathematical_expression.core.calculation.function.Function import Function
from mathematical_expression.core.calculation.number import functionFormulaCalculation2
from mathematical_expression.core.manager import CalculationManagement


# 实现一个函数
class Sum(Function):
    def run(self, floats: list):
        res = 0
        for d in floats:
            res += d
        return res


# 开始创建出来函数，并将其注册到管理者中
CalculationManagement.register_function(Sum("sum"))
# 将新版函数计算组件获取到
functionFormulaCalculation2 = functionFormulaCalculation2.get_instance("zhao")
# 启用共享池
functionFormulaCalculation2.startSharedPool = True
# 构建需要被计算的数学表达式 TODO 表达式中使用的函数参数不只一个
s = "2 * (200 - sum(1 + 10.1, 2, 3)) + sum(10, 20)"
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

- 运行结果

```
计算层数：2	计算结果：397.8	计算来源：BracketsCalculation2
```

### 快速区间求和计算组件（基于括号表达式）

- 类组件：mathematical_expression/core/calculation/number/fastSumOfIntervalsBrackets.py
- 介绍
  1.15版本的新产物，区间快速求和组件，是针对一个等差为n的区间进行所有元素求和的快速组件，它将一个区间在逻辑上模拟成为一个数学数列，并通过求和公式进行快速的求和。

  该组件实现了共享池计算功能，将检查，计算，以及上一次结果记录实现，能够加快计算速度，具体API调用如下所示。

```python
from mathematical_expression.core.calculation.number import fastSumOfIntervalsBrackets

# 获取到区间快速求和计算组件
fastSumOfIntervalsBrackets = fastSumOfIntervalsBrackets.get_instance("fastSumOfIntervalsBrackets")
# 构建我们需要计算的区间表达式，表达式由区间左右边界构成，其中的双公式中间使用逗号分割
s = "1 + 10, 20 - (5 + 2)"
# 检查表达式，共享池从1.15版本后，已经是默认启用的状态了！不需要手动设置了
# fastSumOfIntervalsBrackets.set_start_shared_pool(True)
fastSumOfIntervalsBrackets.check(s)
# 从1.15版本之后可以对区间中每一个元素的步长进行设置
fastSumOfIntervalsBrackets.step = 2
# 计算结果数值
calculation = fastSumOfIntervalsBrackets.calculation(s)
# 打印结果数值
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())
```

- 运行结果

  从上面代码中我们可以看到，快速区间求和计算的公式由被逗号分割的两个括号表达式组成

```
计算层数：3
计算结果：24.0
计算来源：fastSumOfIntervalsBrackets
```

### 快速区间累乘计算组件（基于括号表达式）

- 类组件：mathematical_expression/core/calculation/number/fastSumOfIntervalsBrackets.py
- 介绍
  1.1.5版本的新产物，区间快速累乘组件，是针对一个等差为n的区间进行所有元素累乘的快速组件，它将一个区间在逻辑上模拟成为一个数学数列，并通过求和公式进行快速的累乘。

  该组件实现了共享池计算功能，将检查，计算，以及上一次结果记录实现，能够加快计算速度，具体API调用如下所示。

```python
from mathematical_expression.core.calculation.number import fastMultiplyOfIntervalsBrackets

# 获取到区间快速累乘计算组件
fastMultiplyOfIntervalsBrackets = fastMultiplyOfIntervalsBrackets.get_instance("fastMultiplyOfIntervalsBrackets")
# 构建我们需要计算的区间表达式，表达式由区间左右边界构成，其中的双公式中间使用逗号分割
s = "1 + 10, 20 - (5 + 2)"
# 检查表达式，共享池从1.15版本后，已经是默认启用的状态了！不需要手动设置了
# fastSumOfIntervalsBrackets.set_start_shared_pool(True)
fastMultiplyOfIntervalsBrackets.check(s)
# 从1.15版本之后可以对区间中每一个元素的步长进行设置
fastMultiplyOfIntervalsBrackets.step = 2
# 计算结果数值
calculation = fastMultiplyOfIntervalsBrackets.calculation(s)
# 打印结果数值
print("计算层数：" + str(calculation.get_result_layers()) + "\n计算结果：" + str(calculation.get_result()) +
      "\n计算来源：" + calculation.get_calculation_source_name())
```

- 运行结果

  从上面代码中我们可以看到，快速区间求和计算的公式由被逗号分割的两个括号表达式组成

```
计算层数：3
计算结果：143.0
计算来源：fastMultiplyOfIntervalsBrackets
```

<hr>

更多信息

- date: 2022-11-14
- Switch to [English Document](https://github.com/BeardedManZhao/mathematical-expression-py/blob/main/README.md)
- [mathematical-expression-Java](https://github.com/BeardedManZhao/mathematical-expression)
