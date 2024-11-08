
print("1.Addition - Click 1 to See this solution of Addition")
print("2.Subtraction- Click 2 to See this solution of Subtraction")
print("3.Multiplication-Click 3 to See this solution of Multiplication")
print("4.Division-Click 4 to See this solution of Division")
print()

option= int(input("Select option an Basic Calculator Operation : "))
if option==1:
    num1=int(input("Enter first number as you wish : "))
    num2 = int(input("Enter second number as you wish : "))
    num3=num1+num2
    #Addition : ",num3
    print("Addition : "+str(num3))

elif option == 2:
    num4 = int(input("Enter first number as you wish : "))
    num5 = int(input("Enter second number as you wish : "))
    num6 = num4 - num5
    #Subtraction : ",num6
    print("Subtraction : " + str(num6))

elif option == 3:
    num7 = int(input("Enter first number as you wish : "))
    num8 = int(input("Enter second number as you wish : "))
    num9 = num7 * num8
    #Multiplication : ",num9
    print("Multiplication : " + str(num9))

elif option == 4:
    num10 = int(input("Enter first number as you wish : "))
    num11 = int(input("Enter second number as you wish : "))
    num12 = num10 / num11
    #Division : ",num9
    print("Division : " + str(num12))

else:
    print("Invalid Input")


