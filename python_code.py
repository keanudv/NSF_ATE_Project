'''
Name: Keanu Valencia
Date: 06/21/2024
'''

# Imports the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data set into Python
file_location = "C:\\Users\\keanu\\OneDrive\\Desktop\\Hotsheet_spreadsheet_version.csv"
df = pd.read_csv(file_location, encoding="UTF-8")

'''
Note that you have to use double backslashes (\\) for the Pandas read_csv() function to work properly.
Also, you must have the data set in CSV format for the Pandas read_csv() function to work properly.
Also, know what character encoding the data set is using. For my project, the data set is in CSV UTF-8.
'''

# View the data
df.head(10)
df.tail(10)

# Exploratory Data Analysis (EDA)
df.shape #The shape function shows how many rows and columns the data set has.
df.info() #The info() function shows the data type of each column.
df.describe() #The describe() function shows summary statistics for numerical columns/quantitative data.

'''
Upon analyzing the data types using the info() function, it shows that Python is not interpreting the Original Price and Price columns as quantitative data.
The reason is because the Original Price and Price column is formatted in Accouting ($) on Excel.
Python interperts the $ as a String data type.
To fix this issue, I have to adjust the formatting in Excel.
Once the formatting is fixed, I can use the info() function to see if Python now interprerts the Original Price and Price columns as quantitative data.
'''

df.info() #Python should interpret the Original Price and Price columns as quantitative data (int or float).
df.describe() #Get summary statistics on the Original Price and Price columns.

# Check for missing values
df.isnull().sum()

'''
Upon analyzing the missing values using the isnull().sum() function, it shows that the Price column has 4 missing values.
Because I am going to do an analysis on the Price column, I have to dig deep into why the values are missing.
'''

print(df[df["Price"].isnull()]) #This code shows the rows of the Price column that contain missing values.

'''
Upon analyzing the nulls in the price column, it shows that the Status of the propery listing is canceled.
This means that missing price values are associated with canceled property listings.
Therefore, we can drop the 4 rows in the Price column that have nulls.
'''

# Creates a new data frame (clean_df) that contains no nulls in the Price column
clean_df = df.dropna(subset = ["Price"])
clean_df.isnull().sum() #The Price column should have 0 nulls.

# Selects only the needed columns
columns = [
  "Status",
  "Type",
  "Original Price",
  "Price",
  "List Date",
  "Price Date",
  "Days On Market"
]

# Creates a new data frame (new_df) that contains only the needed columns using the clean data frame.
new_df = clean_df[columns]
new_df.shape #Verify that the number of columns is equal to the number of selected columns.
new_df.isnull().sum() #Verify that there are no nulls in the new dataframe.
