from core.manager import CalculationManagement


class Calculation:
    """
    计算接口 其中提供不同计算组件针对数学公式的不同实现
    The calculation interface provides different implementations of different calculation components for mathematical formulas
    """
    __Name__: str

    def __init__(self, string: str):
        """
        构造出来一个计算组件，需要提供一个名字，由名字来构造计算组件
        :param string: 计算组件的名称
        """
        self.__Name__ = string

    def format_str(self, string: str) -> str:
        """
        格式化一个公式 使得其可以被该计算组件进行运算
        Format a formula so that it can be calculated by the calculation component
        :param string: 需要被格式化的数学运算公式
        :return:格式化之后的数学运算公式
        """
        pass

    def get_name(self) -> str:
        return self.__Name__

    def check(self, string: str) -> None:
        """
        检查公式格式是否正确，如果不正确就会抛出一个异常
        Check whether the formula format is correct. If not, an exception will be thrown
        :param string: 需要被检查的字符串
        """
        pass


def get_instance(name: str):
    """
    从管理者中获取到一个组件，请注意类型哦！！！因为这里没有提供类型判断
    :param name: 组件的名称
    :return: 组件的对象
    """
    return CalculationManagement.get_calculation_by_name(name)
