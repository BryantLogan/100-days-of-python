# simple function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
# greet()

# function that allows for input

def greet_with_name(name):
    print(f"Hello, {name}")
    print(f"How do you do, {name}?")

# greet_with_name("Billy")

def greet_with(a, b):
    print(f"Hello {a}")
    print(f"What's it like in {b}?")

greet_with(a = "Bryant",b = "Spain")