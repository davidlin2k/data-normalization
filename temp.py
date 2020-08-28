# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:12:35 2020

@author: david
"""

import math 

import pandas as pd

#simple feature scaling
df = pd.DataFrame({
      "num" : [10, 12, 23, 23, 16, 23, 21, 16]
      })

df["num"] = df["num"] / df["num"].max()

print(df)


#min-max
df_1 = pd.DataFrame({
      "num" : [10, 12, 23, 23, 16, 23, 21, 16]
      })

df_1["num"] = (df_1["num"] - df_1["num"].min()) / (df_1["num"].max() - df_1["num"].min())

print(df)


#z-score
def std(data):
    upper = 0
    for x in data:
        upper = upper + (x - (sum(data) / len(data)))**2
    lower = len(data) - 1
    return math.sqrt(upper/lower)

df_2 = pd.DataFrame({
      "num" : [10, 12, 23, 23, 16, 23, 21, 16]
      })

df_2["num"] = (df_2["num"] / df_2["num"].mean()) / std(df_2["num"])

#or
#df_2["num"] = (df_2["num"] / df_2["num"].mean()) / df_2["num"].std()))

print(df_2)
