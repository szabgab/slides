import pandas
data = pandas.read_csv('../../data/ifmetrics.csv', na_values=['(null)'])
data.fillna(0, inplace=True)
# , parse_dates=True )
# print(type(data))  # pandas.core.frame.DataFrame
print(data.columns)  # Index([ ... ],  dtype='object', length=135)

#print(data['Utilization In - Threshold Exception Rate'].head(3))

for col in ['Utilization In - Threshold Exception Rate', 'Overall Exception Rate']:
    dt = data[col]
    print(dt[dt != 0])


#print(data.head(1))
#print(data.get_values())