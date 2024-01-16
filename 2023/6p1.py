with open("6.txt", "r") as file:
    lines = file.read().splitlines()

    times = [int(i) for i in lines[0].split(" ") if i.isdigit()]
    distance = [int(i) for i in lines[1].split(" ") if i.isdigit()]

    multiply_vals = 1
    for i in range(len(times)):
        min_hold = 0
        max_hold = 0
        for hold_time in range(1, times[i] + 1):
            if ((times[i] - hold_time) * hold_time > distance[i]):
                min_hold = hold_time
                break

        for hold_time in range(times[i], 0, -1):
            if ((times[i] - hold_time) * hold_time > distance[i]):
                max_hold = hold_time
                break
        multiply_vals *= max_hold - min_hold + 1

    print(multiply_vals)