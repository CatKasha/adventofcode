with open("1.txt", "r") as file:
    lines = file.read().splitlines()

    digits_sum = 0
    for line in lines:
        in_line_digits = []
        for char in line:
            if (char.isdigit()):
                in_line_digits.append(char)

        digits_sum += int(in_line_digits[0] + in_line_digits[-1])

    print(digits_sum)