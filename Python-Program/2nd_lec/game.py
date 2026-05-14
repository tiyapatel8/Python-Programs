# Guess the number 
# import random

# print("🎮 Welcome to Guess the Number Game!")

# number = random.randint(1, 100)
# guess = 0
# attempts = 0

# while guess != number:
#     guess = int(input("Enter your guess (1-100): "))
#     attempts += 1

#     if guess > number:
#         print("Too high! 📈 Try again.")
#     elif guess < number:
#         print("Too low! 📉 Try again.")
#     else:
#         print("🎉 Correct! You guessed it in", attempts, "attempts.")

# print("Thanks for playing 😊")


#  /////////////////////////////////////////
# Tic-Tac-Toe
# Tic-Tac-Toe Game (2 Players)
# board = [" ", " ", " ",
#          " ", " ", " ",
#          " ", " ", " "]

# def print_board():
#     print()
#     print(board[0], "|", board[1], "|", board[2])
#     print("--+---+--")
#     print(board[3], "|", board[4], "|", board[5])
#     print("--+---+--")
#     print(board[6], "|", board[7], "|", board[8])
#     print()

# def check_winner(player):
#     if (board[0]==board[1]==board[2]==player or
#         board[3]==board[4]==board[5]==player or
#         board[6]==board[7]==board[8]==player or
#         board[0]==board[3]==board[6]==player or
#         board[1]==board[4]==board[7]==player or
#         board[2]==board[5]==board[8]==player or
#         board[0]==board[4]==board[8]==player or
#         board[2]==board[4]==board[6]==player):
#         return True
#     return False

# player = "X"

# for turn in range(9):
#     print_board()
    
#     move = int(input(f"Player {player}, choose position (1-9): ")) - 1
    
#     if board[move] == " ":
#         board[move] = player
#     else:
#         print("Position already taken! Try again.")
#         continue

#     if check_winner(player):
#         print_board()
#         print(f"🎉 Player {player} wins!")
#         break

#     if player == "X":
#         player = "O"
#     else:
#         player = "X"

# else:
#     print_board()
#     print("It's a draw!")


# ////////////////////////////////////
# Math Quiz Game

import random

print("🧠 Welcome to Math Quiz Game!")

score = 0

for i in range(5):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    print(f"\nQuestion {i+1}: {num1} + {num2} = ?")
    
    answer = int(input("Your answer: "))
    
    correct = num1 + num2

    if answer == correct:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! Correct answer is:", correct)

print("\n🎉 Your final score is:", score, "/ 5")