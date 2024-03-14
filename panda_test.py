import pandas as pd
import numpy as np

df = pd.read_csv('credit_scoring_sample.csv')  # to load a csv file

#print(df.shape) # to print the dimensions of the dataset like (45063, 8)

#print(df.info()) # to print all the info about the dataset like no. of cols & rows, their datatype, null & not null values....

#pd.set_option('display.max_columns', 8) # to set options like max_cols, max_rows.....

#print(df.head()) # to print first 5 rows

#print(df.tail()) # to print last 5 rows

#print(df.head(10)) # to print first n rows

#df = pd.DataFrame(test_dictionary) # to load a dictionary to the dataframe

#print(df['age']) / print(df.age)  # to print all the values of a column

# print(df.iloc[0])  # to print the row based on integer location or the index

# print(df.iloc[[0, 1]])  # to print multiple rows based on integer location or the index

# print(df.iloc[0, 1]) # to print value of 0th row and 1st column

# print(df.iloc[[0, 1], 2]) # to print value of 0th, 1st row and 2nd column

# print(df.loc[0, 'age']) # to print suing location of row and columns

# print(df.loc[0:10, 'age':'DebtRatio']) # we can use slicing as well

# print(df.columns) # to print all the column names

# print(df.DebtRatio.value_counts()) #to print the count of each unique values in the column

#print(df.index)   #to show the row index

# df.set_index('age') # to temporarily set the index as age

# df.set_index('age', inplace=True) # to make change to actual DF

# df.reset_index(inplace=True) # to reset the indexes

# df = pd.read_csv('credit_scoring_sample.csv', index_col='age')  # to load a csv file in which age column is the index

# df.sort_index()  # to sort the index in alphabetical order

# df.sort_index(ascending=False) # to sort in descending order

#print(df['age'] == 41)  # prints True if values are same or else false

# filt = df['age'] == 41
# print(df[filt])           # to print rows which contains those values

# print(df.loc[filt, 'DebtRatio']) # to filter rows and get only the columns

# filt = (df['age'] == 41) & (df['MonthlyIncome'] == 3000)  # to add a 'AND' condition

# filt = (df['age'] == 41) & (df['MonthlyIncome'] == 3000)  # to add a 'OR' condition

# print(df.loc[~filt]) # to negate the filter conditon, works as a NOT

# age_group = [41, 31, 38]
# filt = df['age'].isin(age_group)
# print(df[filt])                   # to create a list and filter based on it

#filt = df['ProgramName'].str.contains('Python', na=False)  # to create a filter with string contains option and setting na=False for ignoring NaN values

#df.columns = [x.upper() for x in df.columns]  # list comprehension to make all the column names in upper case

#df.columns = df.columns.str.replace('Number', 'No.')  # string replace for updating column names

#df.renames(columns={'age' : 'Age', 'MonthlyIncome' : 'Monthly_Income'})  # to change multiple column names at once

#df.loc[2] = ['val1', 'val2', .....]  # to update all the valeus of a row

# df.loc[2, 'age'] = [32]  # to update values based on rows and cols

# df['age'] = df['age'].str.upper()   # to make all the values in that column in upper case

#-----------------------------------------------------------------------------------------------#

#apply
# def func(age):
#     pass
# df['age'] = df['age'].apply(func)   # to apply function that call
# print(df['age'].apply(func))

#df['email'] = df['email'].apply(lambda x: x.lower()

#print(df.apply(len))  #to find number of values in each column 

#print(df.apply(len, axis='coulmns'))  #to find number of values in each rows

#print(df.apply(pd.Series.min))   # to find min of each columns

#applymap - to apply a function and create map
#df.applymap(str.lower)

#map
#df['first'].map({'Jane' : 'John, "Chris": "Carter"})  #it will replace these values and make other values as NaN

#replace
#df['first'].map({'Jane' : 'John, "Chris": "Carter"})  #it will replace these values and keep other values as is

#-----------------------------------------------------------------------------------------------#

