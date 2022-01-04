# Calculate the sum of elements of the list.

from ast import literal_eval as LE

def sum_of_list_elements(l):
    """
    The function adds the elements of the list and returns the sum.
    """
    sum = 0
    for i in l:
        if isinstance(i, list):
            sum += sum_of_list_elements(i)
        else:
            sum += i
    return sum


while True:
    user_list = input("Enter the list of numbers using python syntax to calculate the sum of all elements or press the key \"Enter\" to exit: ") 
    if user_list == "":
        print("Exit the program.")
        break
    try:
        user_list = LE(user_list)    
        if not isinstance(user_list, list):
            raise RuntimeError("Variable type is not 'list'.")
        print(f"The sum of the elements of the list is {sum_of_list_elements(user_list)}")
    except RuntimeError:
        print("Variable type is not 'list'. Please, use python sintax. Lists are created using square brackets: [1, 2, 3]. Try again.")
        continue
    except TypeError:
        print("Please, enter the list of numbers. Try again.")
        continue    
    except:
        print("The list is entered incorrectly. Please, use python sintax. Lists are created using square brackets: [1, 2, 3]. Try again.")
        continue

