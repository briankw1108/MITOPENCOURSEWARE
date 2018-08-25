# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

# define a method to find the position of matched letter in a seq
def search(seq, letter):
    '''
    A function to search the position of the letter in a sequence of string
    
    seq: a sequence of string
    letter: the letter to be located in a sequence of string
    
    Returns: the position index where the letter locates in the string
    
    Example:
    >>> search('abc', 'b') returns
    1
    '''
    # verify the seq contains letter
    assert (letter in seq), letter + ' not in ' + seq
    # if letter is equal to seq, return 0
    if letter == seq:
        return(0)
    # otherwise
    else:
        # get the length of the sequence to be searched
        length = len(seq)
        # create a variable that store the position of first letter in original seq
        first = 0
        # if letter appears in the first half, then recursively search this half
        if letter in seq[:(length//2)]:
            position = search(seq[:(length//2)], letter)
        # else
        else:
            # set the position of first letter in this half from original seq
            first = length//2
            # recursively search this half
            position = search(seq[first:], letter)
        # return the position with respect to the original seq
        return(first+position)


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # set attributes
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        
        return(self.message_text)

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        
        return(self.valid_words.copy())
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        # create an empty dictionary
        dic = {}
        # loop through vowels and its permutation to set mapping letters
        for (i, l) in enumerate(string.ascii_lowercase):
            if l in 'aeiou':
                pos = search(VOWELS_LOWER, l)
                dic[l] = vowels_permutation[pos]
                dic[l.upper()] = vowels_permutation[pos].upper()
            else:
                dic[l] = l
                dic[l.upper()] = l.upper()
        # return the dictionary
        return(dic)
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        # get message text        
        text = self.message_text
        # create an empty variable to store string
        new_text = ''
        # loop through text with its letters 
        for l in text:
            # if the letter is symbols
            if l in " !@#$%^&*()-_+={}[]|\:;'<>?,./\"":
                # add it to the string    
                new_text = new_text + l
            # otherwise
            else:
                # add the mapping letter from dictionary to the string
                new_text = new_text + transpose_dict[l]
        # return the final string
        return(new_text)
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        # load package needed
        import random
        # retrieve the attribute of message text
        text = self.message_text
        # get word list
        word_list = self.valid_words
        # get all the permutations for the vowels
        perms = get_permutations(VOWELS_LOWER)
        # create an empty dictionary to store decrypted results
        result = {}
        # loop through all permutations
        for perm in perms:
            # create a counter for calculating counts for valid words
            count = 0
            # get transpose dictionary from permutation
            dic = self.build_transpose_dict(perm)
            # get encrypted message text by transpose dictionary
            decrypted = self.apply_transpose(dic).split()
            # loop through the list of words in decrypted message
            for w in decrypted:
                # if the word is a valid word, then increment 1
                if is_word(word_list, w):
                    count += 1
            # store count: encrypted message in the result dictionary
            if count not in result:
                result[count] = [' '.join(decrypted)]
            else:
                result[count].append(' '.join(decrypted))
        # get the maximum count from dictionary's keys
        max_key = max(result.keys())
        # get the number of items in the list with maximum valid words stored in the dictionary
        num_seq = len(result[max_key])
        # return one of the answers in the list
        return(result[max_key][random.choice(range(num_seq))])
        

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
