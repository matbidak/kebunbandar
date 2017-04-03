import random
num = random.randint(1, 99)
guess = int(raw_input("Enter a number between 1 - 99: "))
while num != "guess":
  print
  if guess < num:
      print "guess is high"
      guess = int(raw_input("Enter a number between 1 - 99: "))
  elif guess > num:
      print "guess is low"
      guess = int(raw_input("Enter a number between 1 - 99: "))
  else:
      print "you guessed it!"
  print
