import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("Berkeley.csv") #Reading the dataset in a dataframe using Pandas


head = df.head(10)

#print head

#print df

fare_not_survived = df["Gender"][df["Admit"] == "Admitted"]

print fare_not_survived