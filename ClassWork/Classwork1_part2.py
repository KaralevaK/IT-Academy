#строка числительных
l = input("Введите строку, содержащую числительные больше 0 и меньше 21 через пробел:").split(" ")
print(f"Строка, преобразованная в коллекцию:\n{l}")
while  l.count("one")>0:
    l.insert(l.index("one")+1, 1)
    l.pop(l.index("one"))
while  l.count("two")>0:
    l.insert(l.index("two")+1, 2)
    l.pop(l.index("two"))
while  l.count("three")>0:
    l.insert(l.index("three")+1,3)
    l.pop(l.index("three"))
while  l.count("four")>0:
    l.insert(l.index("four")+1, 4)
    l.pop(l.index("four"))
while  l.count("five")>0:
    l.insert(l.index("five")+1, 5)
    l.pop(l.index("five"))
while  l.count("six")>0:
    l.insert(l.index("six")+1, 6)
    l.pop(l.index("six"))
while  l.count("seven")>0:
    l.insert(l.index("seven")+1, 7)
    l.pop(l.index("seven"))
while  l.count("eight")>0:
    l.insert(l.index("eight")+1, 8)
    l.pop(l.index("eight"))
while  l.count("nine")>0:
    l.insert(l.index("nine")+1, 9)
    l.pop(l.index("nine"))
while  l.count("ten")>0:
    l.insert(l.index("ten")+1, 10)
    l.pop(l.index("ten"))
while  l.count("eleven")>0:
    l.insert(l.index("eleven")+1, 11)
    l.pop(l.index("eleven"))
while  l.count("twelve")>0:
    l.insert(l.index("twelve")+1, 12)
    l.pop(l.index("twelve"))
while  l.count("thirteen")>0:
    l.insert(l.index("thirteen")+1, 13)   
    l.pop(l.index("thirteen")) 
while  l.count("fourteen")>0:
    l.insert(l.index("fourteen")+1, 14) 
    l.pop(l.index("fourteen"))  
while  l.count("fifteen")>0:
    l.insert(l.index("fifteen")+1, 15)  
    l.pop(l.index("fifteen")) 
while  l.count("sixteen")>0:
    l.insert(l.index("sixteen")+1, 16)  
    l.pop(l.index("sixteen")) 
while  l.count("seventeen")>0:
    l.insert(l.index("seventeen")+1, 17) 
    l.pop(l.index("seventeen"))  
while  l.count("eighteen")>0:
    l.insert(l.index("eighteen")+1, 18) 
    l.pop(l.index("eighteen"))  
while  l.count("nineteen")>0:
    l.insert(l.index("nineteen")+1, 19) 
    l.pop(l.index("nineteen"))  
while  l.count("twenty")>0:
    l.insert(l.index("twenty")+1, 20)  
    l.pop(l.index("twenty")) 
   
print(f"Коллекция, в которой элементы преобразованы в числа:\n{l}")
print(f"Коллекция, из которой исключены дубликаты:\n{set(l)}")
l=sorted(list(set(l)))
print(f"Коллекция, элементы которой отсортированы по возрастанию:\n{l}")
# добавление для хранения индекса элемента в конец списка
l.append(0)
print("Последовательность произведение-сумма:")
while l[len(l)-1] < len(l)-2:
    print(l[l[len(l)-1]]*l[l[len(l)-1]+1]) if (l[len(l)-1]+1)%2 != 0 else print(l[l[len(l)-1]]+l[l[len(l)-1]+1])
    l[len(l)-1] += 1
# добавление для хранения суммы элемента в конец списка
l.append(0)
l[len(l)-2]=0
while l[len(l)-2] < len(l)-2:
    if l[l[len(l)-2]]%2 != 0:
        l[len(l)-1] += l[l[len(l)-2]]
    l[len(l)-2] += 1     
print(f"Сумма нечетных чисел:{l[len(l)-1]}")
   