#   CALCULATOR PROJECT

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b    

def mulitiply(a,b):
    return a*b

def divide(a,b):
    return a/b

# CREATING DICTIONARY

operations = {
    "+" : add,
    "-" : subtract,
    "*" : mulitiply,
    "/" : divide
}


#print(operations["+"](5,10))
#print(operations["-"](9,5))


num1 = float(input("What is the first number?: "))
for symbol in operations:
    print(symbol)
    should_continue = True
operator = input("Pick an operation from the line above: ")

num2 = float(input("What is the next number?: "))

answer = operations[operator](num1,num2)

print(f"{num1} {operator} {num2} = {answer}")




