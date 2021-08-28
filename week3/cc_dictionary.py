inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    print("Total snowfall inches:", total_inches)


print_total_snowfall(inches_snow)

# using while loop to try to catch non numeric and negative values
# user must enter a value of 0 or greater
while True:
    thurs_snow = input("How many inches of snow fell on Thursday? ")

    if thurs_snow.isdigit():
        break

    print("Value must be a digit ==> 0 or greater")


if int(thurs_snow) >= 0:
    inches_snow["Thursday"] = int(thurs_snow)
    print_total_snowfall(inches_snow)
