for x in range(101):
  if x == 0:
    continue
  elif x % 3 == 0 and x % 5 == 0:
    print("FIZZBUZZ")
  elif x % 3 == 0:
    print("FIZZ")
  elif x % 5 == 0:
    print("BUZZ")
    if x == 100:
     print("You have reached 100")
  else: 
   print(x)