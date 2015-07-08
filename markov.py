import sys
import random

def file_convert(file_name):
    """ Takes the name of a file as input, converts that file to a single 
    text string with a single space inserted between lines.
    """

    text_string = ""

    with open(file_name, "r") as text_file:
        for line in text_file:
            new_line = line.rstrip() + " "
            text_string += new_line

    return text_string


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    word_list = corpus.split(" ") #creates ordered list of words from text
    chain_dict = {}

    for i in range(0, (len(word_list)-2)) :
        bi_gram = word_list[i] + " " + word_list[i+1]
        
        if bi_gram not in chain_dict:
            chain_dict[bi_gram] = []
        
        chain_dict[bi_gram].append(word_list[i+2])

        #chain_dict[bi_gram] = chain_dict.get(bi_gram, [])
        #words.setdefault('porcupine', []).append("hello") -- method of appending
        #word_dict[word] = word_dict.get(word, 0) + 1
        #word_list[i+2] = value for bi_gram
        #{key:value for (key, value) in iterable}

    return chain_dict    


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    random_text = ""
    bi_gram_list = chains.keys()
    random_start = random.choice(bi_gram_list)
    random_text = random_start + " "
    word_pair = random_start

    while True:   
        if chains[word_pair] == [""]:
            break
        else:
            value_list = chains[word_pair]
            random_word = random.choice(value_list)
            random_text += random_word + " "
            word_pair = word_pair.split()[-1] + " " + random_word

    return random_text


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "Some text"

# Get a Markov chain
# chain_dict = make_chains(input_text)

# Produce random text
# random_text = make_text(chain_dict)

#print random_text

# For test purposes, executed functions using hard-coded file as input
# Will replace these lines with more generic version per above comments
chains = make_chains(file_convert('green-eggs.txt'))
print make_text(chains)
