from simpleeval import simple_eval

def str_operation():
    operation = simple_eval(input("Enter operation :", ))
    return operation

result = str_operation()
print("Result :", result)