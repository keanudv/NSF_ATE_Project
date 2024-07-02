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

'''
Note that you have to use double backslashes (\\) for the Pandas read_csv() function to work properly.
Also, you must have the data set in CSV format for the Pandas read_csv() function to work properly.
Also, know what character encoding the data set is using. For my project, the data set is in CSV UTF-8.
'''

df = pd.read_csv(file_location, encoding="UTF-8")

# View the data
df.head(10)
df.tail(10)

# Initial Exploratory Data Analysis (EDA)
df.shape #The shape function shows how many rows and columns the data set has.

df.info() #The info function shows the data type of each column.

df.describe() #The describe function shows summary statistics for numerical columns/quantitative data.

'''
Upon analyzing the data type, it seems that Python is not interpreting the Original Price and Price columns as quantitative data.
The reason is because the Original Price and Price column is formatted in Accouting ($ at the beginning).
Python interperts the $ as a String data type.
Therefore, to fix this issue, I have to adjust the formatting in Excel.
'''

# Once the formatting is adjusted, I can use the info function to see if Python interprets the Original Price and Price columns as quantitative data (int or float)
df.info()

# Now, I can get summary statistics on the Original Price and Price columns
df.describe()

# Check for missing values
df.isnull().sum()

'''
The Price column has 4 nulls.
Because I am going to do an analysis on the Price column, I have to dig deep into why the values are missing. 
'''

print(df[df["Price"].isnull()]) #This code shows the rows of the Price column that contain missing values.

'''
Upon analyzing the nulls in the price column, it shows that the Status of the propery listing is canceled.
This means that missing price values are associated with canceled property listings.
Therefore, we can drop the 4 rows in the Price column that have nulls.
'''

# Creates a new data frame (clean_df) that contains no nulls in the Price column.
clean_df = df.dropna(subset = ["Price"])
clean_df.isnull().sum()
