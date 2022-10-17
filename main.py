#!/usr/bin/env python3


"""Fetch and print words

Usage:
    python main.py <filepath>
    ./main.py <filepath>

    from main import main
    main(<filepath>)

"""


import sys


def fetch_words(filepath):
    """
    Fetch words from given filepath
    :param filepath: relative or absolute filepath
    :type filepath: str
    :return: word list from given filepath
    :rtype: list[str]
    """
    with open(filepath, 'r') as file:
        return [word for line in file for word in line.split()]
        # words = []
        # for line in file.readlines():
        #     for word in line.split():
        #         words.append(word)
        # return words



def print_items(items):
    """
    Print items from iterable
    :param items: any iterable collection of data
    :type items: iterable
    :return: None
    :rtype: None
    """
    for item in items:
        print(item)


def main(filepath):
    """
    Fetch and show word from given filepath
    :param filepath: relative or absolute filepath
    :type filepath: str
    :return: None
    :rtype: None
    """
    words = fetch_words(filepath)
    print_items(words)


# read_file('text.txt')
# print(__name__)

# czy jest uruchamiany z terminala czy w pythonie
if __name__ == '__main__':
    # read_file('text.txt')
    # read_file(sys.argv[1])
    main(sys.argv[1])  # Zero-index is module name (indeks 0 to nazwa modułu)
# print(__name__) dla shella: __main__
# print(__name__) dla pythona: app

# w konktekście otwarcia z shella się odpali
# w kontekści pythona zaimportje się, ale nie odpali

