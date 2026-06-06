def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def mutiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : mutiply,
    "/" : divide,
}

n1 = float(input("Enter the first number : \n"))
for symbol in operations:
    print(symbol)
operator = input("Choose an operator : \n")
n2 = float(input("Enter the second number : \n"))

answer = operations[operator](n1, n2)
print(f"{n1} {operator} {n2} = {answer}")
