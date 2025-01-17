while True:
    def check(wordc: str, guessc: str) -> bool:
        i = 0
        j = 0
        while i < 5:
            if guessc[i] in wordc:
                if guessc[i] == wordc[i]:
                    print("G ")
                    i += 1
                    j += 1
                else:
                    print("Y ")
                    i += 1
            else:
                print("B ")
                i += 1
        if j == 5:
            return True
        else:
            return False

    isValid = False

    print("Player 1: Please Input Your Starting Word")

    word = str(input())

    while not isValid:
        if len(word) != 5 or not word.isalpha():
            print("Please Input a Valid 5 letter word")
            word = str(input())
        else:
            isValid = True

    guessNum = 1
    winCon = False
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    while True:
        if winCon:
            print("Congrats, you won in " + str(guessNum-1) + " guesses!")
            break
        else:
            print("Hello Player 2, please input a valid guess.")
            print("Guess: " + str(guessNum) + " out of 6")
            guess = str(input())
            isValidGuess = False
            while not isValidGuess:
                if len(guess) != 5 or not guess.isalpha():
                    print("Please Input a Valid 5 letter word")
                    guess = str(input())
                else:
                    isValidGuess = True
            winCon = check(word, guess)
            guessNum += 1
        if guessNum > 6 and not winCon:
            print("Sorry, you lose!")
            break
