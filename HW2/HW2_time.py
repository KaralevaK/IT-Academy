#текстовый вывод времени
import datetime
import re
from datetime import datetime, date, time

dict = {1:"один",
        2:"два",
        3:"три",
        4:"четыре",
        5:"пять",
        6:"шесть",
        7:"семь",
        8:"восемь",
        9:"девять",
        10:"десять",
        11:"одинадцать",
        12:"двенадцать",
        13:"тринадцать",
        14:"четырнадцать",
        15:"пятнадцать",
        16:"шестнадцать",
        17:"семнадцать",
        18:"восемнадцать",
        19:"девятнадцать",
        20:"двадцать",
        30:"тридцать",
        40:"сорок",
        50:"пятьдесят"}

while True:
    option = input("Введите \"1\" для вывода текущего времени, \"2\" - для ввода времени вручную, \"3\" - для выхода из программы:")
    
    if option == "1" or option == "2":
        # получение текущего времени
        if option == "1":
            hour = datetime.today().time().hour
            minute = datetime.today().time().minute
            
        # ввод времени пользователем
        else:
            while True:
                user_time = input("Введите время в формате hh:mm : ")
                if re.fullmatch("\d\d:\d\d",user_time): 
                    hour = int(user_time[0:2])
                    minute = int(user_time [3:5])
                    if hour in range(0,24) and minute in range(0,60):
                        break
                print("Проверьте введенные данные.") 
        # подсчет часов
        if hour > 12:
                hour = hour-12

        if minute == 0:
            if hour == 12:
                print("Полдень")
            elif hour == 0:
                print("Полночь")
            else:
                if hour == 1:
                    hour_word = "час"
                elif hour >= 2 and hour <=4:
                    hour_word = "часа"
                else:
                    hour_word = "часов"
                print(f"Время: {dict[hour]} {hour_word} ровно")
        else: 
            if hour == 12:
                hour = 1
            else:
                hour += 1
        
            if minute > 0 and minute < 45:
            
                if hour == 1:
                    hour_word = "первого"
                elif hour == 2:
                    hour_word = "второго"
                elif hour == 3:
                    hour_word = "третьего"
                elif hour == 4:
                    hour_word = "четвертого"
                elif hour == 7:
                    hour_word = "седьмого"
                elif hour == 8:
                    hour_word = "восьмого"
                else:
                    hour_word = dict[hour][:len(dict[hour])-1]+"ого"
                       
                if minute == 30:
                    print(f"Время: половина {hour_word}")
                else:
                    # построение числительного
                    if minute > 20:
                        minute_word = f"{dict[(minute//10)*10]} {dict[minute % 10]}"
                    else:
                        minute_word = dict[minute]
                    # подбор окончания и нужной формы слова "минут"
                    if minute_word[len(minute_word)-4:] == dict[1]:
                        minute_word = minute_word.replace(dict[1], "одна минута")
                    elif minute_word[len(minute_word)-3:] == dict[2]:
                        minute_word = minute_word.replace(dict[2], "две минуты")
                    elif minute_word[len(minute_word)-3:] == dict[3] or minute_word[len(minute_word)-6:] == dict[4]:
                        minute_word = f"{minute_word} минуты"
                    else:
                        minute_word = f"{minute_word} минут"
                    print(f"Время: {minute_word} {hour_word} ")

            if minute >= 45:
                minute = 60 - minute
                if minute == 1:
                    minute_word = "одной минуты"
                elif minute == 2:
                    minute_word = "двух минут"
                elif minute in [3,4]:
                    minute_word = f"{dict[minute][:len(dict[minute]-1)]}ёх минут"
                elif minute == 8:
                    minute_word = "восьми минут"
                else:
                    minute_word = f"{dict[minute][:len(dict[minute])-1]}и минут"

                if hour == 1:
                    hour_word = "час"
                else:
                    hour_word = dict[hour]
                print(f"Время: Без {minute_word} {hour_word} ")

    elif option == "3":
        print("Завершение работы.")
        break
    else:
        print("Проверьте вводимые данные.")