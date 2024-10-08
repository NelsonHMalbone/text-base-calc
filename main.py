import sys
# Daily Python Project
# text base calculator
while True:
    # have user choose a operator
    function_input = input("Enter Operator + - * / or 'exit' : ")
    if function_input == 'exit':
        sys.exit()
    else:
        # Have user input two numbers
        user_number_input_1 = int(input('enter first number: '))
        user_number_input_2 = int(input('enter second number: '))

        match function_input:
            case '+':
                result_Add = user_number_input_1 + user_number_input_2
                print(result_Add)
            case '-':
                result_sub = user_number_input_1-user_number_input_2
                print(result_sub)
            case '*':
                result_mult = user_number_input_1 * user_number_input_2
                print(result_mult)

            case '/':
                try:
                    result_divison = user_number_input_1 / user_number_input_2
                    print(result_divison)
                except ZeroDivisionError:
                    print("Error message: Divison by Zero: Can not divide by Zero")