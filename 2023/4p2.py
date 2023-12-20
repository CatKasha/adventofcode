with open("4.txt", "r") as file:
    lines = file.read().splitlines()

    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        win_num_s, nums = line.split(": ")[1].split(" | ")
        win_num_s = win_num_s.split()
        nums = nums.split()

        matches = 0
        for win_num in win_num_s:
            if (win_num in nums):
                matches += 1

        if (matches != 0):
            for j in range(matches):
                cards[i + 1 + j] += 1 * cards[i]

    print(sum(cards))