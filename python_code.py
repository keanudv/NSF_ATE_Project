'''
Name: Keanu Valencia
Date: 06/21/2024
'''

# Import the libraries
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

# See the first and last 5 rows of the data set
df.head()
df.tail()

# Exploratory Data Analysis (EDA)
df.shape #The shape function shows how many rows and columns the data set has.
df.info() #The info() function shows the data type of each column.
df.describe() #The describe() function shows summary statistics for numerical columns/quantitative data.

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

# Verify that there are no nulls in the Price column for the new data frame
clean_df.isnull().sum()

'''
For this project, I will only use the Status, Type, Original Price, Price, List Date, Price Date, and Days On Market variables.
Therefore, we must create a final data frame that contains only the needed columns.
'''

# Select only the needed columns
columns = [
  "Status",
  "Type",
  "Original Price",
  "Price",
  "List Date",
  "Price Date",
  "Days On Market"
]

# Creates a new data frame (final_df) that contains only the needed columns using the clean data frame.
final_df = clean_df[columns]

# Verify that the number of columns is equal to the number of selected columns (7)
final_df.shape

# Verify that there are no nulls in the new dataframe
final_df.isnull().sum()

