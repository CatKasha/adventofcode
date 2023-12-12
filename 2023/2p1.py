with open("2.txt", "r") as file:
    lines = file.read().splitlines()

    sum_game_ids = 0
    for i, game in enumerate(lines):
        game = game.split(": ")[1].split("; ")
        for color_set in game:
            color_set = color_set.split(", ")
            for color in color_set:
                color = color.split(" ")
                if (color[1] == "red"):
                    if (int(color[0]) > 12):
                        break
                if (color[1] == "green"):
                    if (int(color[0]) > 13):
                        break
                if (color[1] == "blue"):
                    if (int(color[0]) > 14):
                        break
            else:
                continue
            break
        else:
            sum_game_ids += i + 1

    print(sum_game_ids)