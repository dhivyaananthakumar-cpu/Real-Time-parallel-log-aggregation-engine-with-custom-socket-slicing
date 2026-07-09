import struct
import os

files = [
    "mumbai_WARNING.bin",
    "mumbai_ERROR.bin",
    "mumbai_INFO.bin",
    "mumbai_DEBUG.bin",
    "chennai_WARNING.bin",
    "chennai_ERROR.bin",
    "chennai_INFO.bin",
    "chennai_DEBUG.bin",
    "bangalore_WARNING.bin",
    "bangalore_ERROR.bin",
    "bangalore_INFO.bin",
    "bangalore_DEBUG.bin"
]

for file_name in files:

    if not os.path.exists(file_name):
        continue

    print("\n====================================")
    print(file_name)
    print("====================================")

    with open(file_name, "rb") as file:

        while True:

            size = file.read(4)

            if not size:
                break

            length = struct.unpack("I", size)[0]

            data = file.read(length)

            print(data.decode("utf-8"))