def happyman(word):
    wrong = 0
    stages = ["Idx #0",
              "Idx #1     *        *      ",
              "Idx #2      *      *        ",
              "Idx #3       ** **        ",
              "Idx #4       \ O /        ",
              "Idx #5         |          ",
              "Idx #6         |          ",
              "Idx #7        / \         "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Happygman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Input a letter."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            print("The wrong count is {}.".format(wrong))
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("You loose. The answer is {}.".format(word))
    else:
        print("Bye!")

import random
choice = random.randint(0,4)

answer_list = ["dog", "cat", "lion", "monkey"]
answer = answer_list[choice]

happyman(answer)





