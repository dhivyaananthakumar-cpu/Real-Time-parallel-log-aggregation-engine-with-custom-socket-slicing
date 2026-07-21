import os

def partition(mapped_data, reducers):

    os.makedirs("intermediate", exist_ok=True)

    files = []

    for i in range(reducers):
        files.append(open(f"intermediate/part-{i}.txt", "w"))

    for key, value in mapped_data:

        index = hash(key) % reducers

        files[index].write(f"{key},{value}\n")

    for file in files:
        file.close()