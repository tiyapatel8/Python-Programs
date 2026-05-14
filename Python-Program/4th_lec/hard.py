# # 1. Write a generator that produces an infinite sequence of prime numbers; use next() to get the first 10 primes.
# def prime_generator():
#     num = 2
#     while True:
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num
#         num += 1
# primes = prime_generator()
# for i in range(10):
#     print(next(primes))

# # 2. Create a dictionary comprehension to invert keys and values of a given dictionary, handling duplicate values by storing them in a list.
# d = {"a": 1, "b": 2, "c": 1}
# invert = {i: [x for x in d if d[x] == i] for i in set(d.values())}
# print(invert)

# # 3. Write a function that accepts a list of dictionaries (each representing a student with marks) and returns the student with the highest total marks.
# students = [
#     {"name": "Tiya", "math": 90, "eng": 90},
#     {"name": "Riya", "math": 90, "eng": 85},
#     {"name": "Priya", "math": 60, "eng": 75}
# ]
# def top_student(data):
#     return max(data, key=lambda x: x["math"] + x["eng"])
# print(top_student(students))

# # 4. Use map() and a lambda function to normalize a list of numbers between 0 and 1.
# nums = [10, 20, 30, 40, 50]
# min_val = min(nums)
# max_val = max(nums)
# normalized = list(map(lambda x: (x - min_val) / (max_val - min_val), nums))
# print(normalized)

# # 5. Create a tuple of tuples representing (name, score). Sort it by score using a lambda function.
# students = (("Tiya", 80), ("Riya", 95), ("Priya", 70))
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)

# # 6. Write a generator to yield all palindromic numbers between 1 and 1000.
# def palindrome_generator():
#     for i in range(1, 1001):
#         if str(i) == str(i)[::-1]:
#             yield i
# for num in palindrome_generator():
#     print(num)

# # 7. Write a function that accepts another function as a parameter and applies it to a list of numbers (demonstrating higher-order functions).
# def apply_function(func, numbers):
#     return [func(x) for x in numbers]
# nums = [1, 2, 3, 4]
# result = apply_function(lambda x: x * x, nums)
# print(result)

# # 8. Create two sets of strings and use set operations to find words unique to the first set, common words, and words unique to the second set.
# set1 = {"apple", "banana", "mango", "grapes"}
# set2 = {"banana", "kiwi", "mango", "orange"}
# print("Unique to first:", set1 - set2)
# print("Common:", set1 & set2)
# print("Unique to second:", set2 - set1)

# # 9. Write a recursive function to flatten a nested dictionary (keys can be nested dictionaries) into a single-level dictionary with tuple keys representing the path.
# def flatten_dict(d, parent_key=()):
#     items = {}
#     for k, v in d.items():
#         new_key = parent_key + (k,)

#         if isinstance(v, dict):
#             items.update(flatten_dict(v, new_key))
#         else:
#             items[new_key] = v

#     return items
# data = {
#     "a": {
#         "b": 1,
#         "c": 2
#     },
#     "d": 3
# }
# print(flatten_dict(data))

# # 10. Write a function to calculate the factorial of a number using a generator to yield intermediate factorial values, and use reduce() to compute the final result.
# from functools import reduce
# def factorial_generator(n):
#     for i in range(1, n + 1):
#         yield i
# fact = reduce(lambda x, y: x * y, factorial_generator(5))
# print(fact)