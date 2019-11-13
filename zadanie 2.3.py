try:
    num_float = float(input("Enter a float value "))
    if num_float > 0:
        print("Value is positive +1 ")
    else:
        print("Value is negative -1 ")
except ValueError:
    print("I can only work on float value!")
