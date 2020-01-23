"""
@author:    tosstosstoss
@date:      1/22/2020
@description:   showing how to implement basic algebra formulas using functions.
"""



def formula_one(a, b):
    """
    function:       formula_one
    params:         a -> int, b -> int
    return:         int
    description:    a^2 - b^2 = (a - b) (a + b)
    """
    return a**2 - b**2

def formula_two(a, b):
    """
    function:       formula_two
    params:         a -> int, b -> int
    return:         int
    description:    (a + b)^2 = a^2 + 2ab + b^2
    """
    return (a + b)**2

def formula_three(a, b):
    """
    function:       formula_three
    params:         a -> int, b -> int
    return:         int
    description:    a^2 - b^2 = (a - b) (a + b)
    """
    return a**2 + b**2

def formula_four(a, b):
    """
    function:       formula_four
    params:         a -> int, b -> int
    return:         int
    description:    a^2 - b^2 = (a - b) (a + b)
    """
    return (a - b)**2


def test_formula_one(a, b):
    """
    function:       test_formula_one
    params:         a -> int, b -> int
    return:         int
    description:    a^2 - b^2 = (a - b) (a + b)
    """
    val = (a - b) * (a + b)
    
    assert formula_one(a, b) == val

def test_formula_two(a, b):
    
    assert formula_two(a, b) == a**2 + 2 * a * b + b**2

def test_formula_three(a, b):
    
    assert formula_three(a, b) == (a + b)**2 - 2 * a * b
 
def test_formula_four(a, b):
    
    assert formula_four(a, b) == a**2 - 2 * a * b + b**2
    
def run_tests():
    a_list = [5.0, 4.0, 3.0, 2.0, 1.0]
    b_list = [1.0, 2.0, 3.0, 4.0, 5.0]
    for i in range(0, 5):
        test_formula_four(a_list[i], b_list[i])
        test_formula_three(a_list[i], b_list[i])
        test_formula_two(a_list[i], b_list[i])
        test_formula_one(a_list[i], b_list[i])
    return "PASS"

def main():
    if run_tests() == "PASS":
        print("success")
    else:
        print("failure")

if __name__ == "__main__":
    print("formulas example")
    main()