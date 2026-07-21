def split_input(lines, num_splits):

    if not lines:
        return []

    header = lines[0]
    data = lines[1:]

    chunk_size = max(1, len(data) // num_splits)

    chunks = []

    for i in range(num_splits):
        start = i * chunk_size

        if i == num_splits - 1:
            end = len(data)
        else:
            end = (i + 1) * chunk_size

        chunk = [header] + data[start:end]
        chunks.append(chunk)

    return chunks