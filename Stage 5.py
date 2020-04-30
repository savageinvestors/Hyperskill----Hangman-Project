import random

def loadWords():
    word_list = ['javascript']
    # word_list = ['python', 'kotlin', 'java', 'javascript']
    return random.choice(word_list)

word = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    c = 0
    for i in lettersGuessed:
        if i in secretWord:
            c += 1
    if c == len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    s = []
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans = ''
    for i in secretWord:
        if i in s:
            ans += i
        else:
            ans += '-'
    return ans
    print(ans)

def getAvailableLetters(lettersGuessed):
    import string
    ans = list(string.ascii_lowercase)
    for i in lettersGuessed:
        ans.remove(i)
    return ''.join(ans)
    print(ans)

def hangman(secretWord):
    print("H A N G M A N")
    print()
    hidden = len(word)
    hint = "-" * hidden
    print(hint)
# print("Welcome to the game, Hangman!")
# print("I am thinking of a word that is", len(secretWord), "letters long.")
#
    global lettersGuessed
    turns = 0
    lettersGuessed = []

    while 8 - turns > 0:
        turns += 1
        if isWordGuessed(secretWord, lettersGuessed):
        # 	print(word)
        # 	print("Congratulations, you won!")
        # 	break
            continue

        else:
            # print("-------------")
            # print("You have", 8 - mistakeMade, "guesses left.")
            # print("Available letters:", getAvailableLetters(lettersGuessed))
            guess = str(input("Input a letter: ")).lower()
            print()
            # if guess in lettersGuessed:
            # 	print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))

            if guess in secretWord and guess not in lettersGuessed:
                # x = guess in secretWord and guess not in lettersGuessed
                lettersGuessed.append(guess)
                print(getGuessedWord(secretWord, lettersGuessed))

            else:
                lettersGuessed.append(guess)
                print("No such letter in the word.")
                print()
                if 8 - turns > 0:
                    print(getGuessedWord(secretWord, lettersGuessed))

        if 8 - turns == 0:
            # print(word)
            print("Thanks for playing!")
            print("We'll see how well you did in the next stage")
            break

        else:
            continue

secretWord = word.lower()
hangman(secretWord)
