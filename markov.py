"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file = open(file_path)
    text = file.read()
    file.close()
   
    return text
# open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]

       
    """
    chains = {} 
    
    words = text_string.split()
    # print(words)

    # To set a stop point, append None to the end of our word list... (research this)
    words.append(None)

    print(words)
    # next_word = []

    for i in range(len(words) -2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains: 
           chains[key] = []

    # or we could replace the last three lines with:
        #    chains.setdefault(key, []).append(value)
        chains[key].append(value)
    # print(chains)
    return chains

    # To set a stop point, append None to the end of our word list.


def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    # Keep looping until value of None is reached 
    # (which would mean it was the end of the original text)
    # For long texts such as a book, this may mean run for a while.

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
