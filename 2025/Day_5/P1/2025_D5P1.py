def main():
    input_file = "../input.txt"
    count = 0
    ranges = []

    with open(input_file, "r") as file:
        reading_input_ranges = True

        for line in file:
            # Switches modes
            if line == "\n":
                reading_input_ranges= False
                continue
            
            line = line.strip()

            if reading_input_ranges:
                # Split line based on "-" and add to ranges
                curr_range = line.split("-")
                ranges.append(range(int(curr_range[0]), int(curr_range[1])))
            else:
                # Check if current number is in range
                for i in ranges:
                    if (int(line) in i):
                        count += 1
                        break
    
    print(count)        


if __name__ == "__main__":
    main()