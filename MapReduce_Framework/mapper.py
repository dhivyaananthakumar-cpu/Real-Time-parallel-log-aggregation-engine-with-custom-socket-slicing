def mapper(lines):

    mapped_data = []

    for line in lines[1:]:

        data = line.strip().split(",")

        if len(data) == 11:

            category = data[4]

            mapped_data.append((category, 1))

    return mapped_data