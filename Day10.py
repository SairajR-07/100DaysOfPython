def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
     return n1-n2

def multiply(n1,n2):
     return n1*n2

def divide(n1,n2):
     return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

# print(operations["+"](4,8))
# print(operations["-"](4,8))
# print(operations["*"](4,8))
# print(operations["/"](4,8) )
should_accumulate=True
num = float(input("What is the first num?:"))

while should_accumulate:
    for symbol in operations:
        print(symbol)
    operation_symbols=input("Pick an opertion")
    num2=float(input("What is the second num?:"))
    answer=(operations[operation_symbols](num,num2))
    print(f"{num} {operation_symbols} {num2}={answer}")

    choice=input(f"Tpe 'Y' for calculating with {answer}, or type 'n' to start a new calculation?")
    if choice=="y":
     num=answer
    else:
        should_accumulate=False