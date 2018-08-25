# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    # make sure the sequence of letter are all lower case
    sequence = sequence.lower()
    
    # if the length of seq is 1, return seq
    if len(sequence) == 1:
        return(sequence)
    # otherwise:
    else:
        # create an empty list
        result = []
        # get the permutations of sequence without the first letter
        perms = get_permutations(sequence[1:])
        # insert the first letter into permutations obtained above
        for m in perms:
            for i in range(len(m)+1):
                result.append(m[:i] + sequence[0] + m[i:])
        # return the list of permutations
        return(sorted(result))
        
                
            
        
        
            

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

