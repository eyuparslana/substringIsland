
def get_all_substrings(entry):
    length = len(entry)
    return [entry[i:j + 1] for i in range(length) for j in range(i, length)]


def get_island_count(entry, substring):
    s_len = len(substring)
    tmp_list = ['0'] * len(entry)

    for i in range(len(entry)):
        if entry[i] == substring[0] and entry[i: i + s_len] == substring[0:s_len]:
            for j in range(i, i + s_len):
                tmp_list[j] = entry[j]

    splited_islands = ''.join(tmp_list).split('0')
    island_count = 0

    for island in splited_islands:
        if island:
            island_count += 1

    return island_count, tmp_list


def main():
    entry = input("Enter a String: ")
    number = int(input("Enter a Number: "))

    substrings = set(get_all_substrings(entry))
    result = 0

    print(substrings)
    print("{} has {} substrings".format(entry, len(substrings)))

    for substring in substrings:
        island_count, tmp_list = get_island_count(entry, substring)
        if island_count == number:
            result += 1
            print(f'{tmp_list} -->> {substring}')

    print(f'There are {result} different substrings of "{entry}" that produce exactly {number} islands.')


if __name__ == '__main__':
    main()
