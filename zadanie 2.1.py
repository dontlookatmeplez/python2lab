print("This utility will show you whether a integer is an odd or even number.")
print("######################################################################")
num = int(input("To continue enter a integer: "))
    #allows you to put a value that is a integer, and then makes use of it
if (num % 2) == 0:
    #divides your integer by 2 and shows if remainder is equal to 0
    print("{0} is even".format(num))
    #{0} together with .format(***) allows you to use your defined (as "num") values in brackets
else:
    print("{0} is odd".format(num))
