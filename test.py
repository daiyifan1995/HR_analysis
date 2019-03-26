import pandas as pd

content = ['T', 'F'] * 10

data = pd.DataFrame(content, columns=['Y'])
print(data)
data.loc[data['Y'] == 'T'] = 1
data.loc[data['Y'] == 'F'] = 0

print(data)