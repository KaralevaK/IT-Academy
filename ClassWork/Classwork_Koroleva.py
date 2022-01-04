# строка числительных

dict = {"one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
        "ten":10,
        "eleven":11,
        "twelve":12,
        "thirteen":13,
        "fourteen":14,
        "fifteen":15,
        "sixteen":16,
        "seventeen":17,
        "eighteen":18,
        "nineteen":19,
        "twenty":20
       }

l = input("Введите строку, содержащую числительные больше 0 и меньше 21 через пробел:").split(" ")
print(f"Строка, преобразованная в коллекцию:\n{l}")
for i in range(len(l)):
    l[i] = dict[l[i]]     
print(f"Коллекция, элементы которой преобразованы в числа:\n{l}")
print(f"Коллекция, из которой исключены дубликаты:\n{set(l)}")
l=sorted(list(set(l)))
print(f"Коллекция, элементы которой отсортированы по возрастанию:\n{l}")
print("Последовательность произведение-сумма:")
for i in range(len(l)-1):
    print(l[i]*l[i+1]) if (i+1)%2 != 0 else print(l[i]+l[i+1])
sum = 0    
for i in l:
    if i%2 != 0:
        sum = sum + i 
print(f"Сумма нечетных чисел: {sum}")

   