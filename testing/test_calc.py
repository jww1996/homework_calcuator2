import allure
import pytest
import yaml
from python_code.calc import Calculator

# 读取文件


with open("./datas/calc.yaml") as f:
    # 用D代表读取的整个yaml文件
    D = yaml.safe_load(f)

    # 读取yaml中加法的测试用例
    """
        加法的测试用例:
            datas：除法的测试用例
            myid1：别名

    """
    adddata = D['add']
    add_datas = adddata['datas']
    print(add_datas)
    myid1 = adddata['myid1']
    print(myid1)

    # 读取yaml中除法的测试用例
    """
        除法的测试用例:
            divdatas：除法的测试用例
            myid2：别名

    """
    divdata = D['div']
    div_datas = divdata['divdatas']
    print(div_datas)
    myid2 = divdata['myid2']
    print(myid2)

    # 读取yaml中减法的测试用例
    """
        减法的测试用例:
            subdatas：除法的测试用例
            myid3：别名

    """
    subdata = D['sub']
    sub_datas = subdata['subdatas']
    print(sub_datas)
    myid3 = subdata['myid3']
    print(myid3)

    # 读取yaml中乘法的测试用例
    """
        乘法的测试用例:
            muldatas：乘法的测试用例
            myid4：别名

    """
    muldata = D['mul']
    mul_datas = muldata['muldatas']
    print(mul_datas)
    myid4 = muldata['myid4']
    print(myid4)

# 利用fixture 带参数传递，通过 get_datas 获取参数，区分加减乘除的变量名
@pytest.fixture(params=add_datas, ids=myid1)
def get_datas1(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算")

# 利用fixture 带参数传递，通过 get_datas 获取参数，区分加减乘除的变量名
@pytest.fixture(params=div_datas, ids=myid2)
def get_datas2(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算")

# 利用fixture 带参数传递，通过 get_datas 获取参数，区分加减乘除的变量名
@pytest.fixture(params=sub_datas, ids=myid3)
def get_datas3(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算")

# 利用fixture 带参数传递，通过 get_datas 获取参数，区分加减乘除的变量名
@pytest.fixture(params=mul_datas, ids=myid4)
def get_datas4(request):
    print("开始计算")
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算")

@allure.feature("测试计算器")
class TestCalc:

    """
        优化点：
        1.把setup和teardown 换成了 fixture方法 get_calc
        2.把get_calc 放到 conftest 中
        3.把参数化换为了 fixture 参数化方式
        4.测试用例中的数据需要通过 get_datas 获取
          get_datas返回了一个列表[0.1, 0.2, 0.3],分别代表了a, b, expect
        """
    @allure.story("测试加法")
    # 设定测试用例执行的顺序
    @pytest.mark.run(order=1)
    # 加法的测试用例
    def test_add(self, get_calc, get_datas1):

        # 调用add方法
        with allure.step("计算两数的相加和"):
            result = get_calc.add(get_datas1[0], get_datas1[1])
        # 可以使用isinstance来判断类型,判断result是浮点数，作保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)

        # 得到结果之后需要写断言
        assert result == get_datas1[2]

    @allure.story("测试除法")
    @pytest.mark.run(order=4)
    # 除法的测试用例
    def test_div(self, get_calc, get_datas2):
        # 调用div方法
        with allure.step("计算两数相除的结果"):
            result = get_calc.div(get_datas2[0], get_datas2[1])

        # 可以使用isinstance来判断类型,判断result是浮点数，作保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 断言，得到结果后需要写断言
        assert result == get_datas2[2]

    @allure.story("测试减法")
    @pytest.mark.run(order=2)
    # 减法的测试用例
    def test_sub(self, get_calc, get_datas3):
        with allure.step("计算两数相减的结果"):
            result = get_calc.sub(get_datas3[0], get_datas3[1])

        # 可以使用isinstance来判断类型,判断result是浮点数，作保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 断言，得到结果后需要写断言
        assert result == get_datas3[2]

    @allure.story("测试乘法")
    @pytest.mark.run(order=3)
    # 乘法的测试用例
    def test_mul(self, get_calc, get_datas4):
        with allure.step("计算两数相乘的结果"):
            result = get_calc.mul(get_datas4[0], get_datas4[1])

        # 可以使用isinstance来判断类型,判断result是浮点数，作保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 断言，得到结果后需要写断言
        assert result == get_datas4[2]
