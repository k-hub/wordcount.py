
def count_words(test_file):
    '''Counts word occurances in text.'''

    data = open(test_file)

    list_of_words = []
    dict_of_words = {}

    for line in data:
        line = line.rstrip()
        line = line.split(" ")
        list_of_words.extend(line)
    for word in list_of_words:
        dict_of_words[word] = list_of_words.count(word) # Setting keys and values and adding them to dictionary.
        # word_key = dict_of_words[word]
        # word_key_value = list_of_words.count(word)


    print dict_of_words
    # print dict_of_words[look_up_this_word]
    return dict_of_words


# count_words("test.txt", "seven")
count_words("test.txt")