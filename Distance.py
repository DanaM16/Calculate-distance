import haversine as hs

"""This program uses the "Haversine" formula to calculate the great-circle distance between two points – that is,
 the shortest distance over the earth’s surface – giving an ‘As the crow flies’ distance between the points. """

print("This program uses the 'Haversine' formula to calculate the great-circle distance between two points – that is,"
      " the shortest distance over the earth’s surface.")


def celo():

    # User's input
    first_city = input("Please name the first point: ")
    f_1 = float(input("Please enter the first coordinate: "))
    f_2 = float(input("Please enter the second coordinate: "))

    second_city = input("Please name the second point: ")
    s_1 = float(input("Please enter the first coordinate: "))
    s_2 = float(input("Please enter the second coordinate: "))

    f_coor = (f_1, f_2)
    s_coor = (s_1, s_2)

    # Formulas for different measurements
    result = round(hs.haversine(f_coor, s_coor), 2)
    mi = round(result * 0.62137, 2)
    nm = round(result / 1.852, 2)
    st = round(result * 1312.336, 2)

    print("km for kilometers, mi for miles, nm for nautical miles and st for steps")

    kilometers = f"The shortest distance between {first_city} and {second_city} is {result} kilometers."
    miles = f"The shortest distance between {first_city} and {second_city} is {mi} miles."
    nautical = f"The shortest distance between {first_city} and {second_city} is {nm} nautical miles."
    step = f"The shortest distance between {first_city} and {second_city} is {st} steps."

    while True:

        metric = input("Do you want to use km, mi, nm or st? ")

        if metric == "km":
            return kilometers
        elif metric == "mi":
            return miles
        elif metric == "nm":
            return nautical
        elif metric == "st":
            return step
        else:
            print("Please try again!")
            print(metric)


print(celo())


def again():

    # Try again?
    while True:
        another = input("Try again? 'y' for yes or 'n' for no. ")

        if another == "y":
            print(celo())

        elif another == "n":
            print("Thank you and goodbye!")
            break

        else:
            print(another)


again()
