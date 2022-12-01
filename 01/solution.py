import numpy as np

def main():
    elves = 0
    totals = []

    with open('01\input.txt') as file:
        total_for_this_elf = 0

        for line in file:

            # if we get to the newline seperator then we're at a new elf
            if (line.strip() == ''):
                totals.append(total_for_this_elf)
                elves += 1
                total_for_this_elf = 0
            # otherwise lets add up how much this one is carrying
            else:
                total_for_this_elf += int(line.strip())

    print("We took {} elves with us on this festive trip. The elf with the most was carrying {} calories.".format(elves, np.max(totals)))
    # Output: We took 254 elves with us on this festive trip. The elf with the most was carrying 70698 calories.

    totals.sort()
    top = sum(sorted(totals[-3:]))

    print("The 3 elves with the largest bags were carrying {} calories".format(top))
    # Output: The 3 elves with the largest bags were carrying 206643 calories
    
if __name__ == "__main__":
    main()