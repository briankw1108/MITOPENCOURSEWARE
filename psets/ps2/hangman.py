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



def create_letter_dictionary(secret_word):
    '''
    secret_word: string, the word the user is guessing
    returns: dictionary, a dictionary that contains all letters in secret word
      as keys and index as associated values
    '''
    secret_word = secret_word.lower()
    dic = {}
    for index, letter in enumerate(secret_word):
        if letter in dic:
            if type(dic[letter]) == list:
                dic[letter].append(index)
            else:
                temp = dic[letter]
                dic[letter] = [temp, index]
        else:
            dic[letter] = index
    return(dic)



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word = secret_word.lower()
    unique = len(create_letter_dictionary(secret_word))
    word_len = 0
   
    for letter in letters_guessed:
        if letter in secret_word:
            word_len += 1
        else:
            pass
        
    if word_len == unique:
        return(True)
    else:
        return(False)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word = secret_word.lower()
    letters_guessed = list(''.join(letters_guessed).lower())
    dic = create_letter_dictionary(secret_word)
    answer = list('_' * len(secret_word))
    for letter in letters_guessed:
        if letter in dic:
            if type(dic[letter]) == list:
                for i in dic[letter]:
                    answer[i] = letter
            else:
                answer[dic[letter]] = letter
        else:
            pass
    return(''.join(answer))
    


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_list = list(string.ascii_lowercase)
    if len(letters_guessed) == 0:
        return(string.ascii_lowercase)
    else:
        for letter in letters_guessed:
            if letter.lower() in ''.join(letters_list):
                letters_list.remove(letter.lower())
            else:
                pass
        return(''.join(letters_list))
    
    
    
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
    secret_word = secret_word.lower()
    letters_guessed = []
    
    unique = len(create_letter_dictionary(secret_word))
    
    available_letters = get_available_letters(letters_guessed)
    guess_remaining = 6
    warning_remaining = 3
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warning_remaining, ' warnings left.')
    
    while (not is_word_guessed(secret_word, letters_guessed)) & (guess_remaining > 0):
        
        if guess_remaining > 1:
            print('You have', guess_remaining, 'guesses left:', get_guessed_word(secret_word, letters_guessed))
        else:
            print('You have', guess_remaining, 'guess left:', get_guessed_word(secret_word, letters_guessed))
        
        guess = input('Please guess a letter: ').lower()
        if (guess in available_letters) & (guess in secret_word):
            letters_guessed.append(guess)
            available_letters = get_available_letters(letters_guessed)
            print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        elif (guess in available_letters) & (guess not in secret_word):
            if guess in 'aeiou':
                guess_remaining = guess_remaining - 2
            else:
                guess_remaining = guess_remaining - 1
            letters_guessed.append(guess)
            available_letters = get_available_letters(letters_guessed)
            print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
        elif guess not in string.ascii_lowercase:
            warning_remaining = warning_remaining - 1
            if warning_remaining > 1:
                print('Oops! That is not a valid letter. You now have', warning_remaining, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! That is not a valid letter. You now have', warning_remaining, 'warning left:', get_guessed_word(secret_word, letters_guessed))
        elif guess not in available_letters:
            warning_remaining = warning_remaining - 1
            if warning_remaining > 1:
                print('Oops! You\'ve already guessed that letter. You now have', warning_remaining, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! You\'ve already guessed that letter. You now have', warning_remaining, 'warning left:', get_guessed_word(secret_word, letters_guessed))
        
        if warning_remaining == 0:
            guess_remaining = guess_remaining - 1
            warning_remaining = 3
            
        print('-'*10)
        
    if (guess_remaining <=0) & (not is_word_guessed(secret_word, letters_guessed)):
        print('Sorry, you ran out of guesses. The word was', secret_word)
    elif is_word_guessed(secret_word, letters_guessed):
        print('Congratulations! You won!')
        print('Your total score for this game is:', guess_remaining*unique)
    
    

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
    my_word_dic = create_letter_dictionary(my_word)
    other_word_dic = create_letter_dictionary(other_word)
    del(my_word_dic['_'])
    if len(my_word) != len(other_word):
        return(False)
    elif len(my_word_dic) > 0:
        for key in list(my_word_dic.keys()):
            if key in other_word:
                if my_word_dic[key] != other_word_dic[key]:
                    return(False)
                else:
                    pass
            else:
                return(False)
    elif len(my_word_dic) == 0:
        return(False)
        
    return(True)
        


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)
        
    if len(matches) == 0:
        print('No matches found')
    else:
        print(' '.join(matches))
            



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
    secret_word = secret_word.lower()
    letters_guessed = []
    
    unique = len(create_letter_dictionary(secret_word))
    
    available_letters = get_available_letters(letters_guessed)
    guess_remaining = 6
    warning_remaining = 3
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warning_remaining, 'warnings left.')
    
    while (not is_word_guessed(secret_word, letters_guessed)) & (guess_remaining > 0):
        
        if guess_remaining > 1:
            print('You have', guess_remaining, 'guesses left:', get_guessed_word(secret_word, letters_guessed))
        else:
            print('You have', guess_remaining, 'guess left:', get_guessed_word(secret_word, letters_guessed))
        
        guess = input('Please guess a letter: ').lower()
        if guess == '*':
            print('Possible word matches are:')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            if (guess in available_letters) & (guess in secret_word):
                letters_guessed.append(guess)
                available_letters = get_available_letters(letters_guessed)
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            elif (guess in available_letters) & (guess not in secret_word):
                if guess in 'aeiou':
                    guess_remaining = guess_remaining - 2
                else:
                    guess_remaining = guess_remaining - 1
                letters_guessed.append(guess)
                available_letters = get_available_letters(letters_guessed)
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
            elif guess not in string.ascii_lowercase:
                warning_remaining = warning_remaining - 1
                if warning_remaining > 1:
                    print('Oops! That is not a valid letter. You now have', warning_remaining, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops! That is not a valid letter. You now have', warning_remaining, 'warning left:', get_guessed_word(secret_word, letters_guessed))
            elif guess not in available_letters:
                warning_remaining = warning_remaining - 1
                if warning_remaining > 1:
                    print('Oops! You\'ve already guessed that letter. You now have', warning_remaining, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops! You\'ve already guessed that letter. You now have', warning_remaining, 'warning left:', get_guessed_word(secret_word, letters_guessed))
            
            if warning_remaining == 0:
                guess_remaining = guess_remaining - 1
                warning_remaining = 3
            
        print('-'*10)
        
    if (guess_remaining <=0) & (not is_word_guessed(secret_word, letters_guessed)):
        print('Sorry, you ran out of guesses. The word was', secret_word)
    elif is_word_guessed(secret_word, letters_guessed):
        print('Congratulations! You won!')
        print('Your total score for this game is:', guess_remaining*unique)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
