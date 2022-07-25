"""Calculate Gregorian Easter using Gauss's algorithm."""

# Betty Kouadio and  Tourkish Hasnan
import sys


def easter_date(year):
    y = year
    a = (y % 19) # the year's position in  cycle
    b = (y % 4) # number of leap days  (Julian calendar)
    c = (y % 7) # non leap year (one day longer)
    k = (y // 100)
    p = ((13 + 8 * k) // 25) 
    q = (k // 4)
    M = (15 - p + k - q) % 30
    N = (4 + k - q) % 7 # starting point for the calculations for each century
    d = ((19 * a) + M) % 30 # number of days (counting from March 21) for the closest following full moon to occur
    e = ((2 * b) + (4 * c) + (6 * d) + N) % 7
    r = 22 + d + e # day in March
    s = d + e - 9 # day in April
    
    # Raise ValueError
    if (y < 1583):
        raise ValueError("Year must be from 1583 to current")

    # Return Easter day
    if (d == 29) and (e == 6) and (s == 26):
        return " Easter fell on April 19"
    elif (d == 28) and (e == 6) and ((((11 * M) + 11) % 30) < 19) and (s == 26):
        return "Easter fell on April 18"
    elif (s > 0):
        return "Easter fell on April {}".format(s)
    else:
        return "Easter fell on March {}".format(r)

          

if __name__ == "__main__":
    try:
        year = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a year as a command-line argument")
    except ValueError:
        sys.exit("could not convert", sys.argv[1], "into an integer")
    print(easter_date(year))