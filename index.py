import requests
import random

# Insert API for selecting random word in future
# word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
# response = requests.get(word_site)
# words = response.content.splitlines()
# randomWord = random.randint(0, len(words))
# print(words[randomWord])

def play():
    words = ['Houston', 'Boston', 'Orlando', 'Seattle', 'Atlanta']
    continuePlay = True
    guesses = 0
    wrongGuesses = 0
    randomWord = random.choice(words).lower()
    strWord = ""

    for letter in randomWord:
        strWord += '*' 

    # hangman[39] == O <---Head
    # hangman[51] == / <---Left arm
    # hangman[52] == | <---Upper body
    # hangman[53] == \ <---Right arm Insert extra '\' hangman[54]
    # hangman[66] == | <---Lower body
    # hangman[78] == / <---Left leg
    # hangman[80] == \ <---Right leg

    print('Welcome to Hangman!')
    hangman = """
     ________
     |/    |
     |     
     |    
     |     
     |    
    _|_
        """


    while continuePlay:
        print(hangman)
        print(strWord)
        print('Guesses: ', guesses)
        response = input('Choose a letter: ').lower()
        # Checks if response is not a string or more than one letter input
        if type(response) != 'str' or len(response) > 1:
            break
        elif response in randomWord:
            guesses += 1
            for ind, letter in enumerate(randomWord):
                if letter == response:
                    strWord[ind] = response
        else:
            guesses += 1
            wrongGuesses += 1
            if wrongGuesses == 1:
                strWord[39] = 'O'
            elif wrongGuesses == 2:
                strWord[52] = '|'
                strWord[66] = '|'
            elif wrongGuesses == 3:
                strWord[51] = '/'
            elif wrongGuesses == 4:
                strWord[53] = '\\'
            elif wrongGuesses == 5:
                strWord[78] = '/'
            else:
                strWord[80] = '\\'
                continuePlay = False


if __name__ == '__main__':
    play()