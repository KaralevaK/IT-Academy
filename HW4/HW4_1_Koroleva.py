# list transformation
def get_list():
    flag = True
    while flag:
        l=input("Enter, using a comma, a non-empty list of non-repeating integers:\n")
        if len(l) != 0:
            flag = False
            l=l.split(",")
        else:
            print("The list is empty!")
    l=[int(x) for x in l]
    l=sorted(list(set(l)))
    return l

def get_ranges(l):
    s=[]
    while len(l) > 0:
        s1=""
        k=0
        while k<len(l)-1 and abs(l[k+1]-l[k]) == 1:
            k +=1
        if k > 0:
            s1=f"{l[0]} \u2014 {l[k]}"
            while k >= 0:
                l.pop(0)
                k -= 1
        else:
            s1=str(l[0])
            l.pop(0)
        s.append(s1)
    return ", ".join(s) 

print(f"Result: {get_ranges(get_list())}")