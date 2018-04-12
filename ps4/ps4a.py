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
    results=[]
    if len(sequence)==1:
        results = [sequence]
        return results
    else:               
        key =sequence[0]
        sequence = sequence[1:]
        result = get_permutations(sequence)
        for re in result:
            for i in range(len(re)+1):
                word = re[0:i]+key +re[i:]
                results.append(word)
        
        return results
        

if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abcde'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print(len(get_permutations(example_input)))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    

