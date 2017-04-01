import random
num = random.ranin(1, 99)
guess = int(raw_input("Enter a number between 1 - 99: ""))
while n != "guess":
  print
  if guess < num:
      print "guess is high"
      guess = int(raw_input("Enter a number between 1 - 99: "))
  elif guess > num:
      guess = int(raw_input("Enter a number between 1 - 99: "))
  else:
      print "you guessed it!"
  print
