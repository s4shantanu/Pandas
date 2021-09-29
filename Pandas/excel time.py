import numpy as np
import pandas as pd
import time

start = time.time()
df= pd.read_csv('ooo.csv')
print(df)
end = time.time()
print(end - start)