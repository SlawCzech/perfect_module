#!/usr/bin/env python3

import sys


def fetch_words(filepath):
    with open(filepath, 'r') as file:
        return [word for line in file for word in line.split()]
        # words = []
        # for line in file.readlines():
        #     for word in line.split():
        #         words.append(word)
        # return words


def main(filepath):
    words = fetch_words(filepath)
    print_items(words)


def print_items(items):
    for item in items:
        print(item)


# read_file('text.txt')
# print(__name__)

# czy jest uruchamiany z terminala czy w pythonie
if __name__ == '__main__':
    # read_file('text.txt')
    # read_file(sys.argv[1])

    main(sys.argv[1])
# print(__name__) dla shella: __main__
# print(__name__) dla pythona: app

# w konktekście otwarcia z shella się odpali
# w kontekści pythona zaimportje się, ale nie odpali

