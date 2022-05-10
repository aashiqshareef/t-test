import numpy as np
import pandas as pd
df = pd.read_csv("/content/autoscout24-germany-dataset.csv")
pop_mean = df["hp"].mean()
print(pop_mean)
sample = df.head(20)
sample_mean = sample["hp"].mean()
print(sample_mean)
std_error = sample["hp"].std() / np.sqrt(len(sample))
print(std_error)
t = (sample_mean - pop_mean)/std_error
print(t)
