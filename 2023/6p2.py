with open("6.txt", "r") as file:
    lines = file.read().splitlines()

    time = int("".join(lines[0].split(":")[1].split()))
    distance = int("".join(lines[1].split(":")[1].split()))

    min_hold = 0
    max_hold = 0
    for hold_time in range(1, time + 1):
        if ((time - hold_time) * hold_time > distance):
            min_hold = hold_time
            break

    for hold_time in range(time, 0, -1):
        if ((time - hold_time) * hold_time > distance):
            max_hold = hold_time
            break

    print(max_hold - min_hold + 1)