with open("4.txt", "r") as file:
    lines = file.read().splitlines()

    card_points = []
    for i, line in enumerate(lines):
        win_num_s, nums = line.split(": ")[1].split(" | ")
        win_num_s = win_num_s.split()
        nums = nums.split()

        card_points.append(0)
        for win_num in win_num_s:
            if (win_num in nums):
                if(card_points[i] == 0):
                    card_points[i] = 1
                else:
                    card_points[i] = card_points[i] * 2

    print(sum(card_points))