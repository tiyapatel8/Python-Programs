# # 1.Check whether a given string is a palindrome.
# Str = input("Enter a String:")
# if Str == Str[::-1] :
#     print("String is pallindrom :", Str)


# # 2.Calculate the GCD using loops and if-else statements.
# no1 = int(input("Enter first number: "))
# no2 = int(input("Enter second number: "))
# small = no1 if no1 < no2 else no2
# gcd = 1
# for i in range(1, small + 1):
#     if no1 % i == 0 and no2 % i == 0:
#         gcd = i
# print("GCD is:", gcd)

# # 3.Take a string and count the number of words.
# Str = input("Enter a String:")
# word = Str.split()
# print(len(word))

# # 4.Print the following pattern for N = 5.
# for i in range(1, 6):
#     print("*" * i)

# # 5.Reverse a given integer without converting it to a string.
# num = int(input("Enter Number: "))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print("Reverse Number:", reverse)

# # 6.Take N numbers as input and print the sum of their squares.
# N = int(input("How many numbers you want to enter: "))
# total = 0
# for i in range(N):
#     num = int(input("Enter number: "))
#     total = total + (num * num)
# print("Sum of squares is:", total)

# # 7.Check whether a number is an Armstrong number.
# num = int(input("Enter Number: "))
# temp = num
# sum = 0
# digits = len(str(num))
# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** digits
#     temp = temp // 10
# if sum == num:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

# # 8.Count the frequency of each character in a string.
# Str = input("Enter String: ")

# for char in set(Str):
#     print(char, ":", Str.count(char))

# # 9.Print all odd numbers from 50 down to 1 using a loop.
# for i in range( 50 ,0,-1):
#     if i % 2 != 0:
#         print(i)
        
# # 10.Build a basic calculator that takes two numbers and an operator and performs the operation.
# no1 = float(input("Enter No1:"))
# no2 = float(input("Enter No2:"))

# Sum = no1 + no2
# print("Sum:",Sum)

# Sub = no1 -  no2
# print("Sub:",Sub)

# Mul = no1 * no2
# print("Multiplication:",Mul)

# Div = no1 / no2
# print("Division:",Div)

# Mod = no1 % no2
# print("MOd:",Mod)