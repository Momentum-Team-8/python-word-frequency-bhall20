


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# Why isnt this printing? Is everything else functioning?
def print_word_freq(file):
    a = []
    with open('one-today.txt', 'r') as file:
        file.readlines()
        file.strip('.!,:;-"')
        file.lower()
        for line in file:
            a.append(line)
    print(a)

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
