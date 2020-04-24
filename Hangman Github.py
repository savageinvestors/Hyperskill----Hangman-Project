import random
from string import ascii_lowercase
print('H A N G M A N')
print('Type "play" to play the game, "exit" to quit: ', end='')
x = input()
word = random.choice(['python', 'java', 'kotlin', 'javascript'])
# word = random.choice(['java'])
s = set()
w = set()
lives = 8
while x != 'play':
	if x == 'exit':
		exit()
	print('Type "play" to play the game, "exit" to quit: ', end = '')
	x = input()
while lives > 0 and x == 'play':
    print()
    for k in word:
        if k in s:
            print(k, end='')
        else:
            print('-', end='')
    print()
    print('Input a letter: ', end='')
    n = input()
    if n not in word and n not in w and n in ascii_lowercase:
        print('No such letter in the word')
        lives -= 1
        w.add(n)
    elif n in w:
        print('You already typed this letter')
        lives -= 0
    elif n in s:
        print('You already typed this letter')
        lives -= 0
    elif len(n) > 1:
        print('You should print a single letter')
        lives -= 0
    elif n not in ascii_lowercase:
        print('It is not an ASCII lowercase letter')
        lives -= 0
    else:
        s.add(n)
    if set(word) == s:
        print('You guessed the word ' + word +'!\nYou survived!')
        break
else:
    print('You are hanged!')
