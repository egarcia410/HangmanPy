import requests
import random

# Insert API for selecting random word in future
# word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
# response = requests.get(word_site)
# words = response.content.splitlines()
# randomWord = random.randint(0, len(words))
# print(words[randomWord])

def hangman():
    words = ['Houston', 'Boston', 'Orlando', 'Seattle', 'Atlanta']
    randomWord = random.choice(words).lower()
    guesses = 0
    wrongGuesses = 0
    guessedLetters = ""
    strWord = ""
    won = True
    continuePlay = True

    for letter in randomWord:
        strWord += '*' 

    print('Welcome to Hangman!')

    listHangman = [ [' ', '_', '_', '_', '_', '_', '_', '_', ' '],
                    [' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' '],
                    [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                    ['_', '|', '_', ' ', ' ', ' ', ' ', ' ', ' '] ]

    while continuePlay:
        strHangman = listToStrHangman(listHangman)
        print(strHangman)
        print(strWord)
        print('Number of Guesses: ', guesses)
        print('Guessed Letters: ', guessedLetters)
        response = input('Choose a letter: ').lower()
        # Checks if response is not a string or more than one letter input
        if isinstance(response, str) and len(response) < 2:
            if response in randomWord:
                guesses += 1
                guessedLetters += response
                for ind, letter in enumerate(randomWord):
                    if letter == response:
                        strList = list(strWord)
                        strList[ind] = response
                        strWord = ''.join(strList)
                        if strWord == randomWord:
                            continuePlay = False
            else:
                guesses += 1
                guessedLetters += response
                wrongGuesses += 1
                if wrongGuesses == 1:
                    listHangman[2][6] = 'O'
                elif wrongGuesses == 2:
                    listHangman[3][6] = '|'
                    listHangman[4][6] = '|'
                elif wrongGuesses == 3:
                    listHangman[3][5] = '/'
                elif wrongGuesses == 4:
                    listHangman[3][7] = '\\'
                elif wrongGuesses == 5:
                    listHangman[5][5] = '/'
                elif wrongGuesses == 6:
                    listHangman[5][7] = '\\'
                    won = False
                    continuePlay = False
        
        for ind, x in enumerate(listHangman):
            strHangman += ''.join(listHangman[ind]) + '\n'
        print('---------------------')

    if won:
        print('You Won!')
    else:
        print('You Died')
    print(listToStrHangman(listHangman))
    print(strWord)
    print('Number of Guesses: ', guesses)
    print('Guessed Letters: ', guessedLetters)

def listToStrHangman(listHangman):
    strHangman = ""
    for ind, x in enumerate(listHangman):
        strHangman += ''.join(listHangman[ind]) + '\n'
    return strHangman

if __name__ == '__main__':
    hangman()