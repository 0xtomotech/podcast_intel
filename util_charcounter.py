def count_chars(filename):
    with open(filename, 'r') as file:
        char_count = 0
        for line in file:
            char_count += len(line)
        return char_count


if __name__ == "__main__":
    chars = count_chars('./russillo_blowouts.txt')
    print(f'Total characters: {chars}')
