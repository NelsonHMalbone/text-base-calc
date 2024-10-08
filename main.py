# Daily Python Project
# text base calculator

# Have user input two numbers
user_number_input_1 = int(input('enter first number: '))
user_number_input_2 = int(input('enter second number: '))

# have user choose a operator
function_input = input("Enter Operator + - * /: ")

match function_input:
    case '+':
        result = user_number_input_1 + user_number_input_2
    case '-':
        result = user_number_input_1-user_number_input_2
    case '*':
        result = user_number_input_1 * user_number_input_2
    case '/':
        result = user_number_input_1 / user_number_input_2

print(result)