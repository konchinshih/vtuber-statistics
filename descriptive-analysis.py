import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv("result.csv")

data['viewRate'] = (data['view'] / data['video']) / data['fan']

ind = data.loc[data['isOffice'] == 0]
office = data.loc[data['isOffice'] == 1]

#   Question 1
sns.histplot(data=ind, x='fan', bins=100)
plt.savefig("q1-ind-fan-hist.png"); plt.show()

sns.histplot(data=office, x='fan', bins=100)
plt.savefig("q1-office-fan-hist.png"); plt.show()

sns.boxplot(data=[ind['fan'], office['fan']], orient='h')
plt.savefig("q1-fan-box.png"); plt.show()


#   Question 2
ind = ind.sort_values(
    by=['viewRate']
).iloc[
    len(ind.index)*5//100:len(ind.index)*95//100
]
office = office.sort_values(
    by=['viewRate']
).iloc[
    len(office.index)*5//100:len(office.index)*95//100
]

sns.histplot(data=ind, x='viewRate', bins=100)
plt.savefig("q2-ind-viewRate-hist.png"); plt.show()

sns.histplot(data=office, x='viewRate', bins=100)
plt.savefig("q2-office-viewRate-hist.png"); plt.show()

sns.boxplot(data=[ind['viewRate'], office['viewRate']], orient='h')
plt.savefig("q2-viewRate-box.png"); plt.show()


#   Question 3
firstHalf = data.iloc[lambda x: x.index < len(data.index)//2]
firstHalf = firstHalf.sort_values(
    by=['viewRate']
).iloc[
    len(firstHalf.index)*5//100:len(firstHalf.index)*95//100
]
secondHalf = data.iloc[lambda x: x.index >= len(data.index)//2]
secondHalf = secondHalf.sort_values(
    by=['viewRate']
).iloc[
    len(secondHalf.index)*5//100:len(secondHalf.index)*95//100
]

sns.histplot(data=firstHalf, x='viewRate', bins=100)
plt.savefig("q3-firstHalf-viewRate-hist.png"); plt.show()

sns.histplot(data=secondHalf, x='viewRate', bins=100)
plt.savefig("q3-secondHalf-viewRate-hist.png"); plt.show()

sns.boxplot(
    data=[firstHalf['viewRate'], secondHalf['viewRate']], 
    orient='h'
)
plt.savefig("q3-viewRate-box.png"); plt.show()
