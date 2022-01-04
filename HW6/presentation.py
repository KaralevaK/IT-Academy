import bl

def calculate(user_expression,accuracy):
    return bl.calculate(user_expression,accuracy)

def main_flow():
    while True:
        user_expression = input("Enter your mathematical expression using the following symbols: (,),*, /, +, -,  or press enter to exit:\n")
        if user_expression:
            accuracy = input("Enter accuracy (non-negative integer) for show result or press enter to set default to 2:\n")
            print(calculate(user_expression,accuracy))
            continue
        else:
            print("Have a good day!")
            break

if __name__=="__main__":
    main_flow()

