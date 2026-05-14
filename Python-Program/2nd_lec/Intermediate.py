# # 1.Write a program to calculate factorial using a for loop.
# no = int(input("Enter a Number:"))
# fact = 1
# for i in range(1, no+1) :
#     fact = fact * i
# print("factorial:",fact)
    

# # 2.Find the sum of all even numbers from 1 to N.
# no = int(input("Enter a Number:"))
# sum = 0
# for i in range (1 , no+1) :
#     if i % 2 == 0:
#         sum = sum + i
# print("Sum is:",sum)


# # 3.Take a string input and count the number of vowels.
# Str = input("Enter String:")
# vowel = "aeiouAEIOU"
# count = 0
# for Char in Str:
#     if Char in vowel:
#         count = count + 1
#         print ("Numberr of Vowel count:",count)



# # 4.Write a program to check if a number is prime.
# no  =  int(input("Enter Number:"))
# if no > 1:
#     for i in range (2 , no):
#      if no % i == 0:
#         print("Number is not prime")
#         break
#     else :
#         print("Number is prime")


# # 5.Print all numbers between 1 and 50 divisible by 3 using a loop.
# for i in range (1,51):
#    if i % 3 == 0 :
#     print (i)

# # 6.Take three numbers as input and print the largest using if-elif-else.
# No1 = float(input("Enter a number: "))
# No2 = float(input("Enter a number: "))
# No3 = float(input("Enter a number: "))
# if No1 > No2 and No1 > No3 :
#     print("No1 is greater")
# elif No2 > No1 and No2 > No3 :
#     print("No2 is greater") 
# else : 
#     print("No3 is grater")  

# # 7.Print the first N terms of the Fibonacci series.
# NO = int(input("Enter Number:"))
# a = 0
# b = 1
# for i in range (NO):
#     print(a)
#     c = a + b
#     a = b
#     b = c

# # 8.Write a program to calculate the sum of the digits of a number.
# no = int(input("Enter a number: "))
# sum = 0

# while no > 0:
#     digit = no % 10
#     sum = sum + digit
#     no = no // 10

# print("Sum of digits:", sum)

# # 9.Take numbers as input in a loop and break when a negative number is entered. Print the sum of all numbers entered before a negative.
# sum =0
# while True:
#     No = int(input("Enter number:"))
#     if No < 0 :
#         break
#     sum = sum +  No
#     print("Ans :",sum)


# # 10.Print numbers from 1 to 20, but skip multiples of 5 using continue.
# for i in range (1 , 21):
#     if  i % 5 == 0:
#         continue
#     print(i)
