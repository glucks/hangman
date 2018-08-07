def hangman(word):
    wrong = 0
    stages = ["",
    "   |   ",
    "   o   ",
    "  /|\  ",
    "  / \  "
    ]

    letters = list(word)
    board = ["_"]*len(word)

hangman("cat")
