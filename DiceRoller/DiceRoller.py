import random

print ("Hello, Idiots!")
message = "Hello, Idiots!"
print (message)

roll = random.randrange(1, 6)
print (roll)

numDice = input("How many dice are we rolling?")
numDice = int(numDice)
print ("Great, we're rolling " + str(numDice) + " dice!")
sides = input ("Now how many sides do they have?")
sides = int(sides)
print ("So we have " + str(numDice) + "d" + str(sides))
result = random.randint(1, sides) * numDice
print ("Your result is: " + str(result))
hitDice = random.randint(1, 20)
print ("And with a hit dice of: " + str(hitDice))
if hitDice == 20:
    print ("You smashed that bloody orc!")
elif hitDice == 1:
    print("Critical Miss!")
else:
    print("Nothing special!")