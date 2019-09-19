import unittest
import random
from termcolor import colored #i want to try to play with colors too


def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
                            #here we are just getting our wordlist and choosing one at random
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

#A function that checks if all the letters of the secret word have been guessed.
def is_word_guessed(secret_word, letters_guessed):
    secret_length = len(secret_word)
    i = 0
    for letter in letters_guessed:
        number_of_letters = secret_word.count(letter)
        if (number_of_letters > 0):
            i += number_of_letters
    if secret_length == i:
        return True
    else:
        return False

# A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
def get_guessed_word(secret_word, letters_guessed):
    guessstring = ""
    for letters in secret_word:
        if letters in letters_guessed:
            guessstring += (letters + ' ')
        else:
            guessstring += "_ "
    return print(guessstring)
#simply returns true or false as to whether the guess is in the word
def is_guess_in_word(guess, secret_word):

    return guess in secret_word

def spaceman(secret_word):


#Initiates the game sets the cariables and prompts the player
    print(colored('\n\nReady to play the Spaceman Game?', "blue", attrs=["bold"]))
    print(colored('\n\nSee if you can guess the secret word!', "yellow", attrs=["bold"]))
    print(colored('\n\nGuess the word before you run out of tries!', "green", attrs=["bold"]))


    #print(secret_word)

    letters_guessed = []
    guessed = 7
    running = True

    while (is_word_guessed(secret_word, letters_guessed) == False and guessed > 0):

        print(colored('You have ' + str(guessed) + ' guesses left!', "yellow"))
        get_guessed_word(secret_word, letters_guessed)
        guess = input("Please guess your letter here > ")
#checks that the guess is a single letter
        if not (guess.isalpha() == True and len(guess) == 1):
            print(colored('You messed up, try picking one letter!', "red", attrs=["bold"]))
#checks to see it hasnt been guessed
        elif (guess in letters_guessed):
            print ('We already tried that one! try again!')
        else:
            letters_guessed += guess
            if is_guess_in_word(guess, secret_word) == True:
                print('Nice!')
            else:
                guessed -= 1
                print('The letter is not in the word')

    if (guessed < 1):
        print (colored("I hate to say it but you are out of guesses!", "red"))
        print("The secret word was!")
#prints word if user failed to guess correctly
        for  char in secret_word:
            i = 0
            print(char)
            i = i + 1
#offers to play again
        again = str(input("Type yes if you would like to play again > "))
        print (again)
        if again == "yes":
            secret_word = load_word()
            spaceman(secret_word)


    else:
        print(colored('I cannot believe it!, this have never happend before! Congratulations! you won!. ', "magenta", attrs=["bold"]))
#offers to play again
        again = str(input("Type yes if you would like to play again > "))
        print (again)
        if again == "yes":
            secret_word = load_word()
            spaceman(secret_word)

secret_word = load_word()
#spaceman(secret_word)

class SpacemanTests(unittest.TestCase):


    def test_is_word_guessed(self):
        #teasting edge case with just 3 letters
        self.assertEqual(is_word_guessed("test", "tse"), True)
        self.assertEqual(is_word_guessed("test", "wdse"), False)
        self.assertEqual(is_word_guessed("makeschool", "wdsealdnxs"), False)

        #testing if word is guessed after extra letters
    def test_is_word_guessed_plus(self):
        self.assertEqual(is_word_guessed("fritz", "fraitz"), True)
        self.assertEqual(is_word_guessed("fritz", "fraitews"), False)
        self.assertEqual(is_word_guessed("fritz", "fraitvxawz"), True)

        #testing to see if letters in word
    def test_guess_in_word_true(self):
        self.assertEqual(is_guess_in_word("t", "test"), True)
        self.assertEqual(is_guess_in_word("r", "fact"), False)
        self.assertEqual(is_guess_in_word("p", "please"), True)


    def test_get_guess_in_word(self):
    #interesting behavior here
        self.assertEqual(get_guessed_word("test", "test"), None)
        self.assertEqual(get_guessed_word("test", "doggos"), None)

if __name__ == '__main__':
    unittest.main()
