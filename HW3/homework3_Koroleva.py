import os
from pathvalidate import is_valid_filename

def get_max_number():
    while True:
        number = input("Please enter maximum number of characters in a string, which have to be greater than 35: ")
        if number.isdigit() and int(number)>35:
            return int(number)
        else:
            print("Invalid value. Try again.")
            
def get_new_file_name():
    while True:
        new_name = input("Please enter the file name (without filename extension) to record the result:")
        new_name = f"{new_name}.txt"
        if not is_valid_filename(new_name):
            print("Invalid value. Try again.")
        elif f"{new_name}" in os.listdir():
            print("The same file name already exists. Enter another name.")
        else:
            return new_name
            

flag_error = False #длина слова больше заданной длины строки        

with open("text.txt","r",encoding='utf-8') as f:
    max_len_string = get_max_number()
    s = f.read()
    s = s.split('\n')
    s_write = []
    
    for i in range(0,len(s)):
        s_temp = s[i].split()

        for s1 in s_temp:
            if len(s1) > max_len_string:
                flag_error = True
                break
         
        while s_temp:
            string_write=s_temp[0]
            s_temp.pop(0)
            while s_temp and len(string_write)+len(s_temp[0])+1 <= max_len_string:
                string_write =f"{string_write} {s_temp[0]}"
                s_temp.pop(0)
            s_write.append(string_write)    
        else:
            s_write.append(False)
       
if flag_error:
    print("One of the words is longer than maximum number of characters in a string. Try again.")
else:
    
    for i,string_write in enumerate(s_write):
        
        if string_write:
            if s_write[i+1] and len(string_write) < max_len_string:
                s_temp = string_write.split()
                spaces_in = len(s_temp) - 1
                spaces_add = max_len_string - len(string_write) 
                sep=" "*(spaces_add//spaces_in+1)
                spaces_add -= spaces_in*(spaces_add//spaces_in)

                if spaces_add > 0:
                    j=0
                    while spaces_add > 0:
                        s_temp[j]=f"{s_temp[j]} "
                        j += 1
                        spaces_add -= 1
                string_write=sep.join(s_temp) 
            
            s_write[i]=string_write
    f_rezult = get_new_file_name()   
    with open(f_rezult, "w",encoding='utf-8') as f:
        for row in s_write:
            if row:
                f.write(f"{row}\n")
        print(f"Formatted text is written to a file \"{f_rezult}\"")



        

