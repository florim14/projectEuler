
def leapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def sundayOrNot(numberToCheck):
    if numberToCheck % 7 == 0:
        return 1
    return 0


def countSundays():
    months = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    currentDay = 2
    numberOfSundays = 0
    for year in range(1901, 2001):
        months[1] = 28 + leapYear(year)
        for month in months:
            currentDay += month % 7
            numberOfSundays += sundayOrNot(currentDay)

    print(f'Number of Sundays is: {numberOfSundays}')


if __name__ == '__main__':
    countSundays()
