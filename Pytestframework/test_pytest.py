import pytest
@pytest.fixture()
def f1():
    print("Hi welcome")

def test_1(f1):
    print("this is first test case")

def test_2(f1):
    print("this is second test case")

def test_3(f1):
    print("this is third test case")

def test_4(f1):
    print("this is fourth test case")

def test_5(f1):
    print("this is fifth test case")
