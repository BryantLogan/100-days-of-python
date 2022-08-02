def add(n1,n2):
  return n1 + n2

#Subtract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1 * n2
3

#Divide
def divide(n1,n2):
  return n1 / n2

#Dictionary with keys as operation symbols, values as previously defined functions
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

# printing the dictionary keys to the console
def calculator():
  num1 = float(input("What is the first number?\n"))
  for symbol in operations:
    print(symbol)

# creating while loop for user input and mathematical operations
  repeat = True

  while repeat: 
    operation_symbol = (input("Pick an operation:\n"))

    num2 = float(input("What is the next number?\n"))

    calc_function = operations[operation_symbol]

    answer = calc_function(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.\n").lower() == "y":
      num1 = answer
    else:
      repeat = False
      # calling the function within itself (recursive)
      calculator()

# calling the function 
calculator()