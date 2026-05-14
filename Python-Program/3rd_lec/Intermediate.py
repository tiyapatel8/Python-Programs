# # 1.Count the number of uppercase and lowercase letters 
# Str = input("Enter String :")
# upper = 0
# lower = 0
# for char in Str:
#     if char.isupper():
#         upper += 1
#     elif char.islower():
#         lower += 1
# print("Uppercase :", upper)
# print("Lowercase :", lower)

# # 2.Remove all vowels from  string.
# Str = input("Enter String :")
# vowels = "aeiouAEIOU"
# result = ""
# for char in Str:
#     if char not in vowels:
#         result += char
# print("Remove Vowels:",result)

# # 3.Take a list of numbers and return a list of only the prime numbers.
# nums = list(map(int, input("Enter numbers: ").split()))
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# primes = []
# for n in nums:
#     if is_prime(n):
#         primes.append(n)
# print("Prime numbers:", primes)

# # 4.Given a list of strings, print all strings with length greater than 3.
# Str = input("Enter String :").split()
# for word in Str:
#     if len(word) > 3:
#         print(word)
        
# # 5.Replace all spaces in a string with underscores.
# str = input("Enter a string: ")
# print(str.replace(" ", "_"))

# # 6.Square of list numbers.
# nums = list(map(int, input("Enter numbers: ").split()))
# squared = []
# for n in nums:
#     squared.append(n * n)
# print("Squared list:", squared)

# # 7.Given a string, print it in reverse word order.
# str = input("Enter a string: ")
# words = str.split()
# words.reverse()
# print("Reversed words:", " ".join(words))

# # 8.Merge two lists element-wise into a list of tuples.
# list1 = list(map(int, input("Enter list1: ").split()))
# list2 = list(map(int, input("Enter list2: ").split()))
# merged = list(zip(list1, list2))
# print("Merged tuples:", merged)

# # 9.Take a list of integers and move all zeros to the end.
# nums = list(map(int, input("Enter numbers: ").split()))
# non_zero = []
# zero = []
# for n in nums:
#     if n == 0:
#         zero.append(n)
#     else:
#         non_zero.append(n)
# result = non_zero + zero
# print("Result:", result)

# # 10.Take a string and print a dictionary with the count of each character.
# s = input("Enter a string: ")
# char_count = {}

# for ch in s:
#     if ch in char_count:
#         char_count[ch] += 1
#     else:
#         char_count[ch] = 1
# print(char_count)