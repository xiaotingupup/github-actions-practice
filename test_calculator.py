# 单元测试文件：测试calculator模块的功能
import pytest
from calculator import add, multiply

# 测试加法函数
def test_add():
    assert add(2, 3) == 5      # 正数相加
    assert add(-1, 1) == 0     # 正负相加

# 测试乘法函数
def test_multiply():
    assert multiply(3, 4) == 12  # 正数相乘
    assert multiply(2, 0) == 0   # 与0相乘
