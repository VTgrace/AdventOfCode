def main():
    input_file = "../input.txt"
    totalVoltage = 0

    with open(input_file, "r") as file:
        for line in file:
            stripped = line.strip()

            # start out with first two digits being the highest sum
            firstDig = int(stripped[0])
            secondDig = int(stripped[1])

            for i in range(1, len(stripped)):
                currNum = int(stripped[i])

                if ((i != len(stripped) - 1) and currNum > firstDig):
                    firstDig = currNum
                    secondDig = int(stripped[i + 1])
                elif (currNum > secondDig):
                    secondDig = currNum

            currVoltage = int(str(firstDig) + str(secondDig))
            totalVoltage += currVoltage

        print(totalVoltage)

if __name__ == "__main__":
    main()