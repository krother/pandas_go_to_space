g = df.groupby('species')

# standard aggregation functions
g.mean()
g.max()
g.min()
g.sum()
g.count()
g.std()
g.median()
g.quantile(0.9)
g.describe()

# Aggregation with selecting columns
g['body_mass_g'].describe()

# Aggregation with a list of function names
g.agg(['count', 'mean', 'std'])

# function name with a label
g.agg([('Total', 'sum')])

# custom aggregation function with parameter
def sum_greater(dataframe, threshold):
    for column in dataframe.columns:
        return dataframe[dataframe[column] > threshold].sum()
    
g.agg(sum_greater, threshold=200)
