# # 1. Create a dictionary comprehension where keys are numbers 1–10 and values are cubes of the keys.
# nums = {x: x**3 for x in range(1, 11)}
# print(nums)

# # 2. Write a function that accepts variable-length arguments and returns their sum.
# def total(*numbers):
#    return sum(numbers)
# print(total(1,2,3,4))

# # 3. Create a generator function that yields the Fibonacci sequence up to n terms.
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
# for num in fibonacci(10):
#     print(num)

# # 4. Use `filter()` to select all odd numbers from a list of 1–20.
# nums = list(range(1, 21))
# odd = list(filter(lambda x: x % 2 != 0, nums))
# print(odd)

# # 5. Use `reduce()` to multiply all numbers in a list of 1–5.
# from functools import reduce
# ans = reduce(lambda x,y:x*y ,[1,2,3,4,5])
# print(ans)

# # 6. Write a lambda function that checks if a number is prime, and use it with `filter()` on a list of numbers 1–20.
# nums = list(range(1,21))
# prime = list(filter(lambda x:x > 1 and all(x % i != 0 for i in range(2,x)),nums))
# print(prime)

# # 7. Merge two dictionaries using dictionary comprehension.
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# merged = {k: v for d in (d1, d2) for k, v in d.items()}
# print(merged)

# # 8. Create a set of numbers 1–10 and print numbers that are common with another set {5, 6, 7, 8}.
# s1 = set(range(1,11))
# s2 = {5,6,7,8}
# print(s1 & s2)

# # 9. Create a nested dictionary to store 3 students with their marks in 2 subjects each. Print total marks for each student.
# students = {
#     "Tiya": {"math": 80, "eng": 70},
#     "Riya": {"math": 85, "eng": 75},
#     "Priya": {"math": 60, "eng": 65}
# }
# for name in students:
#     total = students[name]["math"] + students[name]["eng"]
#     print(name, "Total:", total)

# # 10. Write a function with default arguments to calculate the area of a rectangle, defaulting to 1 if width is not provided.
# def area (length,width=1):
#     return length * width
# print(area(20))
# print(area(2,3))
