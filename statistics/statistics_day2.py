import pandas as pd
import numpy as np

#skewness
#right skewed
data = pd.Series([
    10, 11, 12, 13, 14, 50
])

print("Mean:", data.mean())
print("Median:", data.median())
print("Skewness:", data.skew())


#left skewed
data = pd.Series([
    10, 46, 47, 48, 49, 50
])

print("Mean:", data.mean())
print("Median:", data.median())
print("Skewness:", data.skew())


