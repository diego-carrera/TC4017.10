"""
Program: word_count.py
Author: Diego Carrera Nicholls
Date: 2023-01-30
Version: 1.0
Description: Count the frequency of words in a given dataset.
"""

import sys
import time

def read_data(file_path):
    """
    Read data from a file and return a list of words.

    Args:
        file_path (str): The path to the file.

    Returns:
        tuple: A tuple containing the list of words and the number of lines read.

    Raises:
        FileNotFoundError: If the file does not exist.
    """

    data = []
    lines_read = 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue
                try:
                    data.append(line.strip())
                except ValueError:
                    print(f"Error in line {lines_read+1}: {line.strip()} is not a number.")

                lines_read += 1

    except FileNotFoundError:
        print("Error: File does not exist.")
        sys.exit(1)
    return data, lines_read

def count_words_freq(data):
    """
    Count the frequency of words in a list of words.

    Parameters:
    data (list): A list of words.

    Returns:
    dict: A dictionary containing the frequency of each word.
    """
    freq = {}
    for word in data:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    return freq

def print_freq(freq):
    """
    Print the frequency of each word in a dictionary.

    Parameters:
    freq (dict): A dictionary containing the frequency of each word.
    """
    with open("word_count_results.txt", "w", encoding="utf-8") as file:
        for word, count in freq.items():
            print(f"{word}\t{count}")
            file.write(f"{word}\t{count}\n")

        grand_total = sum(freq.values())
        print(f"Grand Total\t{grand_total}")
        file.write(f"Grand Total\t{grand_total}\n")

def main():
    """
    Entry point of the program.

    Reads a file path from the command line arguments, reads the data from the file,
    counts the frequency of each word in the data, prints the frequency, and writes
    the elapsed time to a file.
    """
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py <file_path>")
        sys.exit(1)

    start = time.time()

    file_path = sys.argv[1]
    data, _ = read_data(file_path)

    freq = count_words_freq(data)
    print_freq(freq)
    end = time.time()
    elapsed_time = end - start

    print(f"TIME:\t{elapsed_time}")

    with open("word_count_results.txt", "a", encoding="utf-8") as file:
        file.write(f"TIME:\t{elapsed_time}\n")


if __name__ == "__main__":
    main()
