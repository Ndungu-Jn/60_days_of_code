#Functions with output
#example: an empty bottle enters a machine and comes out with milk.
#so the machine encapsulates the code inside  the function that helps give a results

# def my_function():
#     result = 3*2
#     return result
#
# print(my_function())
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("John", "ndungu")
print(formatted_string)





