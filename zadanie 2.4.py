try:
  num_a = int(input("Enter the first value: "))
  num_b = int(input("Enter the second value: "))
  num_c = int(input("Enter the third value: "))
  m = max(num_a, num_b, num_c )
  print("Largest value is:",m)

except ValueError:
  print("I can only work on integers.")
