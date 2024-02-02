"""
Program: convert_numbers.py
Author: Diego Carrera Nicholls
Date: 2023-01-30
Version: 1.0
Description: Convert numbers to binary and hex.
"""

import sys
import time

def read_data(file_path):
    """
    Read data from a file and return a list of values.

    Args:
        file_path (str): The path to the file.

    Returns:
        tuple: A tuple containing the list of values and the number of lines read.

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
                    value = int(line.strip())
                    data.append(value)
                except ValueError:
                    print(f"Error in line {lines_read+1}: {line.strip()} is not a number.")

                lines_read += 1

    except FileNotFoundError:
        print("Error: File does not exist.")
        sys.exit(1)
    return data, lines_read


def _ones_complement(binary_number):
    """
    Takes a binary number as input and returns its one's complement.

    Parameters:
    binary_number (str): The binary number to find the one's complement of.

    Returns:
    str: The one's complement of the binary number.
    """
    ones_complement = ""
    for bit in binary_number:
        if bit == "0":
            ones_complement += "1"
        else:
            ones_complement += "0"

    return ones_complement

def _twos_complement(ones_complement):
    """
    Calculates the two's complement of a binary number represented as a string.

    Args:
        ones_complement (str): The binary number in ones' complement representation.

    Returns:
        str: The two's complement of the input binary number.
    """
    twos_complement = ""
    carry = 1
    for bit in ones_complement[::-1]:
        if carry == 1:
            if bit == "0":
                twos_complement = "1" + twos_complement
                carry = 0
            else:
                twos_complement = "0" + twos_complement
                carry = 1
        else:
            twos_complement = bit + twos_complement

    return twos_complement

def to_binary(number):
    """
    Converts a decimal number to its binary representation.

    Args:
        number (int): The decimal number to convert.

    Returns:
        str: The binary representation of the input number.
    """

    if number == 0:
        return "0"

    is_negative = False
    if number < 0:
        is_negative = True
        number = abs(number)

    binary_conversion = ""

    while number > 0:
        remainder = number % 2
        binary_conversion = str(remainder) + binary_conversion
        number //= 2

    if is_negative:

        # pad zeros to make 10 bits
        while len(binary_conversion) < 10:
            binary_conversion = "0" + binary_conversion

        ones_complement = _ones_complement(binary_conversion)
        twos_complement = _twos_complement(ones_complement)

        binary_conversion = twos_complement

    return binary_conversion


def to_hex(number):
    """
    Converts a decimal number to its hexadecimal representation.

    Args:
        number (int): The decimal number to be converted.

    Returns:
        str: The hexadecimal representation of the input number.
    """
    if number == 0:
        return "0"

    hex_conversion = ""
    if number < 0:
        number = abs(number) ^ 0xFFFFFFFFFF
        number += 1

    while number > 0:
        remainder = number % 16
        if remainder < 10:
            hex_conversion = str(remainder) + hex_conversion
        else:
            hex_conversion = chr(remainder + 55) + hex_conversion
        number //= 16

    return hex_conversion


def convert_and_print(data):
    """
    Converts the given list of numbers to binary and hexadecimal representations,
    and prints the results along with their decimal values.

    Args:
        data (list): A list of numbers to be converted and printed.

    Returns:
        None
    """

    with open("conversion_results.txt", "w", encoding="utf-8") as file:
        file.write("NUMBER\tDEC\tBIN\tHEX\n")
        print("NUMBER\tDEC\tBIN\tHEX")
        for i, number in enumerate(data):
            print(f"{i+1}\t{number}\t{to_binary(number)}\t{to_hex(number)}")
            file.write(f"{i+1}\t{number}\t{to_binary(number)}\t{to_hex(number)}\n")


def main():
    """
    Entry point of the program.
    Reads a file, converts the numbers in the file, and prints the converted numbers.
    Calculates and prints the elapsed time for the conversion process.
    Appends the elapsed time to a file named "ConversionResults.txt".
    """
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py <file_path>")
        sys.exit(1)

    start = time.time()
    file_path = sys.argv[1]


    data, lines_read = read_data(file_path)
    if lines_read > 0:
        convert_and_print(data)
        end = time.time()
        elapsed_time = end - start

        print(f"TIME:\t{elapsed_time}")

        with open("conversion_results.txt", "a", encoding="utf-8") as file:
            file.write(f"TIME:\t{elapsed_time}\n")

    else:
        print("No data found.")


if __name__ == "__main__":
    main()
