num1 = float(input('1st number '))
operator = input("enter operator  ")
num2 = float(input('2nd number '))

if operator == "+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("invalid operator")
