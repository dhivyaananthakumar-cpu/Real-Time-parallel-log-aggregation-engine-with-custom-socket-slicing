from collections import defaultdict

def reducer(file_name):

    result = defaultdict(int)

    with open(file_name, "r") as file:

        for line in file:

            key, value = line.strip().split(",")

            result[key] += int(value)

    return result