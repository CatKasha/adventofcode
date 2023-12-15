with open("3.txt", "r") as file:
    lines = file.read().splitlines()

    num_pos = []
    symbol_pos = []
    for line in lines:
        line_num_pos = []
        line_symbol_pos = []

        start_pos = -1
        end_pos = 0
        for char_pos, char in enumerate(line):
            if (char.isdigit()):
                if (start_pos == -1 or end_pos != char_pos - 1):
                    start_pos = char_pos
                    end_pos = char_pos
                else:
                    end_pos = char_pos

                if (char_pos == len(line) - 1):
                    line_num_pos.append([start_pos, end_pos])
            else:
                if (char_pos - 1 == end_pos and start_pos != -1):
                    line_num_pos.append([start_pos, end_pos])

                if (char == "."):
                    continue
                else:
                    line_symbol_pos.append(char_pos)

        num_pos.append(line_num_pos)
        symbol_pos.append(line_symbol_pos)

    parts_sum = 0
    for line_pos in range(len(lines)):

        if (num_pos[line_pos] != [] and symbol_pos[line_pos] != []):
            for num in num_pos[line_pos]:
                for symbol in symbol_pos[line_pos]:
                    if (num[0] - 1 == symbol or num[1] + 1 == symbol):
                        parts_sum += int(lines[line_pos][num[0] : num[1] + 1])

        if (symbol_pos[line_pos] != []):
            if (num_pos[line_pos - 1] != [] and line_pos != 0):
                for num in num_pos[line_pos - 1]:
                    for symbol in symbol_pos[line_pos]:
                        if (num[0] - 1 <= symbol and symbol <= num[1] + 1):
                            parts_sum += (int(lines[line_pos - 1][num[0] : num[1] + 1]))

            if (num_pos[line_pos + 1] != [] and line_pos != len(lines) - 1):
                for num in num_pos[line_pos + 1]:
                    for symbol in symbol_pos[line_pos]:
                        if (num[0] - 1 <= symbol and symbol <= num[1] + 1):
                            parts_sum += (int(lines[line_pos + 1][num[0] : num[1] + 1]))

    print(parts_sum)