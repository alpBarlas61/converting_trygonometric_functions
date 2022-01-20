import math
from urllib.parse import DefragResult

#define the loop value
loop='yes'

while(loop=='yes'):

    print("Enter 1 to choose cos() function.")
    print("Enter 2 to choose sin() function.")
    print("Enter 3 to choose tan() function.")
    print("Enter 4 to choose cot() function.")
    print("Enter 5 to choose sec() function.")
    print("Enter 6 to choose csc() function.")

    function = int(input("Enter the function number :"))

    if function == 1 :
        print("cos() function was chosed.")
    
    elif function == 2:
        print("sin() function was chosed.")

    elif function == 3:
        print("tan() function was chosed.")

    elif function == 4:
        print("cot() function was chosed.")

    elif function == 5:
        print("sec() function was chosed.")

    elif function == 6:
        print("csc() function was chosed.")

    else :
        print("Invalid function")

        

    degree = int(input("Enter the degree you want to calculate :"))

    #convert the degree into more basic form

    degree = degree%360

    print(f"{degree} is the basic form of your input-degree.")

    if degree>=0 and degree <= 90 :
        if function == 1:
            print(f"cos{degree} is equal to sin{90-degree}")
            print(f"cos{degree} corresponds to {math.cos(math.radians(degree))} value")

        elif function == 2:
            print(f"sin{degree} is equal to cos{90-degree}")
            print(f"sin{degree} corresponds to {math.sin(math.radians(degree))} value")

        elif function == 3:
            print(f"tan{degree} is equal to cot{90-degree}")
            print(f"tan{degree} corresponds to {math.tan(math.radians(degree))} value")

        elif function == 4:
            print(f"cot{degree} is equal to tan{90-degree}")
            print(f"cot{degree} corresponds to {math.tan(math.radians(90-degree))} value")

        elif function == 5:
            print(f"sec{degree} is equal to csc{90-degree}")
            print(f"sec{degree} corresponds to {1/(math.cos(math.radians(degree)))} value")

        elif function == 6:
            print(f"csc{degree} is equal to sec{90-degree}")
            print(f"csc{degree} corresponds to {1/(math.sin(math.radians(degree)))} value")

    elif degree>=90 and degree <= 180 :
            if function == 1:
                print(f"cos{degree} is equal to -sin{degree-90}")
                print(f"cos{degree} is equal to -cos{180-degree}")
                print(f"cos{degree} corresponds to {math.cos(math.radians(degree))} value")

            elif function == 2:
                print(f"sin{degree} is equal to cos{degree-90}")
                print(f"sin{degree} is equal to sin{180-degree} ")
                print(f"sin{degree} corresponds to {math.sin(math.radians(degree))} value")

            elif function == 3:
                print(f"tan{degree} is equal to -cot{degree-90}")
                print(f"tan{degree} is equal to -tan{180-degree}")
                print(f"tan{degree} corresponds to {math.tan(math.radians(degree))} value")

            elif function == 4:
                print(f"cot{degree} is equal to -tan{degree-90}")
                print(f"cot{degree} is equal to -tan{180-degree}")
                print(f"cot{degree} corresponds to {math.tan(math.radians(90-degree))} value")

            elif function == 5:
                print(f"sec{degree} is equal to csc{degree-90}")
                print(f"sec{degree} is equal to csc{180-degree}")
                print(f"sec{degree} corresponds to {1/(math.cos(math.radians(degree)))} value")

            elif function == 6:
                print(f"csc{degree} is equal to sec{degree-90}")
                print(f"csc{degree} is equal to sec{180-degree}")
                print(f"csc{degree} corresponds to {1/(math.sin(math.radians(degree)))} value")

    elif degree >= 180 and degree <= 270 :
            if function == 1:
                print(f"cos{degree} is equal to -cos{degree-180}")
                print(f"cos{degree} is equal to -sin{270-degree}")
                print(f"cos{degree} corresponds to {math.cos(math.radians(degree))} value")

            elif function == 2:
                print(f"sin{degree} is equal to -sin{degree-180}")
                print(f"sin{degree} is equal to -cos{270-degree} ")
                print(f"sin{degree} corresponds to {math.sin(math.radians(degree))} value")

            elif function == 3:
                print(f"tan{degree} is equal to tan{degree-180}")
                print(f"tan{degree} is equal to cot{270-degree}")
                print(f"tan{degree} corresponds to {math.tan(math.radians(degree))} value")

            elif function == 4:
                print(f"cot{degree} is equal to cot{degree-180}")
                print(f"cot{degree} is equal to tan{270-degree}")
                print(f"cot{degree} corresponds to {math.tan(math.radians(90-degree))} value")

            elif function == 5:
                print(f"sec{degree} is equal to -sec{degree-180}")
                print(f"sec{degree} is equal to -csc{270-degree}")
                print(f"sec{degree} corresponds to {1/(math.cos(math.radians(degree)))} value")

            elif function == 6:
                print(f"csc{degree} is equal to -csc{degree-180}")
                print(f"csc{degree} is equal to -sec{270-degree}")
                print(f"csc{degree} corresponds to {1/(math.sin(math.radians(degree)))} value")

    elif degree >= 270 and degree <= 360 :
        if function == 1:
            print(f"cos{degree} is equal to sin{degree-270}")
            print(f"cos{degree} is equal to cos{360-degree}")
            print(f"cos{degree} corresponds to {math.cos(math.radians(degree))} value")

        elif function == 2:
            print(f"sin{degree} is equal to -cos{degree-270}")
            print(f"sin{degree} is equal to -sin{360-degree} ")
            print(f"sin{degree} corresponds to {math.sin(math.radians(degree))} value")

        elif function == 3:
            print(f"tan{degree} is equal to -cot{degree-270}")
            print(f"tan{degree} is equal to -tan{360-degree}")
            print(f"tan{degree} corresponds to {math.tan(math.radians(degree))} value")

        elif function == 4:
            print(f"cot{degree} is equal to -tan{degree-270}")
            print(f"cot{degree} is equal to -cot{360-degree}")
            print(f"cot{degree} corresponds to {math.tan(math.radians(90-degree))} value")

        elif function == 5:
            print(f"sec{degree} is equal to csc{degree-270}")
            print(f"sec{degree} is equal to sec{360-degree}")
            print(f"sec{degree} corresponds to {1/(math.cos(math.radians(degree)))} value")

        elif function == 6:
            print(f"csc{degree} is equal to -sec{degree-270}")
            print(f"csc{degree} is equal to -csc{360-degree}")
            print(f"csc{degree} corresponds to {1/(math.sin(math.radians(degree)))} value")

    loop = input("Would ypu like to continue ?(yes/no):").lower()

print("Program is being closed..")