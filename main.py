import random


# 🚨 Don't change the code above 👆


#Write your code below this row 👇
def game(player1,player2,score1,score2):
    values = {
        "1": "11",
        "2": "21",
        "3": "31",
        "4": "12",
        "5": "22",
        "6": "32",
        "7": "13",
        "8": "23",
        "9": "33"
    }
    row1 = ["⬜", "⬜", "⬜"]
    row2 = ["⬜", "⬜", "⬜"]
    row3 = ["⬜", "⬜", "⬜"]
    box = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    game_over = False

    symbol = {
        player1: "X",
        player2: "O"
    }
    turn = player1

    n = 1
    while not game_over:
        print(f"{turn}'s turn")
        position = values[input("Where do you want to put the treasure? ")]
        row = int(position[1])
        column = int(position[0])
        box[row - 1][column - 1] = symbol[turn]
        print(f"{row1}\n{row2}\n{row3}")
        if (row1[0] == row1[1] == row1[2] == 'X') \
                or (row2[0] == row2[1] == row2[2] == 'X') \
                or (row3[0] == row3[1] == row3[2] == 'X') \
                or (row1[0] == row2[0] == row3[0] == 'X') \
                or (row1[1] == row2[1] == row3[1] == 'X') \
                or (row1[2] == row2[2] == row3[2] == 'X') \
                or (row1[0] == row2[1] == row3[2] == "X") \
                or (row1[2] == row2[1] == row3[0] == "X"):
            print(f"{player1} won the game")
            score1 += 1
            game_over=True

        elif (row1[0] == row1[1] == row1[2] == 'O') \
                or (row2[0] == row2[1] == row2[2] == 'O') \
                or (row3[0] == row3[1] == row3[2] == 'O') \
                or (row1[0] == row2[0] == row3[0] == 'O') \
                or (row1[1] == row2[1] == row3[1] == 'O') \
                or (row1[2] == row2[2] == row3[2] == 'O') \
                or (row1[0] == row2[1] == row3[2] == "O") \
                or (row1[2] == row2[1] == row3[0] == "O"):
            score2 += 1
            print(f"{player2} won the game")

            game_over = True
        elif "⬜" not in (row1 and row2 and row3):
            print("it's a draw")
            game_over = True
        n*=-1
        if n==1:
            turn=player1
        elif n==-1:
            turn=player2
    print(f"{player1}'s score is {score1}"
          f"{player2}'s score is {score2}")
    game_continue = input("do you want to continue the game?:")
    if game_continue == "yes":
        game(player1,player2,score1,score2)
player1 = input("enter the name of the 1st player")
player2 = input("enter the name of the 2nd player")
score1=0
score2=0
game(player1,player2,score1,score2)

#Write your code above this row 👆

# 🚨 Don't change the code below 👇


