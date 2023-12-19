with open("4.txt", "r") as file:
    lines = file.read().splitlines()

    card_points = []
    for i, line in enumerate(lines):
        win_num_s, nums = line.split(": ")[1].split(" | ")
        win_num_s = win_num_s.split()
        nums = nums.split()

        card_points.append(-1)
        for win_num in win_num_s:
            if (win_num in nums):
                if(card_points[i] == -1):
                    card_points[i] = 1
                else:
                    card_points[i] = card_points[i] * 2

    card_points_sum = 0
    for point in card_points:
        if (point != -1):
            card_points_sum += point

    print(card_points_sum)