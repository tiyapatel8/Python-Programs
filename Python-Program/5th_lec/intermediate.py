# # 1. Name Shortener App
# name = input("Enter Name:")
# words = name.split()
# for i in words:
#     print(i[0].upper(),end=".")

# # 2. Restaurant Menu System
# menu={
#     "Pizza":200,
#     "Burger":150,
#     "Sandwich":100
# }
# total = 0 
# item = input("Enter Item Name:")
# if item in menu:
#     total += menu[item]
#     print("Total Cost:",total)
# else:
#     print("Item not found.")

# # 3. Email Validator
# email = input("Enter email: ")
# if "@" in email and email.endswith(".com"):
#     print("Valid")
# else:
#     print("Invalid")

# # 4. Unique Words Extractor
# str = input("Enter Sentance:")
# words = str.lower().split()
# unique_words = set(words)
# print(unique_words)

# # 5. Class Marks Tracker
# stud ={}
# for i in range(5):
#     name = input("Enter Student Name:")
#     marks = input("Enter Students marks:")
#     stud[name] = marks
# topper = max(stud, key=stud.get)
# print("Topper is:",topper)

# # 6. Bus Seat Allocation
# seat = ["Empty"] * 10
# seat_no = int(input("Enter seat no from 0 to 9:"))
# if seat[seat_no] == "Empty":
#     seat[seat_no] = "Booked"
#     print(seat)
# else :
#     print("This seat is already booked ")

# # 7. Vowel Counter
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for i in text:
#         if i in vowels:
#             count += 1
#     return count
# string = input("Enter string: ")
# print("Total vowels:", count_vowels(string))

# # 8. Fruit Basket Organizer
# fruits = ("apple" , "banana","apple","graps","apple","banana")
# fruit_name = input("Enter fruit name:")
# print("Fruits Count:",fruits.count(fruit_name))

# # 9. Password Strength Checker
# password = input("Enter password: ")
# upper = False
# lower = False
# digit = False
# special = False
# for i in password:
#     if i.isupper():
#         upper = True
#     elif i.islower():
#         lower = True
#     elif i.isdigit():
#         digit = True
#     else:
#         special = True
# if upper and lower and digit and special:
#     print("Strong Password")
# else:
#     print("Weak Password")

# # 10. Student Subject Selection
# math ={"Tiya" , "Priya" , "Jiya"}
# science = {"Kavya", "Tiya" , "Henal"}
# print("Student in both:",math & science)
# print("Only Math student:",math-science)
# print("Only Sciece Student:",science - math)