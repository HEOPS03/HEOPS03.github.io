def main():
    ROUND = 0
    SQUARE = 1
    FIGURE = 2

    RIGHT_BRACKETS = ")]}"
    LEFT_BRACKETS = "([{"

    YES = "YES"
    NO = "NO"

    result = YES
    
    countOpen = [0, 0, 0]

    input = "((("
    temp = ""

    index = 0
    length = len(input)

    while index < length and result == YES:
        bracket = input[index]
        if (bracket in RIGHT_BRACKETS):
            countOpen[RIGHT_BRACKETS.index(bracket)] += 1
        if (bracket in LEFT_BRACKETS):
            countOpen[LEFT_BRACKETS.index(bracket)] -= 1

        if bracket in RIGHT_BRACKETS:
            leftBracket = LEFT_BRACKETS[RIGHT_BRACKETS.index(bracket)]
            tempIndex = len(temp) - 1
            bracket = temp[tempIndex]
            tempCountOpen = [0, 0, 0]
            while tempIndex >= 0 and temp[tempIndex] != leftBracket or (temp[tempIndex] == leftBracket and (countOpen[0] != 0 or countOpen[1] != 0 or countOpen[2] != 0)):
                bracket = temp[tempIndex]

                if (bracket in RIGHT_BRACKETS):
                    tempCountOpen[RIGHT_BRACKETS.index(bracket)] += 1
                if (bracket in LEFT_BRACKETS):
                    tempCountOpen[LEFT_BRACKETS.index(bracket)] -= 1
                tempIndex -= 1
                pass

            if countOpen[0] != 0 or countOpen[1] != 0 or countOpen[2] != 0:
                result = NO
        
        temp += input[index]
        index += 1

    if countOpen[0] != 0 or countOpen[1] != 0 or countOpen[2] != 0:
        result = NO
    print(result)





if __name__ == "__main__":
    print("start")
    main()