while True:
  try:
    mark = int(input("Enter a percentage: "))
    if mark > 100:
      print("You can score as much as 100%!")
    elif 100 >= mark >= 90:
      print("You would score A!")
    elif 89 >= mark >= 79:
      print("You would score B+!")
    elif 78 >= mark >= 68:
      print("You would score B!")
    elif 67 >= mark >= 57:
      print("You would score C+")
    elif 56 >= mark >= 46:
      print("You would score C!")
    elif 45 >= mark >= 0:
      print("You would not pass...")
      
  except ValueError:
    print("Enter a valid value (0-100)")


