import random
import time
import string

alphabet = []
for i in range(95):
    if string.printable[i] != " ":
        alphabet.append(string.printable[i]) # we are using the default printable character set here, but it can be changed to japanese.
        # you can change the character set to japanese by including a string with all characters you would like in the list. aka str'ABCDEFG'
print(f"Character set: {alphabet}")
cols = int(input("How many columns should it have? (Default fullscreen: 180) > "))
speed = float(input("How fast would you like the effect to go? (0 = zero delay between each row, 1 = a second of delay between each row) > "))
if cols == "": 
    cols = 180
if speed == "":
    speed = 0
deadcols = 15 # number of random columns that will not have characters in them.
leftout = [random.randint(0, 10)] # original value for dead columns list is between 0, 10 but you can change it.
for i in range(deadcols):
    gennumber = leftout[i] + random.randint(1, int(cols/12)) # incrementation ratemax for dead columns list. aka ratemax = 20, [0, 20, 33, 50], never above the ratemax
    if gennumber < cols:
        leftout.append(gennumber)
    else:
        gennumber -= cols - gennumber
collives = [] # generates lives for each column
for i in range(cols):
    collives.append(random.randint(1, 35))
lifechance = 10
while True:
    time.sleep(speed)
    y = "" # row variable used to print the current row
    z = 0 #  variable used to iterate the dead columns array. (leftout[])
    for x in range(cols):
        if ( x/10 - ( x/10 - random.randint(0, lifechance) ) ) == 1: # revives or extends the life of a column in a 1 to $lifechance chance.
            collives[x] += random.randint(0, 10) 
        if x != leftout[z]: # checks if the current column is dead (leftout) or not
            if not collives[x] <= 0: # checks if the current column has any lives left
                y += alphabet[random.randint(0, len(alphabet) - 1)] # ads a random character to the current row
                collives[x] -= 1
            else:
                y += " " # ads a " " for dead column
        else:
            y += " " # ads a " " for left out column
            if not z + 1 > len(leftout) - 1:
                z+=1 # increases the iterations counter for the dead columns array
    print(y)