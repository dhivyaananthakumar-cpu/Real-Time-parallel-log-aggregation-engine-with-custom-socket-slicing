import os
from multiprocessing import Process

from splitter import split_input
from mapper import mapper
from partition import partition
from sorter import sort_partition
from reducer import reducer

REDUCERS = 4


try:
    with open("input/input.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Error: input/input.txt not found!")
    exit()


if len(lines) == 0:
    print("Error: input.txt is empty!")
    exit()


split_data = split_input(lines, REDUCERS)

mapped_data = []

for chunk in split_data:
    mapped_data.extend(mapper(chunk))

partition(mapped_data, REDUCERS)

processes = []

for i in range(REDUCERS):
    filename = f"intermediate/part-{i}.txt"
    p = Process(target=sort_partition, args=(filename,))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

final_result = {}

for i in range(REDUCERS):
    filename = f"intermediate/part-{i}.txt"
    result = reducer(filename)

    for key, value in result.items():
        final_result[key] = final_result.get(key, 0) + value

os.makedirs("output", exist_ok=True)

with open("output/result.txt", "w") as file:
    file.write("Category,TotalOrders\n")

    for key in sorted(final_result):
        file.write(f"{key},{final_result[key]}\n")

print("================================")
print("MapReduce Framework Completed")
print("================================")

for key in sorted(final_result):
    print(f"{key} : {final_result[key]}")