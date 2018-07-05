from apyori import apriori
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('data/apriori_data.csv', header = None)
records = []
for i in range(0, 7):
    records.append([str(dataset.values[i,j]) for j in range(0,6)])

from apyori import apriori
rules = apriori(records, min_support=0.003, min_confidence = 0.2, min_lift=3, min_length = 2)

results = list(rules)

print(results)



