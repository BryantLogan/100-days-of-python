# Functions with Outputs
import re
# def titlecase(format_name):
    

def my_function():
    result = 3 * 2
    return result

output = my_function()

print(output)

# Will return 6 to the console

def format_name(f_name, l_name):
    # print(f_name.title())
    # print(l_name.title())
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(formatted_f_name + " " + formatted_l_name)
    # print(f"{formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("bryant", "LOGAN")
print(formatted_string)
