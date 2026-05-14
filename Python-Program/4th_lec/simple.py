# # 1. Create a tuple of 5 fruits and print the first and last fruit.
# fruits= ("Mango","Grapes","Orange","Apple","Banana")
# print("First:",fruits[0])
# print("Last:",fruits[-1])

# # 2. Create a set of 10 numbers and remove all duplicates.
# nums = {1,2,3,4,5,6,4,3,3,2}
# print("Numbers:",nums)

# # 3. Create a dictionary of 3 students with their marks and print the marks of a given student.
# stud = {"Tiya":90 , "Riya" : 46 , "Keya" :89}
# name = input("Enter student name:")
# print(stud[name])

# # 4. Write a function `greet_user(name)` that prints a greeting for the given name.
# def greet_user(name):
#     print("Hello,",name)
# greet_user("Tiya")

# # 5. Create a list of 5 numbers and print their squares using a lambda function and `map()`.
# nums = [1,2,3,4,5]
# square = list(map(lambda x:x*x,nums))
# print(square)

# # 6. Create a dictionary of names and ages; update the age of one person and print the dictionary.
# student = {"Tiya" : 21 , "Priya" : 22, "Jiya" :24}
# print("Before :",student)
# student["Jiya"] = 20
# print("After update",student)

# # 7. Use a generator function to yield the first 5 even numbers.
# def even_numbers():
#     for i in range(2, 11, 2):
#         yield i
# for num in even_numbers():
#     print(num)

# # 8. Create a set of 5 colors and check if a color `"blue"` exists in it.
# set = {"Pink","Yellow","blue","Green","Black"}
# if "blue" in set:
#     print("Blue exist")

# # 9. Create a tuple of numbers and count how many times a particular number occurs.
# nums = 2,3,4,3,2,4,2
# print("Count 2 in :",nums.count(2))

# # 10. Use a for loop to iterate over a dictionary of fruits and their prices, printing each key and value.
# fruits = {"Apple":70 , "Mango" : 100}
# for i in fruits :
#     print(i,fruits[i])