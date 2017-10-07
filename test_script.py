
import pandas as pd
from pandas import DataFrame
import pickle

df = pd.read_csv("PR-41713 product_attributes_train.csv", error_bad_lines=False,
                 names  = ['id', 'attribute_name',
                           'attribute_type',
                           'attribute_value'], sep = ";")
print()
print('/////////////')
#print(df)
#print(df[1:])

print(df[1:]['attribute_name'].value_counts())

print(df[1:]['attribute_value'].value_counts())


lst = df[1:]['attribute_name'].unique()
ss = {}

lst2 = df[1:][['attribute_name', 'attribute_value']]

print(lst2.sort_values(by='attribute_name'))

lst3 = {}
i=0

for x in lst2["attribute_name"].unique():
    lst3[x] = {}



for x in lst2["attribute_name"].unique():

    for k, v in zip(lst2["attribute_name"], lst2["attribute_value"]):
        if x == k:
            if v in lst3[x]:
                lst3[x][v] += 1
            else:
                lst3[x][v] = 1


print(lst3)

df2 = DataFrame(lst3)
print(df2)