
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

for x in lst2["attribute_name"].unique():
    lst3[x] = {}



for x in lst2["attribute_name"].unique():

    for t, h in df[1:]["attribute_name"].value_counts().items():
        lst3[t]['val'] = h

    for k, v in zip(lst2["attribute_name"], lst2["attribute_value"]):
        if x == k:
            if v in lst3[x]:
                lst3[x][v] += 1
            else:
                lst3[x][v] = 1


print(lst3)

#df2 = DataFrame(lst3)
#print(df2)

for x in lst3:

    for y in lst3[x]:

        if y != 'val':
            lst3[x][y] = lst3[x][y] / lst3[x]['val']

print(lst3)



df_desc = pd.read_csv("PR-41713 product_descriptions_train_n3.csv", error_bad_lines=False,
                 names  = ['id', 'name',
                           'description',
                           'third_lvl_category_id',
                           'third_lvl_category_name',
                           'fourth_lvl_category_id',
                           'fourth_lvl_category_name'
                           ], sep = ";")

print(df_desc[1:])


lst_desc = {}

for x in lst2["attribute_name"].unique():
    lst_desc[x] = {}



for x in lst2["attribute_name"].unique():


    for v in lst2["attribute_value"].unique():

        for desc, t_c, f_c in zip(df_desc[1:]["description"], df_desc[1:]["third_lvl_category_name"],
                              df_desc[1:]["fourth_lvl_category_name"]):
            desc = str(desc)

            if v in lst_desc[x]:

                if desc.find(v) != -1:

                    lst_desc[x][v] += desc.count(v)

                elif t_c.find(v) != -1:

                    lst_desc[x][v] += t_c.count(v)

                elif f_c.find(v) != -1:

                    lst_desc[x][v] += f_c.count(v)

            else:
                lst_desc[x][v] = 1


print(lst_desc)
