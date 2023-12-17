with open("3.txt", "r") as file:
    lines = file.read().splitlines()

    num_pos = []
    star_pos = []
    for line in lines:
        line_num_pos = []
        line_star_pos = []

        start_pos = -1
        end_pos = 0
        for char_pos, char in enumerate(line):
            if (char.isdigit()):
                if (start_pos == -1 or end_pos != char_pos - 1):
                    start_pos = char_pos
                end_pos = char_pos

                if (char_pos == len(line) - 1):
                    line_num_pos.append([start_pos, end_pos])
            else:
                if (end_pos == char_pos - 1 and start_pos != -1):
                    line_num_pos.append([start_pos, end_pos])

                if (char == "*"):
                    line_star_pos.append(char_pos)

        num_pos.append(line_num_pos)
        star_pos.append(line_star_pos)

    gear_ratios = 0
    for line_pos in range(len(lines)):
        if (star_pos[line_pos] != []):
            # inline
            if (len(num_pos[line_pos]) > 1):
                for star in star_pos[line_pos]:
                    for i in range(len(num_pos[line_pos]) - 1):
                        num1 = num_pos[line_pos][i]
                        num2 = num_pos[line_pos][i + 1]
                        if (star == num1[1] + 1 and star == num2[0] - 1):
                            gear_ratios += (int(lines[line_pos][num1[0] : num1[1] + 1])
                                          * int(lines[line_pos][num2[0] : num2[1] + 1]))
            # upper
            if (line_pos > 0 and len(num_pos[line_pos - 1]) > 1):
                for star in star_pos[line_pos]:
                    for i in range(len(num_pos[line_pos - 1]) - 1):
                        num1 = num_pos[line_pos - 1][i]
                        num2 = num_pos[line_pos - 1][i + 1]
                        if (star == num1[1] + 1 and star == num2[0] - 1):
                            gear_ratios += (int(lines[line_pos - 1][num1[0] : num1[1] + 1])
                                          * int(lines[line_pos - 1][num2[0] : num2[1] + 1]))
            # lower
            if (line_pos != len(lines) - 1 and len(num_pos[line_pos + 1]) > 1):
                for star in star_pos[line_pos]:
                    for i in range(len(num_pos[line_pos + 1]) - 1):
                        num1 = num_pos[line_pos + 1][i]
                        num2 = num_pos[line_pos + 1][i + 1]
                        if (star == num1[1] + 1 and star == num2[0] - 1):
                            gear_ratios += (int(lines[line_pos + 1][num1[0] : num1[1] + 1])
                                          * int(lines[line_pos + 1][num2[0] : num2[1] + 1]))
            # upper and lower
            if (line_pos > 0 and line_pos != len(lines) - 1 and num_pos[line_pos - 1] != [] and num_pos[line_pos + 1] != []):
                for star in star_pos[line_pos]:
                    reverse = 1
                    if (len(num_pos[line_pos - 1]) < len(num_pos[line_pos + 1])):
                        reverse = -1
                    for i in range(len(num_pos[line_pos - (1 * reverse)])):
                        num_i = num_pos[line_pos - (1 * reverse)][i]
                        for b in range(len(num_pos[line_pos + (1 * reverse)])):
                            num_b = num_pos[line_pos + (1 * reverse)][b]
                            if (num_i[0] - 1 <= star and star <= num_i[1] + 1 and
                                num_b[0] - 1 <= star and star <= num_b[1] + 1):
                                gear_ratios += (int(lines[line_pos - (1 * reverse)][num_i[0] : num_i[1] + 1])
                                              * int(lines[line_pos + (1 * reverse)][num_b[0] : num_b[1] + 1]))
            # upper and inline
            if (line_pos > 0 and num_pos[line_pos - 1] != [] and num_pos[line_pos] != []):
                for star in star_pos[line_pos]:
                    if (len(num_pos[line_pos - 1]) > len(num_pos[line_pos])):
                        for i in range(len(num_pos[line_pos - 1])):
                            num_i = num_pos[line_pos - 1][i]
                            for b in range(len(num_pos[line_pos])):
                                num_b = num_pos[line_pos][b]
                                if (num_i[0] - 1 <= star and star <= num_i[1] + 1 and
                                    num_b[0] - 1 <= star and star <= num_b[1] + 1):
                                    gear_ratios += (int(lines[line_pos - 1][num_i[0] : num_i[1] + 1])
                                                  * int(lines[line_pos    ][num_b[0] : num_b[1] + 1]))
                    else:
                        for i in range(len(num_pos[line_pos])):
                            num_i = num_pos[line_pos][i]
                            for b in range(len(num_pos[line_pos - 1])):
                                num_b = num_pos[line_pos - 1][b]
                                if (num_i[0] - 1 <= star and star <= num_i[1] + 1 and
                                    num_b[0] - 1 <= star and star <= num_b[1] + 1):
                                    gear_ratios += (int(lines[line_pos    ][num_i[0] : num_i[1] + 1])
                                                  * int(lines[line_pos - 1][num_b[0] : num_b[1] + 1]))
            # lower and inline
            if (line_pos != len(lines) - 1 and num_pos[line_pos + 1] and num_pos[line_pos] != []):
                for star in star_pos[line_pos]:
                    if (len(num_pos[line_pos]) > len(num_pos[line_pos + 1])):
                        for i in range(len(num_pos[line_pos])):
                            num_i = num_pos[line_pos][i]
                            for b in range(len(num_pos[line_pos + 1])):
                                num_b = num_pos[line_pos + 1][b]
                                if (num_i[0] - 1 <= star and star <= num_i[1] + 1 and
                                    num_b[0] - 1 <= star and star <= num_b[1] + 1):
                                    gear_ratios += (int(lines[line_pos    ][num_i[0] : num_i[1] + 1])
                                                  * int(lines[line_pos + 1][num_b[0] : num_b[1] + 1]))
                    else:
                        for i in range(len(num_pos[line_pos + 1])):
                            num_i = num_pos[line_pos + 1][i]
                            for b in range(len(num_pos[line_pos])):
                                num_b = num_pos[line_pos][b]
                                if (num_i[0] - 1 <= star and star <= num_i[1] + 1 and
                                    num_b[0] - 1 <= star and star <= num_b[1] + 1):
                                    gear_ratios += (int(lines[line_pos + 1][num_i[0] : num_i[1] + 1])
                                                  * int(lines[line_pos    ][num_b[0] : num_b[1] + 1]))
    print(gear_ratios)