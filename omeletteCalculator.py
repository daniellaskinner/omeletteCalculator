import math

numberOfEggsInABox = 6
numberOfEggBoxes = int(input('How many egg boxes you got?'))
eggsOmeletteNeeds = 4

totalOmelettesMakeable = math.floor((numberOfEggsInABox * numberOfEggBoxes) / eggsOmeletteNeeds)

if totalOmelettesMakeable == 1 and numberOfEggBoxes == 1:
    output = "You can make {} omelette with {} box of eggs.".format(totalOmelettesMakeable, numberOfEggBoxes)
elif totalOmelettesMakeable > 1 and numberOfEggBoxes == 1:
    output = "You can make {} omelettes with {} box of eggs.".format(totalOmelettesMakeable, numberOfEggBoxes)
else:
    output = "You can make {} omelettes with {} boxes of eggs.".format(totalOmelettesMakeable, numberOfEggBoxes)

print(output)