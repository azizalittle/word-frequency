import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by',
    'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 
    'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, 'r') as reader:
        contents = reader.read()
        # make all words lowercase
        low_word = contents.lower()
        # remove punctuation
        no_punc = low_word.translate(str.maketrans("", "", string.punctuation))
        # split out spaces
        word_list = no_punc.split()
        # print(word_list)
        # counting loop
        no_stop_words = delete_stop_words(word_list)
        word_count = dict()
        for word in no_stop_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        sorted_counts = sorted(
            word_count.items(), 
            key=lambda item: item[1],
            reverse=True)
        print_freq(sorted_counts)


def delete_stop_words(word_list):
    # check each owrd in the list and see if it is equal to a STOP WORD
    # if the word is in the STOP WORDS list, remove the word
    word_list_copy = word_list[:]
    for word in word_list:
        if word in STOP_WORDS:
            word_list_copy.remove(word)
    return word_list_copy


def print_freq(freq_list):
    for item in freq_list:
        star = "* "
        print(f"{item[0]} | {item[1]} {item[1]*star}")


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
