with open("input") as infile:
    data = infile.readline()


def find_start_of_window(string, window_length) -> int:
    target_char_count = window_length
    window = [x for x in string[:target_char_count]]
    for index, char in enumerate(string):
        window = window[1:]
        window.append(char)
        if len(set(window)) == target_char_count:
            return index + 1


# Part 1
print(find_start_of_window(data, 4))
# Part 2
print(find_start_of_window(data, 14))
