import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
    'to', 'were', 'will', 'with'
]


with open('praise_song_for_the_day.txt') as file:
    text = file.read()
    split_words = text.split()
    no_punctuation_list = []
    for word in split_words:
        newlist = word.translate(str.maketrans("", "", string.punctuation))
        no_punctuation_list.append(newlist.lower())
        # print(no_punctuation_list)
        stop_removed = []
        for words in no_punctuation_list:
            if words not in STOP_WORDS:
                stop_removed.append(words)
                # print()
        for words in stop_removed:
            num_of_words = stop_removed.count(words)
            # sorted(num_of_words) Could not figure out how to sort them
            print(words, num_of_words)

# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path
#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():

#         print(f"{file} does not exist!")
#         exit(1)

# print_word_freq("one-today.txt")
