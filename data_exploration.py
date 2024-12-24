import pandas as pd

#load the dataset
data = pd.read_csv('tested.csv')

#Display the first few rows of the dataset
print(data.head())

#Check the shape of the dataset
print("Shape of the dataset:", data.shape)

#Check data types and missing values
print(data.info())

#Fill missing values with the mean(for numerica columns)
data.fillna(data.mean(), inplace=True)

#Display the first few rows of the dataset after filling missing values
print(data.head())

#Check for duplicate rows
data.drop_duplicates(inplace=True)

#Summary statistics
print(data.describe())