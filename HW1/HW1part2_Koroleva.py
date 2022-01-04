# решение кубического уравнения с использованием тригонометрической формулы Виета 

import math
import numpy
# ввод исходных данных и точности
print("Введите коэффициенты кубического уравнения: a*x^3+b*x^2+c*x+d=0")
a,b,c,d = float(input("a=")), float(input("b=")), float(input("c=")), float(input("d="))
accuracy = int(input("Введите точность вычисления (количество знаков после запятой): "))
# решение квадратного уравнения в случае a = 0
if a == 0:
    if b != 0:
        Discr=c**2-4*b*d
        if Discr > 0:
            x1 = (-c+Discr**0.5) / (2*b)
            x2 = (-c-Discr**0.5) / (2*b)
            print(f"Корни уравнения: x1 = {round(x1,accuracy)}, x2 = {round(x2,accuracy)}")
        elif Discr==0:
            x = -c/(2*b)
            print(f"Корень уравнения x = {round(x,accuracy)}")
        elif Discr < 0:
            print('Нет корней')
    else:
        if c != 0:
            x = -d/c
            print(f"Корень уравнения x={round(x,accuracy)}")
        else:
            print("Проверьте правильность ввода!")
# решение кубического уравнения в случае а != 0

# 
elif b == 0 and c == 0 and ((a > 0 and d < 0) or (a < 0 and d > 0)):
     x = math.pow(-d/a,1/3)
     print(f"Корень уравнения х={round(x,accuracy)}")

# приведение к виду x^{3}+ax^{2}+bx+c=0    
else:
    t = a
    a = b/t
    b = c/t
    c = d/t
    Q = (math.pow(a,2)-3*b)/9
    R = (2*math.pow(a,3)-9*a*b+27*c)/54
    S = math.pow(Q,3)-math.pow(R,2)
    if S > 0:
        corner = math.acos(R/math.pow(Q,3/2))/3
        x1 = -2*math.sqrt(Q)*math.cos(corner)-a/3
        x2 = -2*math.sqrt(Q)*math.cos(corner+(2/3)*math.pi)-a/3
        x3 = -2*math.sqrt(Q)*math.cos(corner-(2/3)*math.pi)-a/3
        print(f"Уравнение имеет три действительных корня: x1 = {round(x1,accuracy)}, x2 = {round(x2,accuracy)}, x3 = {round(x3,accuracy)}")
    elif S < 0:
        if Q > 0:
            corner = math.acosh(abs(R)/math.pow(Q,3/2))/3
            # вычисление действительного корня
            x1 = -2*numpy.sign(R)*math.sqrt(Q)*math.cosh(corner)-a/3
            # вычисление комплексных корней
            x2 = complex(round(numpy.sign(R)*math.sqrt(Q)*math.cosh(corner)-a/3,accuracy), round(math.sqrt(3)*math.sqrt(Q)*math.sinh(corner),accuracy))
            x3 = x2.conjugate()
            
        elif Q < 0:
            corner = math.asinh(abs(R)/math.pow(abs(Q),3/2))/3
            # вычисление действительного корня
            x1 = -2*numpy.sign(R)*math.sqrt(abs(Q))*math.sinh(corner)-a/3
            # вычисление комплексных корней
            x2 = complex(round(numpy.sign(R)*math.sqrt(abs(Q))*math.sinh(corner)-a/3,accuracy), round(math.sqrt(3)*math.sqrt(abs(Q))*math.cosh(corner),accuracy))
            x3 = x2.conjugate()
         
        else:
            # вычисление действительного корня
            x1 = -math.pow(c-math.pow(a,3)/27,1/3)-a/3
            # x1 = -(c-math.pow(a,3)/27)**(1/3)-(a/3)
            # вычисление комплексных корней
            x2 = complex(round(-(a+x1)/2,accuracy),round((abs((a-3*x1)*(a+x1)-4*b)**(1/2))/2,accuracy))
            x3 = x2.conjugate()
            
        print(f"Действительный корень: x1 = {round(x1,accuracy)}, комплексные корни: x2 = {x2}, x3 = {x3}")
    else:
        # уравнение вырождено
        x1 = -2*numpy.sign(R)*math.sqrt(Q)-a/3
        x2 = numpy.sign(R)*math.sqrt(Q)-a/3
        print(f"Корни уравнения: x1 = {round(x1,accuracy)}, x2 = {round(x2,accuracy)}")
