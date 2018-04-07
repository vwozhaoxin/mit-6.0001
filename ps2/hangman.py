# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter in letters_guessed:
            continue
        else:
            return False
    return True 
#test_word = 'apple'
#test_guessed =['a','p','l','o']
#print(is_word_guessed(test_word,test_guessed))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ''
    for letter in secret_word:
        if letter in letters_guessed:
            result+= letter
        else:
            result+='_'
    return result
#test_word = 'apple'
#test_guessed =['a','p','l','o']
#print(get_guessed_word(test_word,test_guessed))

    

import string

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result=''
    for letter in string.ascii_lowercase:
        if letter in letters_guessed:
            continue
        else:
            result +=letter
    return result
#test_guessed =['a','p','l','o']
#print(get_available_letters(test_guessed))
  
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
#    print(secret_word)
    score=0
    win=0
    letters_guessed =[]
    guesses = 6
    m = len(secret_word)
    warn=3
    vowels =['a','e','i','o','u']
    guess_letter = get_available_letters(letters_guessed)
    print("Welcome to the game Hangman! ")
    print('I am thinking of a word that is {} letters long'.format(m))
    print('_'*20)
    print('you have {} warning left'.format(warn))
    print('You have {} guesses left.'.format(guesses))
    print('Available letters: {}'.format(guess_letter))
    while not guesses==0:
        guess = input('please guess a letter:  ')
        if not (guess.isalpha() and len(guess)==1):
            print('please input a letter')
            if (warn !=0):
                warn-=1
            print('you have {} warning left'.format(warn))
            if warn ==0:
                guesses-=1
                print('you have {} times to play'.format(guesses))
            continue
        if guess in letters_guessed:
            print('do not input the same letter')
            if (warn !=0):
                warn-=1
            print('you have {} warning left'.format(warn))
            print('partially secret word is:{}'.format(partially_word))
            if warn ==0:
                guesses-=1
                print('you have {} times to play'.format(guesses))
            continue
        if not (guess in secret_word):
            if guess in vowels:
                guesses-=2
            else:
                guesses-=1
        letters_guessed.append(guess.lower())
        guess_letter = get_available_letters(letters_guessed)
        partially_word= get_guessed_word(secret_word,letters_guessed)
        
        print('you have {} times to play'.format(guesses))
        print('the unguessed letter are: {}'.format(guess_letter))
        if guess in secret_word:
            print('right letter')
        else:
            print('wrong letter')
        print('partially secret word is:{}'.format(partially_word))
        print('-'*40)
        if partially_word==secret_word:
            win =1                
            score = guesses * len(set(secret_word))
            break
    if win==0 and guesses==0:
        print('sorry you lose the game')        
    if win ==1:
        print('congratulation,you win,you total score is:{}'.format(score))
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word.strip())==len(other_word):
        for idx,letter in enumerate(my_word.strip()):
            if letter =='_':
                if other_word[idx] in my_word:
                    return False
                else:
                    continue
            else:
                if letter == other_word[idx]:
                    continue
                else:
                    return False
                
        return True
    else:
        return False

#print(match_with_gaps('a__le ','apple'))


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    result =[word for word in wordlist if match_with_gaps(my_word,word)]
#    for word in wordlist:
#        if match_with_gaps(my_word,word):
#            result.append(word)
    if len(result)==0:
        print('No matches found')
    else:
        print(result)

#show_possible_matches('a_ple')

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    score=0
    win=0
    letters_guessed =[]
    guesses = 6
    m = len(secret_word)
    warn=3
    vowels =['a','e','i','o','u']
    guess_letter = get_available_letters(letters_guessed)
    print("Welcome to the game Hangman! ")
    print('I am thinking of a word that is {} letters long'.format(m))
    print('_'*20)
    print('you have {} warning left'.format(warn))
    print('You have {} guesses left.'.format(guesses))
    print('Available letters: {}'.format(guess_letter))
    while not guesses==0:
        guess = input('please guess a letter:  ')
        if guess=='*':
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
            continue
        if not (guess.isalpha() and len(guess)==1):
            print('please input a letter')
            if (warn !=0):
                warn-=1
            print('you have {} warning left'.format(warn))
            if warn ==0:
                guesses-=1
                print('you have {} times to play'.format(guesses))
            continue
        if guess in letters_guessed:
            print('do not input the same letter')
            if (warn !=0):
                warn-=1
            print('you have {} warning left'.format(warn))
            print('partially secret word is:{}'.format(partially_word))
            if warn ==0:
                guesses-=1
                print('you have {} times to play'.format(guesses))
            continue
        if not (guess in secret_word):
            if guess in vowels:
                guesses-=2
            else:
                guesses-=1
        letters_guessed.append(guess.lower())
        guess_letter = get_available_letters(letters_guessed)
        partially_word= get_guessed_word(secret_word,letters_guessed)
        
        print('you have {} times to play'.format(guesses))
        print('the unguessed letter are: {}'.format(guess_letter))
        if guess in secret_word:
            print('right letter')
        else:
            print('wrong letter')
        print('partially secret word is:{}'.format(partially_word))
        print('-'*40)
        if partially_word==secret_word:
            win =1                
            score = guesses * len(set(secret_word))
            break
    if win==0 and guesses==0:
        print('sorry you lose the game')        
    if win ==1:
        print('congratulation,you win,you total score is:{}'.format(score))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    pass
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
