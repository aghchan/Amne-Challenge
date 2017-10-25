def main():
    inputFile = open("input.txt", "r")
    numDaysAndWindow = inputFile.readline()
    numDays, windowSize = numDaysAndWindow.strip().split(' ')
    if (not numDays.isdigit() or not windowSize.isdigit()):
        raise Exception("First line contains non digits")
    elif (windowSize > numDays):
        raise Exception("Window size is greater than the number of days provided")

    homeSalePriceList = inputFile.readline().strip().split(' ')
    index = 0
    numOfIncSubRange = 0
    start = index

    while index < len(homeSalePriceList) - 1:
        if (homeSalePriceList[index + 1] <= homeSalePriceList[index]):
            numOfIncSubRange += (index - start) * (index - start + 1) / 2
            index += 1
            start = index
        else:
            index += 1

    return numOfIncSubRange

if __name__ == "__main__":
    print(main())

