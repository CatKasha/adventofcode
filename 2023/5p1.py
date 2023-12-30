with open("5.txt", "r") as file:
    lines = file.read().split("\n\n")

    seeds = lines[0].split(" ")[1:]

    for i in range(len(seeds)):
        seeds[i] = int(seeds[i])

    for seed_i in range(len(seeds)):
        for map_i in range(1, 8):
            for map_vals in lines[map_i].splitlines()[1:]:
                vals = map_vals.split(" ")

                destination = int(vals[0])
                source = int(vals[1])
                range_length = int(vals[2])

                if (seeds[seed_i] in range(source, source + range_length)):
                    seeds[seed_i] = destination + seeds[seed_i] - source
                    break
    print(min(seeds))