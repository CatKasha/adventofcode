with open("2.txt", "r") as file:
    lines = file.read().splitlines()

    sum_power = 0
    for game in lines:
        max_rbg = [0, 0, 0]
        for color_set in game.split(": ")[1].split("; "):
            for color in color_set.split(", "):
                color = color.split(" ")
                if (color[1] == "red"):
                    if (int(color[0]) > max_rbg[0]):
                        max_rbg[0] = int(color[0])

                if (color[1] == "green"):
                    if (int(color[0]) > max_rbg[1]):
                        max_rbg[1] = int(color[0])

                if (color[1] == "blue"):
                    if (int(color[0]) > max_rbg[2]):
                        max_rbg[2] = int(color[0])

        sum_power += max_rbg[0] * max_rbg[1] * max_rbg[2]

    print(sum_power)