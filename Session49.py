"""

    Apriori Algorithm

    DataSet:
    TID Cover Guard PowerBank Charger
    1   1     1     1         1
    2   1     0     1         1
    3   0     0     1         1
    4   0     1     0         0
    5   1     1     1         1
    6   1     1     0         1

    1. Support
    Support(Cover) = Number of Transaction in which Cover appeared / Total Transactions
    Support(Cover) = 4/6 => 0.66

    2. Confidence
    Confidence({Cover,Guard} => {PowerBank}) = Support({Cover,Guard,PowerBank}) / Support({Cover,Guard})
                                            = 2/6 / 3/6 = 0.66

    3. Lift
    Lift({Cover,Guard} => {PowerBank}) = Support({Cover,Guard,PowerBank}) / Support(Cover) * Support(Guard)
                                       = 2/6 / 4/6 * 4/6
                                       = 0.77
    If Lift(x=>y) = 1, no correlation, do not consider
    > If Lift(x=>y)> 1, positive correlation, likely to be bought | :)
    If Lift(x=>y)< 1, negative correlation, unlikely to be bought

    4. Conviction
    Conviction({Cover,Guard} => {PowerBank}) = 1 - Support(PowerBank) / 1 - Confidence({Cover,Guard} => {PowerBank})
                                              1 - 4/6 / 1 - 2/6 / 3/6 = 1


    If Conviction(x=>y) = 1, x has no relation with y
    > If Conviction(x=>y) > 1, More the Value, Higher the Interest of item being purchased

    Frequency Table for Items:
    Item        Frequency

    Cover       4
    Guard       4
    PowerBank   4
    Charger     5

    We need to assume Support Threshold = 3
    Item        Frequency
    Cover       4
    Guard       4
    PowerBank   4
    Charger     5

    Lets make pairs
    Item                    Frequency
    Cover, Guard            3
    Cover, PowerBank        3
    Cover, Charger          4
    Guard, PowerBank        2
    Guard, Charger          3
    PowerBank, Charger      4

    Support Threshold > 3
    Hence,
    Cover, Charger          4
    PowerBank, Charger      4


"""

import pandas as pd
from apyori import apriori

# pip install apyori

df = pd.read_csv("transactions.csv", header=None)
print(df)

print(df.shape)

# Convert data frame as list of lists
records = []
for i in range(df.shape[0]):
    records.append([str(df.values[i, j]) for j in range(df.shape[1])])

# List of Lists :)
print(records)

associateionRules = apriori(records, min_support=0.50,  min_confidence=0.7, min_lift=1, min_length=2)
print(list(associateionRules))