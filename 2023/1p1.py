with open("1.txt", "r") as file:
    lines = file.read().split("\n")
    digits = []
    for line in lines:
        if (line == ""):
            continue

        in_line_digits = []
        for char in line:
            if (char.isdigit()):
                in_line_digits.append(char)

        if (len(in_line_digits) == 1):
            digits.append(in_line_digits[0] * 2)
        else:
            digits.append(in_line_digits[0] + in_line_digits[-1])

    digits_sum = 0
    for i in digits:
        digits_sum += int(i)
    print(digits_sum)