#df['name'] = df['first'] + ' ' + df['last']  # to create and join 2 columns

#df[['first', 'last']] = df['name'].str.split(' ', expand=True) # to split 1 coulmn into 2

#df.drop(columns=['age', 'NumberOfDependents'], inplace=True)

#df.append({'age' : 31, 'DebtRatio' : 1}, ignore_index=True) # to add new row with values

#df = df.append(df2, ignore_index=True)  # to append 2 dataframes

# df.drop(index=4)  # to drop a row based on index

#df.drop(index=df[df['age']==41].index)  # to drop using index & filter

#filt = df['age']==41
#df.drop(index=df[filt].index)   # to drop using index & filter

#df.sort_values(by='age')  # to sort values based on column name

#df.sort_values(by='age', ascending=False)  # to sort values based on column name in descending order

#df.sort_values(by=['age', 'DebtRatio'])  # to sort values based on multiple column name

#df.sort_values(by=['age', 'DebtRatio'], ascending=[True, False])  # to sort multiple cols in asc or desc

#df.sort_index()

# print(df['age'].nlargest(10))  # to print the n largest values (just the values and not the rows)

#print(df.nlargest(10, 'age'))  # to print the n largest rows

#df['age'].median()  #median of a particular column

#df.median()  # median of all integers

#print(df.describe())  # gives details like mean, std, min .... for all cols

#df['age'].value_counts()  #count of each values

#df['age'].value_count(normalize=True) #percentage of each value

#group_age = df.groupby(['age'])
# print(group_age.get_group([41]))    # to group and filter based on column and value
# print(group_age['DebtRatio'].value_counts())    # to group and filter based on 2 column and value
# print(group_age['DebtRatio'].value_counts().loc[41])    # to group and filter based on 2 column and a age value
#print(group_age['DebtRatio'].agg(['mean', 'median']))   # to filter based on aggregated function (multiple functions)
#group_age['DebtRatio'].apply(lambda x:x.str.contains('string').sum())

# python_df = pd.concat(['group_age', 'group_DebtRatio'], axis='columns') # to concat dataframes on column level

#df.dropna()   # drops rows with NaN & None values

#df.dropna(axis='index')  # to drop rows

#df.dropna(axis='columns')  # to drop cols

#df.dropna(axis='index', how='any')  # to drop rows when any value is missing

#df.dropna(axis='index', how='all')  # to drop rows when all values are missing

#df.dropna(axis='index', how='any', subset=['age'])  # to drop rows when any value is missing in 'age' cols

#df.replace('NA', np.nan, inplace=True) # to replace any custom None value with NaN

#df.isna()  #to print values which NaN in a boolean table

#df.fillna('MISSING')  # to replace all the NaN values with 'Missing' as the value

#df.dtypes  # to show cols datatypes 

#df['age'] = df['age'].astype(int)  # to convert the datatype of a column

#na_vals = ['NA', 'MISSING']
#df = pd.read_csv('credit_scoring_sample.csv', na_values=na_vals)  # to load a csv file and convert custom none values as NaN values

#df['age'].unique()  #to print unique values in the column

#df['date'] = pd.to_datetime(df['date'], format='%Y....')  # converts str to datetime

#df.loc[0, 'date'].day_name()  # day name of the date (fri, mon, sun...)

#d_parser = lambda x: pd.datetime.strptime(x, '%Y....')
#df = pd.read_csv('credit_scoring_sample.csv', parse_dates=['date'], date_parser=d_parser) # to load data based on the date format

#df['date'].dt.day_name()  # to run day name on whole col

#filt = (df['date'] >= pd.to_datetime('2019-01-01')) & (df['date'] < pd.to_datetime('2020-01-01')) #to add filter in dates

# df.set_index('date')
# df['2019']              #to slice dates
# df['2020-10': '2021:01]

#df['date'].resample('D')   #to resample data ith Day, 1Day, 1week

#df.to_csv('path')   # to write dataframe to csv

