import random

print ("Hello, Idiots!")
message = "Hello, Idiots!"
print (message)

roll = random.randrange(1, 6)
print (roll)

numDice = input("How many dice are we rolling?")
print ("Great, we're rolling " + numDice + " dice!")
sides = input ("Now how many sides do they have?")
print ("So we have " + numDice + " of " + sides + " apiece, or " + numDice + "d" + sides)
print ("Your result is: " + (sides * numDice))
print ("Hope you smashed that orc!")