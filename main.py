def main():
    name_input = input("camelCase: ")
    print("".join(convert_to_snake_case(name_input)))


def convert_to_snake_case(name):
    snake_case = []
    for letter in name:
        if letter.isupper():
            snake_case.append("_")
            snake_case.append(letter.lower())
        else:
            snake_case.append(letter)
    return snake_case


main()
