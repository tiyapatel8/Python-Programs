# # 1.print each character on a new line.
# Str = input("Enter a string:")
# for Char in Str :
#     print(Char)


# # 2.Count the number of spaces.
# Str = input("Enter a string:")
# count = 0
# for Char in Str:
#     if Char == " ":
#         count = count + 1
# print("Total Space :", count)

# # 3.Reverse a string without using slicing ([::-1]).
# Str = input("Enter a string:")
# rev = ""
# for Char in Str:
#    rev = Char + rev
# print("Reverse string =",rev)
   
# # 4.Create a list of 5 numbers and print the sum of all elements.
# num = []
# for i in range (5):
#    n = int(input("Enter number:"))
#    num.append(n)
# print("Sum :",sum(num))
   
# # 5.print only the positive numbers.
# nums = [int(x) for x in input("Enter numbers: ").split()]
# for n in nums:
#     if n > 0:
#         print(n)

# # 6.Take two strings and concatenate them with a space in between.
# Str1 = input("Enter String:")
# Str2 = input("Enter String:")
# print("Concatenated String is :",Str1+ " "+Str2)

# # 7.Print the first and last character of a given string.
# Str = input("Enter a string:")
# if len(Str) > 0:
#     print("First character:", Str[0])
#     print("Last character:", Str[-1])
# else:
#     print("String is empty")

# # 8.Create a list of 10 integers and print the maximum and minimum values.
# nums = []
# for i in range(10):
#     n = int(input("Enter number: "))
#     nums.append(n)
# print("Maximum No:", max(nums))
# print("Minimum No:", min(nums))

# # 9.Take a number n and print a list of the first n even numbers.
# n = int(input("Enter value of n: "))
# even = []
# for i in range(1, n + 1):
#     even.append(2 * i)
# print(even)

# # 10.Take a string input and check if it starts with a vowel.
# Str = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# if Str[0] in vowels:
#     print("Starts with vowel")
# else:
#     print("Does not start with vowel")


