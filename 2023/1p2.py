with open("1.txt", "r") as file:
    lines = file.read().splitlines()

    digits_sum = 0
    for line in lines:
        in_line_digits = []
        number_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        pos_list = []
        for number in number_list:
            pos = line.find(number)
            while pos != -1:
                pos_list.append([pos, number])
                pos = line.find(number, pos + 1)

        pos_list.sort()
        for number in pos_list:
            if (len(number[1]) == 1):
                in_line_digits.append(number[1])
            else:
                in_line_digits.append(number_list[(number_list.index(number[1]) - 9)])

        digits_sum += int(in_line_digits[0] + in_line_digits[-1])

    print(digits_sum)