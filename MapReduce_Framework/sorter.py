def sort_partition(file_name):

    with open(file_name, "r") as file:
        data = file.readlines()

    data.sort()

    with open(file_name, "w") as file:
        file.writelines(data)