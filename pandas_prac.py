import pandas as pd
import numpy as np

# # 1 empty series
# empty_ser = pd.Series()
# print(empty_ser)

#2 series
# data = np.array([1,2,3,4,5,6])
# ser = pd.Series(data)
# print(ser)

#3 series with index
# data = np.array([1,2,3,4,5])
# ser = pd.Series(data, index=['a','b','c','d','e'])
# print(ser)

#4 series with array
# list1 = [1,2,3,4,5]
# data = pd.Series(list1)
# print(data)

#5 series by dictionary
# dic = {'A':1,'B':2,'C':3}
# ser = pd.Series(dic)
# print(ser)

#6 series by scalar value
# data = pd.Series(10, index=[1,2,3,4])
# print(data)


                    # data fram


#1 empty data frame
# data = pd.DataFrame()
# print(data)

#2 data frame by using series
# data = {'one':pd.Series([10,20,30,40,50], index=['a','b','c','d','e']),
#         'two': pd.Series([100,200,300] , index=['a','b','c'])}
# print(data)

#3 dataframe by list
# data = pd.Series([10,20,30])
# df = pd.DataFrame(data)
# print(df)

# 4 data frame by dic
# dic = {'name':['Shamsher','Uvaiz','Sohail','Sahil'],
#        'age': [19,20,30,43],
#        'city':['Jaipur','Ajmer','Kota','Tonk']}

# data = pd.DataFrame(dic)

# print(data)

# 5 multiindex concept
# index = pd.MultiIndex.from_product([['A','B'],['a','b']], names=['group','subgroup'])
# data = {"values": [1,2,3,4]}
# df = pd.DataFrame(data, index=index)
# print(df)

#6 convert dataframe into array

# data = {
#     'A':[1,2,3],
#     'B':[4,5,6],
#     'C':[7,8,9]
# }
# df = pd.DataFrame(data)
# print('dataframe ', df)

# numpy_array = df.values
# print(numpy_array)


#7 
# data = {
#     'A':[1,2,10,None],
#     'B':[4,None, 5, None],
#     'C':[7,8,9,90]
# }

# df = pd.DataFrame(data)
# print(df)

# missing_val = df.isna()
# print('missing values' , missing_val)

# # handle the missing values
# df_filled = df.fillna(df.mean(), inplace=True)
# print('fill missing values ' , df_filled)

# print('Original dataframe', df)

#6 interpolate missing values

# df_interpolate = df.interpolate()
# print("interpolate values ", df_interpolate)


#8 filter data
# data = {
#     'A':[1,2,3,4,5],
#     'B':[6,7,8,8,9]
# }

# df = pd.DataFrame(data)
# filter_data = df[df['A']>3]
# print('filter data greater than 3',filter_data)
# filter_data2 = df[df['B']>7]
# print('filter data greater than 7',filter_data2)


# 10 grouop by
# data = {
#     'Category':['A','B','A','B','A','B'],
#     'Values' : [34,46,35,76,87,98]
# }

# df = pd.DataFrame(data)
# group_sum = df.groupby('Category')['Values'].sum()
# print(group_sum)

# 11 chaning
# data = {
#     'A':[1,2,3,4,5],
#     'B':[6,7,8,9,10]
# }
# df = pd.DataFrame(data)
# print(df)

# result = df[df['A']>2].sort_values(by ='B',ascending=False).reset_index(drop=True)
# print(result)

# 12 duplicate rows
# data = {
#     'A':[1,2,3,1,2],
#     'B':[4,5,6,4,5],
# }

# df = pd.DataFrame(data)
# print(df)

# remove_dupli = df.drop_duplicates()
# print(remove_dupli)


# data = {
#     'A':[1,2,1,2],
#     'B':[4,5,4,5],
#     'C':[10,20,30,40]
# }

# df = pd.DataFrame(data)
# agg_group = df.groupby(['A','B']).agg({'C':'sum'}).reset_index()
# print(agg_group)


# loc and iloc
data = {
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
    }
df = pd.DataFrame(data, index=['X','Y','Z'])
print(df)

print(df.loc['X':'Y','A':'B'])
print(df.loc['Y':'Y','A':'C'])