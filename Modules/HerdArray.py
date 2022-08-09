# region Task

##############################################################################################################################################
#|| A farmer keeps the record of a heard of cows. Every cow has a unique 3 - digit identity code                                           ||#
#|| Farmer has table of cows of a constant arbitary size HeardSize stored as ID Codes in array Herd[]                                      ||#
#||                                                                                                                                        ||#
#|| Each cow can be milked twice each day of the week. The farmer records the yield in liters to one decimal place.                        ||#
#|| This means the cows yields milk 14 times a week. The yield is recorded in 2D arrar HerdYield[][].                                      ||#
#||                                                                                                                                        ||#
#|| At the end of the week, the farmer finds the total and average yield of each cow.                                                      ||#
#|| Calculated                                                                                                                             ||#
#||                                                                                                                                        ||#
#|| The farmer identifies the cow with the best yield that week.                                                                           ||#
#|| Output identity code of cow with highest yield.                                                                                        ||#
#||                                                                                                                                        ||#
#|| The farmer also identifies the cows that yielded less than 12 litres of milk on four or more days.                                     ||#
#|| Keep a count of the number of times the cow yielded less and store the count. If the count exceeds 4, add the cow to DefectiveHerd[].  ||#
#||                                                                                                                                        ||#
##############################################################################################################################################

# endregion

import random

HerdSize = int("10")
Herd = [x for x in range(0, HerdSize)]
HerdYield = [[yieldTime for yieldTime in range(0, 14)] for cow in range(HerdSize)]
HighestYield = 12
BestCow = 0
DefectiveCows = []

for cow in Herd:
    TotalYield = 0
    defectiveDays = 0
    for yieldTime in range(0, 14):
        yieldVolume = random.randint(10, 20)
        # Validate input
        HerdYield[cow][yieldTime] = yieldVolume
        TotalYield += yieldVolume

        if yieldVolume < 12:
            defectiveDays += 1
            print(yieldVolume, defectiveDays)
            if defectiveDays == 4:
                DefectiveCows.append(cow)
                

    AverageYield = TotalYield / 14
    if TotalYield > HighestYield:
        HighestYield = TotalYield

print(Herd)
print("Highest yield and cow: ", HighestYield, BestCow)
print("Defective cows: ", DefectiveCows)
print(HerdYield)