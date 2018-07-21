def foo():
    pass


try:
    foo()
except ZeroDivisionError as e:
    print("ZeroDivisionError")
except ArithmeticError as e:
    print("ArithmeticError")
except AssertionError as e:
    print("AssertionError")
