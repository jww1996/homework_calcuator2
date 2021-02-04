import pytest

from python_code.calc import Calculator


# 在conftest中将calc实例化，将作用域设置为module
@pytest.fixture(scope="module")
def get_calc():
    print("实例化变量")
    calc = Calculator()
    return calc
