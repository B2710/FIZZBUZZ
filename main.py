for x in range(101):
  if x == 0:
      continue
  if x % 3 == 0 and x % 5 == 0:
   if True:
    print("FIZZBUZZ")
    continue  
  if x % 3 == 0:
   if True:
    print("FIZZ")
    continue
  if x % 5 == 0:
   if True:
    print("BUZZ")
    if x == 100:
     print("You have reached 100")
    else: 
     continue
  else: 
   print(x)