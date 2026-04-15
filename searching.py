import time
from pathlib import Path
import json
import matplotlib

from generators import ordered_sequence


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
    with open (file_path, "r") as file:
        data = json.load(file)
        if field in data.keys():
            return data[field]
        else:
            return None


def linear_search(sekvence, number):
    positions = []
    count = 0
    for i, sek in enumerate(sekvence):
        if sek == number:
            positions.append(i)
            count +=1
    all = {"positions": positions, "count": count}
    return all


def binary_search(searched_list, number):
    leva = 0
    prava = len(searched_list) -1

    while leva <= prava:
        middle = (leva+ prava) // 2
        if searched_list[middle] == number:
            return middle
        elif searched_list[middle] < number:
            leva = middle + 1
        elif searched_list[middle] > number:
            prava = middle -1
    return None


def test_complexity(seznam):
    time_linear = []
    time_binary = []
    for n in seznam:
        unordered = unordered_sequence(n)
        ordered = ordered_sequence(n)
        duration_linear = 0
        durationbinary = 0
        repetition = 100
        for meas in range(repetition):
            start = time.perf_counter()
            found = linear_search(my_data, number)
            end = time.perf_counter()
            duration += end - start
            start_binary = time.perf_counter()
            found_bin = binary_search(ordered, number)
            end_binary = time. perf_counter()
            durationbinary += end_binary - start_binary
        time_linear.append(duration_linear/ repetition)
        time_binary.append(durationbinary/repetition)
    print(time_linear)
    print(time_binary)
    plt.plot(seznam, time_linear)
    plt.plot(seznam, time_binary)

    plts.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("Porovnání vyhledávacíh algoritmů")
    plt.show()


def pattern_search():


def main():
    my_data = read_data('sequential.json', 'ordered_numbers')
    print(my_data)
    number = 72
    duration = 0
    repetitions = 100
    for measurments in range(100):
        start = time.perf_counter()
        found = linear_search(my_data, number)
        end = time.perf_counter()
        duration += end - start
    print(found)
    print(duration/repetitions)
    searched = binary_search(my_data, 72)
    print(searched)



if __name__ == "__main__":
    main()
