import Math
import pytest
import sys


#@pytest.mark.mytest #ozacznie testu i wywołanie go po nazwie (pytest -m mytest)
#@pytest.mark.skip(reason="This time skip") #ozaczenie testu do skipnięcia z opisem powodu
#@pytest.mark.skipif(sys.version_info < (3, 11), reason="To low version") #pomija test jeśli spełni się waruenk
# def test_add():
#     assert Math.add(5, 2) == 7
@pytest.mark.numbers
@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 2, 9),
                             ("z", "e", "ze"),
                             (-5, -20, -25)
                         ])
def test_add(num1, num2, result):
    assert Math.add(num1, num2) == result