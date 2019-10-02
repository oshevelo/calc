#1)First task:
def easy_calc():

    try:
        a = int(input("Enter first number :"))
    except:
        print("Not valid number!!!")
        return

    try:
        b = int(input("Enter second number :"))
    except:
        print("Not valid number!!!")
        return

    try:
        operation = input("Enter operation (+, -, *, /) :")
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b != 0:
                return a / b
            else:
                print("Not valid operation, / 0")
    except:
        return

result = easy_calc()
print("Result :", result)


#2) Second task №1:
def calc_second(count = None):
    count = 2
    attempt = 0
    res = 0

    while attempt < count:
        attempt +=1
        if res == 0:
            res = int(input("Enter number :"))
        else:
            res = res
        operation = input("Enter operation (+, -, *, /) :")
        number = int(input("Enter number :"))

        if operation == '+':
            res = res + number
            print("Result operation in:", res)
        elif operation == '-':
            res = res - number
            print("Result operation in:", res)
        elif operation == '*':
            res = res * number
            print("Result operation in:", res)
        elif operation == '/':
            if number != 0:
                res = res / number
            else:
                print("Not valid operation, /0")
                return
            print("Result operation in:", res)

    return res
result = calc_second()
print("Result :", result)


#2) Second task №2:
def calc_second():
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))
    operation = input("Enter operation (+, -, *, /) :")
    if operation == '+':
        res = a + b
    elif operation == '-':
        res = a - b
    elif operation == '*':
        res = a * b
    elif operation == '/':
        if b != 0:
            res = a / b
        else:
            print("Not valid operation, /0")

    while True:
        question = input("Want to continue operation???(Y / N) :")
        if question == "Y" or question == "y":
            c = int(input("Enter number :"))
            operation = input("Enter operation (+, -, *, /) :")
            if operation == '+':
                res = res + c
                print("Result operation in:", res)
            elif operation == '-':
                res = res - c
                print("Result operation in:", res)
            elif operation == '*':
                res = res * c
                print("Result operation in:", res)
            elif operation == '/':
                if c != 0:
                    res = res / c
                else:
                    print("Not valid operation, /0")
                    return
                print("Result operation in:", res)
        elif question == "N" or question == "n":
            return res
            break
    return res
result = calc_second()
print("Result :", result)