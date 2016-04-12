
def count_words(test_file):
    '''Counts word occurances in text.'''

    data = open(test_file)

    list_of_words = []  # Create an empty list to store lists of [word, word count]
    dict_of_words = {}  # Create a dictionary to store word : word count pairs

    for line in data:
        line = line.rstrip()
        line = line.split(" ")
        list_of_words.extend(line)  # Extend list_of_words with all words from .txt

    for word in list_of_words:
        dict_of_words[word] = dict_of_words.get(word, 0) + 1

    for word, count in dict_of_words.items():
        print word, count

    return dict_of_words


count_words("test.txt")
