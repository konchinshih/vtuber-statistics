import pandas as pd
import seaborn as sns
from matplotlib import pyplot

data = pd.read_csv("result.csv")

individual = data.loc[data['isOffice'] == 0]
office = data.loc[data['isOffice'] == 1]

print(individual['fan'])
print(office['fan'])

print(list(individual['fan']))
pyplot.hist(list(individual['fan']))
pyplot.show()
