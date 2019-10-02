import ast
import math

def calc_three():
    str = '2 + 2 * 2'
    code = ast.parse(str, mode='eval')
    print("Result 1:", eval(compile(code, '', mode='eval')))

    str = 'math.pi + 2 - 4'
    code = ast.parse(str, mode='eval')
    print("Result 2:", eval(compile(code, '', mode='eval')))

res = calc_three()