# # # 1. Online Store Inventory
# inventory = {
#     "Pen": {"price": 10, "qty": 50},
#     "Book": {"price": 40, "qty": 20},
#     "Bag": {"price": 500, "qty": 10}
# }
# bill = 0
# item = input("Enter item name: ")
# qty = int(input("Enter quantity: "))
# if item in inventory:
#     if inventory[item]["qty"] >= qty:
#         cost = inventory[item]["price"] * qty
#         inventory[item]["qty"] -= qty
#         bill += cost
#         print("Final Bill:", bill)
#     else:
#         print("Not enough stock")
# else:
# #     print("Item not found")

# # 2. Movie Ratings Aggregator
# movies = {
#     "KGF": [4, 5, 5],
#     "Pushpa": [5, 4, 4],
#     "Leo": [3, 4, 5]
# }
# def average_rating(data):
#     for movie in data:
#         avg = sum(data[movie]) / len(data[movie])
#         print(movie, "Average Rating:", avg)
# average_rating(movies)

# # 3. Electricity Bill Generator
# def calculate_bill(units):
#     if units <= 100:
#         bill = units * 5
#     elif units <= 200:
#         bill = (100 * 5) + ((units - 100) * 8)
#     else:
#         bill = (100 * 5) + (100 * 8) + ((units - 200) * 10)
#     return bill
# units = int(input("Enter units: "))
# print("Electricity Bill =", calculate_bill(units))

# # 4. Word Frequency Counter
# text = input("Enter paragraph: ").lower()
# words = text.split()
# freq = {
#     word: words.count(word)
#     for word in words
# }
# print(freq)

# # 5. Email ID Formatter
# names = ["Tiya Chaudhary","Riya Patel","Priya Shah"]
# emails = list(
#     map(
#         lambda x:x.lower().replace(" ", ".") + "@college.com",names
#     )
# )
# print(emails)

# # 6. Duplicate Remover using Sets
# items = [1,2,3,4,2,1,5,6,3,7]
# result = sorted(set(items))
# print(result)

# # 7. Fibonacci Generator App
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
# fib = fibonacci()
# for i in range(10):
#     print(next(fib))

# # 8. Student Report Card System
# students = {
#     "Tiya": {"math": 90, "eng": 80},
#     "Riya": {"math": 70, "eng": 75},
#     "Priya": {"math": 85, "eng": 95}
# }
# def student_average(data):
#     for name in data:
#         avg = (
#             data[name]["math"] + data[name]["eng"]) / 2
#         print(name, "Average:", avg)
# student_average(students)

# # 9. Employee Salary Processor
# from functools import reduce
# employees = [20000, 35000, 50000, 15000]
# high_salary = list(
#     filter(lambda x: x > 30000,employees
#     )
# )
# print("Salary above threshold:", high_salary)
# total = reduce(
#     lambda x, y: x + y,
#     employees
# )
# print("Total Salary Expense:", total)

# # 10. Crypto Price Tracker
# crypto = {
#     "Bitcoin": 5000000,
#     "Ethereum": 250000,
#     "Solana": 15000
# }
# def highest_crypto(data):
#     highest = max(data, key=data.get)
#     return highest
# print(
#     "Highest Price Crypto:",
#     highest_crypto(crypto)
# )