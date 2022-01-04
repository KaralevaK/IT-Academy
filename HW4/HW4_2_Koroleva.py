# calculating the amount of debt when paying a bill in a restaurant.
 
def is_float_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_bill():
    while True:
        bill=input("Enter, using a comma, how much money each guest contributed to pay the bill within a cent:").split(',')
        flag_correct = True
        sum = 0
        for k,value in enumerate(bill):
            if is_float_number(value) and float(value) >= 0:
                bill[k] = round(float(value),2)
                sum += bill[k]
            else:
                flag_correct = False
                break
        if flag_correct:
            return bill, sum, len(bill)
        else:
            print("Incorrect value.")

bill, sum, number_of_guests = get_bill()
pay_per_one=round(sum/number_of_guests,2)

# checking the possibility to split the bill equally
mistake = round(pay_per_one*number_of_guests - sum,2)
if mistake != 0:
    print(f"To make it possible to calculate, we will change the amount of money for the first guest ({mistake}).")
    sum =  round(pay_per_one*number_of_guests,2)
    bill[0] += mistake

# displaying general information about the bill in a restaurant
print(f"The total amount: {sum}. The amount per person: {pay_per_one}. Contribution of everyone: {bill}. ")

# creating a list of amounts of money that have lent or borrowed
contribution_of_everyone = [round(x-pay_per_one,2) for x in bill]

debtors_list = []
creditors_list = []

for k,value in enumerate(contribution_of_everyone):
    if value < 0:
        debtors_list.append([k+1,-value])
    elif value > 0:
        creditors_list.append([k+1,value])

if len(debtors_list) != 0:
    # calculating the amount of debt, add information in debtors_list about how much money and from whom the debtor borrowed
    # create variable to iterate for debtors_list
    k1=0
    for k,value in enumerate(creditors_list):
        while value[1] > 0:
            if debtors_list[k1][1] != 0 and debtors_list[k1][1] <= value[1]:
                balance = round(value[1] - debtors_list[k1][1],2)
                debtors_list[k1].append([creditors_list[k][0],debtors_list[k1][1]])
                creditors_list[k][1], debtors_list[k1][1] = balance, 0
                k1 += 1    
            elif debtors_list[k1][1] != 0 and debtors_list[k1][1] > value[1]:
                debtors_list[k1].append([creditors_list[k][0], value[1]])
                debt = round(debtors_list[k1][1] - value[1],2)
                creditors_list[k][1], debtors_list[k1][1] = 0, debt

    # displaying a list of debtors
    for debtor in debtors_list:
        s=[]
        k=2
        number_of_debtor = len(debtor)
        while k < number_of_debtor:
            s.append(f"{debtor[k][0]} guest - {debtor[k][1]}$")
            k += 1
        s=", ".join(s)
        print(f"{debtor[0]} guest owes: {s}.")
else:
    print("No one owes nothing to nobody.")


