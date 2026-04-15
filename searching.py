from pathlib import Path
import json


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


def main():
    my_data = read_data('sequential.json', 'ordered_numbers')
    print(my_data)
    searched = binary_search(my_data, 72)
    print(searched)


if __name__ == "__main__":
    main()
