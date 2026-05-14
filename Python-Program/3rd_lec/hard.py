# # 1.Longest word in a string
# s = input("Enter a sentence: ")
# words = s.split()
# longest = ""
# for w in words:
#     if len(w) > len(longest):
#         longest = w
# print("Longest word:", longest)

# # 2.Basic calculator
# expression = input("Enter expression: ")
# a, op, b = expression.split()
# a = int(a)
# b = int(b)
# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "*":
#     print(a * b)
# elif op == "/":
#     print(a / b)

# # 3.Flatten nested list
# def flatten(lst):
#     result = []
#     for i in lst:
#         if isinstance(i, list):
#             result.extend(flatten(i))
#         else:
#             result.append(i)
#     return result
# nested = [1, [2, [3, 4], 5], 6]
# print(flatten(nested))

# # 4. Dictionary with factorial values
# def fact(n):
#     f = 1
#     for i in range(1, n+1):
#         f *= i
#     return f
# nums = list(map(int, input("Enter numbers: ").split()))
# result = {}
# for n in nums:
#     result[n] = fact(n)
# print(result)

# # 5. Palindrome (ignore spaces & case)
# s = input("Enter a string: ")
# clean = s.replace(" ", "").lower()
# if clean == clean[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # 6. Anagrams of first string
# words = input("Enter words: ").split()
# first = sorted(words[0])
# result = []
# for w in words:
#     if sorted(w) == first:
#         result.append(w)
# print(result)

# # 7. Number pyramid
# n = int(input("Enter number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# # 8. Dictionary where key are words and value are length 
# s = input("Enter a sentence: ")
# words = s.split()
# result = {}
# for w in words:
#     result[w] = len(w)
# print(result)

# # 9. Queue using list
# queue = []
# while True:
#     print("1.Enqueue 2.Dequeue 3.Exit")
#     choice = int(input("Enter choice: "))
#     if choice == 1:
#         val = input("Enter value: ")
#         queue.append(val)
#     elif choice == 2:
#         if queue:
#             print("Removed:", queue.pop(0))
#         else:
#             print("Queue empty")
#     else:
#         break
#     print("Queue:", queue)

# # 10. Pairs where sum is even
# nums = list(map(int, input("Enter numbers: ").split()))
# pairs = []
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if (nums[i] + nums[j]) % 2 == 0:
#             pairs.append((nums[i], nums[j]))
# print("Pairs:", pairs)