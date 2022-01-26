import pandas as pd 
import math as math

data = pd.read_excel('./data.xlsx', '5')
values = pd.Series(data['b'])
print(values.count())

#print value on pos 5 and range from 6 to 25
print(values[5], values[6:25])

#print min and max values from set
print(values.min(), values.max())

# print sorted (asc) values
print(values.sort_values())

#print mean value and all values above it
mean = values.mean()
print(mean)
print(values[lambda x: x > mean])

#print intervals
m = math.ceil(math.sqrt(values.count()))
max = values.max()
min = values.min()
step = (max - min)/m

for i in range(m):
    max = min + step
    print('{}-{}: {}'.format(min, max, values[values.between(min, max)].count()))

    min = max 

