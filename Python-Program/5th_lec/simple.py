# # 1.Cafe Bill Calculator
# Price_of_coffeee = 100
# Price_of_sandwitch = 80
# Price_of_pastris= 50
# Coffee = int(input("Enter number of coffees:"))
# Sandwiches = int(input("Enter number sandwitches:"))
# Pastris = int(input("Enter number of pastris:"))

# Total = (Price_of_coffeee * Coffee) + (Price_of_sandwitch * Sandwiches) + (Price_of_pastris * Pastris)
# print("Total Amount :",Total)

# # 2. Temperature Converter
# Celsius = float(input("Enter Celsius: "))
# Kelvin = Celsius + 273.15
# Fahrenheit = (Celsius * 9/5) + 32
# print("Kelvin =", Kelvin)
# print("Fahrenheit =", Fahrenheit)

# # 3. Odd or Even Checker
# no = int(input("Enter number:"))
# if no  % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number is odd")

# # 4. Attendance Warning System
# classes = int(input("Enter TOtal classes:"))
# att_classes = int(input("Enter attendanced classes:"))
# per = (att_classes/classes) * 100
# print("Attandance PErcentages =",per)
# if per >= 70:
#     print("Eligible for exam")
# else:
#     print("Not eligible")

# # 5. Word Reverser
# str = input("Enter Sentence:")
# words = str.split()
# rev = words[::-1]
# ans = " ".join(rev)
# print("Reversed Sentance:",ans)

# # 6. Simple Interest Calculator
# P = float(input("Enter Principal :"))
# R = float(input("Enter rate of Interest:"))
# T = float(input("Enter Time:"))
# SI = (P * R * T) / 100
# print("SI =",SI)

# # 7. Find the Largest of Three Numbers
# no1 = int(input("Enter number1:"))
# no2 = int(input("Enter number2:"))
# no3 = int(input("Enter number3:"))

# if no1>no2 and no1>no3:
#     print("No1 is greater" ,no1)
# elif no2>no3 and no2>no1:
#     print("No2 is greate" ,no2)
# else:
#     print("No3 is greater" ,no3)

# # 8. Leap Year Checker
# year = int(input('enter year:'))
# if(year % 4 == 0):
#     print("This is leap year")
# else:
#     print("Year is not leap year")

# # 9. Shopping Discount System
# price = int(input("Enter Total amount:"))
# if price > 5000 :
#     discount = price * 0.10
#     total_amount = price - discount
#     print('discount amount=',discount)
#     print("Total amount=",total_amount)
# else:
#     print("NO discount")

# # 10. Grade Generator
# marks = int(input("Enter marks:"))
# if marks >= 90 :
#     print("A Grade")
# elif marks >=80:
#     print("B Grade")
# elif marks>=75:
#     print("C Grade")
# elif marks>=60:
#     print("D Grade")
# else:
#     print("Fail")