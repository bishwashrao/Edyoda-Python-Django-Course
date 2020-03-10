from a01 import *
import pytest

@pytest.mark.parametrize("test_input, expected", [(9999335533, 'zeke')])
def test_eval1(test_input, expected):
    assert question_first_solution(test_input)== expected

@pytest.mark.parametrize("test_input, expected", [({"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}, {'Bombay': 'Delhi', 'Delhi': 'Goa', 'Goa': 'Chennai', 'Chennai': 'Banglore'})])
def test_eval2(test_input, expected):
    assert question_second_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", 
[
    ({'New Hampshire': ['Concord', 'Hanover'],
      'Massachusetts': ['Boston', 'Concord',
      'Springfield'],'Illinois': ['Chicago', 'Springfield', 'Peoria'] 
     }, 
     {'Hanover': ['New Hampshire'],
      'Chicago': ['Illinois'],
      'Boston': ['Massachusetts'],
      'Peoria': ['Illinois'],
      'Concord': ['New Hampshire','Massachusetts'],
      'Springfield': ['Massachusetts', 'Illinois'] 
      }), 
])
def test_eval3(test_input, expected):
    assert question_third_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [("()({})[]{}", True)])
def test_eval4(test_input, expected):
    assert question_fourth_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(5, 'V')])
def test_eval5(test_input, expected):
    assert question_fifth_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", 
[(
"""
#Linear search implementation
#Takes list and a key as input and returns True or False as answer
def linear_search(l,key):
    for value in l:
        if key == value:
            return True #Return True is key exist
    else:
        return False #Return False if key does not exist


l = [100,200,300,400,500,600]
key = 500
result = linear_search(l,key)
print(result)
""",
10
)])
def test_eval6(test_input, expected):
    assert question_sixth_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [("Abcd@1234", ("Valid",[]))])
def test_eval7(test_input, expected):
    assert question_seventh_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [("An important part of my life has been the people who stood by me.", (True,['Your sentence is syntactically correct!']))])
def test_eval8(test_input, expected):
    assert question_eighth_solution(test_input) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", [([1, 4, 3, 2, 5], 4, [4, 3, 2, 5])])
def test_eval9(test_input1, test_input2, expected):
    assert question_ninth_solution(test_input1, test_input2) == expected

@pytest.mark.parametrize("test_input, expected", [([1, 3, 5, 4, 2], (2, [1, 3, 5]))])
def test_eval10(test_input, expected):
    assert question_tenth_solution(test_input) == expected