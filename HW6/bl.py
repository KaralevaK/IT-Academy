import data

def calculate(user_expression,accuracy):
    """
    This function calculates the value of a math expression from string and returns the result with the specified accuracy.

    Params:
    user_expression: str
    accuracy: str
    
    Returns:
    str
    """
    try:
        math_expr = convert_expression_to_list(user_expression)
        # преверяем корректность скобочной последовательности
        if not check_braсkets(math_expr):
            raise RuntimeError("Bracket sequence is incorrect.")
        # проверяем и устанавливаем значение точности
        if accuracy.isdigit():
            accuracy = int(accuracy)
        elif accuracy == "":
            accuracy = 2
        else:
            raise RuntimeError("Accuracy is incorrect. Try again.")
        # если пользователь ввел только одно число, вернем его, иначе - вычисляем значение выражения
        if len(math_expr) == 1 and math_expr[0] not in {'(','+','-','*','/',')'}:
            result_expr = round(float(math_expr[0]),accuracy)
        else:
            result_expr=round(calculate_math_expr(math_expr),accuracy)
        return f"Result: {result_expr}"
    except RuntimeError as x:
        return x 
    except:
        return "Something went wrong. Check if the expression is correct. Try again."

def convert_expression_to_list(user_expression):
    """
    This function parses a source string to tokens (numbers and operators).
    
    Params:
    user_expression: str
       
    Returns:
    math_expr: list
    """
    end_index = len(user_expression)-1
    start_index=0
    current_index =0
    math_expr=[]
    while current_index <= end_index:
        if user_expression[current_index] in {'(','+','-','*','/',')'}:
            # проверка для учета отрицательных чисел в начале выражения либо на первом месте в скобках
            if not((current_index == 0 or user_expression[current_index-1] =='(') and user_expression[current_index]=='-') :
                if start_index != current_index:
                    math_expr.append(user_expression[start_index:current_index])
                math_expr.append(user_expression[current_index])
                start_index=current_index+1
        current_index += 1
    else:
        # добавление в список последнего числа
        if start_index < end_index:
            math_expr.append(user_expression[start_index:end_index+1]) 
        elif start_index == end_index:
            math_expr.append(user_expression[start_index]) 
    return math_expr

def check_braсkets(math_expr):
    """
    This function this function checks if the sequence of brackets is correct.
    
    Params:
    math_expression: list
       
    Returns:
    bool
    """
    # введем переменную для проверки корректности скобок
    check_braсkets = 0
    for token in math_expr:
        if token == "(":
            check_braсkets += 1
        elif token == ")":
            check_braсkets -= 1
            if check_braсkets < 0:
                return False
    if check_braсkets != 0:
        return False  
    else:
        return True

def calculate_math_expr(math_expr):
    """
    A function for calculating a mathematical expression obtained as a list of numbers and operators.

    Params:
    math_expr: list

    Returns:
    float
    """
    # Словарь содержит в ключах знаки операций, а в значениях - их приоритет
    oper = { '+':1, '-':1, '*':2,'/':2}
    braсkets={')', '('}    
    stack_numbers=[]
    stack_oper=[]
    for token in math_expr:
        if token in oper:
            while True:
                if len(stack_oper) == 0:
                    stack_oper.append(token)
                    break
                if stack_oper[len(stack_oper)-1] in braсkets:
                    stack_oper.append(token)
                    break
                if oper[token] > oper[stack_oper[len(stack_oper)-1]]:
                    stack_oper.append(token)
                    break
                if oper[token] <= oper[stack_oper[len(stack_oper)-1]]:
                    if len(stack_oper) != 0:
                        # выполняем последнюю операцию из стека
                        do_oper_and_change_stacks(stack_numbers, stack_oper)
        elif token in braсkets:
            if token == "(":
                stack_oper.append(token)
            elif token == ")":
                # выполняем все опeрации из стека операций до тех пор, пока не встретим открывающуюся скобку
                while stack_oper[len(stack_oper)-1] != "(":
                    do_oper_and_change_stacks(stack_numbers, stack_oper)
                stack_oper.pop()
        else:
            stack_numbers.append(token)
        
    # выполняем все операции, оставшиеся в стеке операций
    while len(stack_oper) != 0:
        do_oper_and_change_stacks(stack_numbers, stack_oper)
    # результат - последнее значение в стеке чисел
    return stack_numbers.pop()

def do_oper_and_change_stacks(stack_numbers, stack_oper):
    """
    The function performs the last operation from the stack_oper list with the last two operands from the stack_numbers list.
    
    Params:
    stack_numbers: list
    stack_oper: list
       
    Returns:
    None
    """
    a2 = float(stack_numbers.pop())
    a1 = float(stack_numbers.pop())
    last_oper = stack_oper.pop()
    if last_oper == '+':
        stack_numbers.append(data.sum(a1,a2))
    elif last_oper =='-':
        stack_numbers.append(data.difference(a1,a2))
    elif last_oper =='*':
        stack_numbers.append(data.multiplication(a1,a2))
    elif last_oper=='/':
        stack_numbers.append(data.division(a1,a2))


if __name__=="__main__":
    print("Calculate: -9-0.3*(-5)+(-7)*(56-12)/8-66")
    print(convert_expression_to_list("-9-0.3*(-5)+(-7)*(56-12)/8-66"))
    print(eval("-9-0.3*(-5)+(-7)*(56-12)/8-66"))
    print(calculate_math_expr(convert_expression_to_list("-9-0.3*(-5)+(-7)*(56-12)/8-66")))   








    