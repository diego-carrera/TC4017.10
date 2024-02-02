"""
Program: compute_statistics.py
Author: Diego Carrera Nicholls
Date: 2023-01-30
Version: 1.0
Description: Compute statistics for a given dataset.
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
                    value = float(line.strip())
                    data.append(value)
                except ValueError:
                    print(f"Error in line {lines_read+1}: {line.strip()} is not a number.")

                lines_read += 1

    except FileNotFoundError:
        print("Error: File does not exist.")
        sys.exit(1)
    return data, lines_read


def mean(data):
    """
    Calculate the mean of a list of numbers.

    Parameters:
    data (list): A list of numbers.

    Returns:
    float: The mean of the numbers.
    """
    return sum(data) / len(data)

def median(data):
    """
    Calculate the median value of a given list of data.

    Parameters:
    data (list): A list of numeric values.

    Returns:
    float: The median value of the data.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    middle = n // 2
    if n % 2 == 0:
        median_value = (sorted_data[middle - 1] + sorted_data[middle]) / 2
    else:
        median_value = sorted_data[middle]
    return median_value

def mode(data):
    """
    Calculates the mode of a given list of data.

    Parameters:
    data (list): The list of data for which the mode needs to be calculated.

    Returns:
    The mode value of the given data. If there is more than one mode,
    it returns the first mode encountered.

    If all values in the data are the same, it returns None.
    """
    frequecy = {}
    for i in data:
        if i in frequecy:
            frequecy[i] += 1
        else:
            frequecy[i] = 1

    max_frequecy = max(frequecy.values())
    mode_value = [k for k, v in frequecy.items() if v == max_frequecy]

    if len(mode_value) == len(data):
        return None

    return mode_value[0]


def variance(data, mean_value):
    """
    Calculate the variance of a given list of data.

    Parameters:
    data (list): A list of numeric values.

    Returns:
    float: The variance of the data.
    """
    return sum((x - mean_value) ** 2 for x in data) / (len(data) - 1)

def standard_deviation(data, mean_value):
    """
    Calculate the standard deviation of a given list of data.

    Parameters:
    data (list): A list of numeric values.

    Returns:
    float: The standard deviation of the data.
    """
    # STDEVP function in Excel uses n instead of n - 1
    _variance = sum((x - mean_value) ** 2 for x in data) / len(data)
    return _variance ** 0.5

def main():
    """
    Compute statistics for a given dataset.

    Usage: python compute_statistics.py <file_path>

    Args:
        file_path (str): The path to the file containing the dataset.

    Returns:
        None
    """
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py <file_path>")
        sys.exit(1)

    start = time.time()

    file_path = sys.argv[1]
    data, lines = read_data(file_path)

    count_value = len(data)
    mean_value = mean(data)
    median_value = median(data)
    mode_value = mode(data)
    variance_value = variance(data, mean_value)
    standard_deviation_value = standard_deviation(data, mean_value)
    end = time.time()
    elapsed_time = end - start

    print(f"LINES:\t{lines}")
    print(f"COUNT:\t{count_value}")
    print(f"MEAN:\t{mean_value}")
    print(f"MEDIAN:\t{median_value}")
    print(f"MODE:\t{mode_value}")
    print(f"SD:\t{standard_deviation_value}")
    print(f"VAR:\t{variance_value}")

    print(f"TIME:\t{elapsed_time}")

    # save the results to a file statistics_results.txt
    with open("statistics_results.txt", "w", encoding="utf-8") as file:
        file.write(f"LINES:\t{lines}\n")
        file.write(f"COUNT:\t{count_value}\n")
        file.write(f"MEAN:\t{mean_value}\n")
        file.write(f"MEDIAN:\t{median_value}\n")
        file.write(f"MODE:\t{mode_value}\n")
        file.write(f"SD:\t{standard_deviation_value}\n")
        file.write(f"VAR:\t{variance_value}\n")
        file.write(f"TIME:\t{elapsed_time}\n")

if __name__ == "__main__":
    main()
