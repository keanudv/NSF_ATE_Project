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
  "District",
  "List Date",
  "Price Date",
  "Days On Market"
]

# Creates a new data frame (final_df) that contains only the needed columns using the clean data frame.
final_df = clean_df[columns]

# Verify that the number of columns is equal to the number of selected columns (8)
final_df.shape

# Verify that there are no nulls in the new dataframe
final_df.isnull().sum()

# Creates a function for scatterplots that will make data visualizations easier
import matplotlib.ticker as ticker
def scatterplot(x, y, d, title):
  '''
  This function creates a scatterplot that shows the relationship between two variables.

  Parameters:
  x: The x parameter is the name for the first variable.
  y: The y parameter is the name for the second variable.
  d: The d parameter is the name for the data frame.
  title: The title parameter is the name for the title of the scatter plot.
  '''
  sns.scatterplot(x=x, y=y, data=d)
  plt.title(title, fontsize=20)
  plt.xlabel(x, fontsize=14)
  plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
  plt.xticks(rotation=45, ha="right")
  plt.ylabel(y, fontsize=14)
  plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
  plt.show()

# Creates a function for boxplots that will make visualizations easier
def boxplot(x, y, d, title):
  '''
  This function creates a scatterplot that shows the relationship between two variables.

  Parameters:
  Uses the same parameters as the scatterplot function.
  '''
  sns.boxplot(x=x, y=y, data=d)
  plt.title(title, fontsize=20)
  plt.xlabel(x, fontsize=14)
  plt.xticks(rotation=75, ha="right", fontsize=8)
  plt.subplots_adjust(bottom=0.3)
  plt.ylabel(y, fontsize=14)
  plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
  plt.show()

# Creates a function for bargraphs that will make visualizations easier
def barplot(x, y, d, title):
  '''
  This function creates a scatterplot that shows the relationships between two variables.
  
  Parameters:
  Uses the same parameters as the scatterplot function.
  '''
  sns.barplot(x=x, y=y, data=d)
  plt.title(title, fontsize=20)
  plt.xlabel(x, fontsize=14)
  plt.xticks(rotation=75, ha="right", fontsize=8)
  plt.subplots_adjust(bottom=0.3)
  plt.ylabel(y, fontsize=14)
  plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
  plt.show()

'''
The first question I want to answer is which district had the most sales. To do this, I will create a barplot using my barplot function.
'''

# Filter the Status column to include only sold properties
sold_properties = final_df[final_df["Status"]=="SOLD"]

# Group by district and count the number of sold properties
district_group = sold_properties.groupby("District").size().reset_index(name="Number of Properties Sold")

# Create the barplot
barplot("District", "Number of Properties Sold", district_group, "Number of Sales by District")

'''
Upon analyzing the barplot, it shows that Kihei had the most sales (1,400).
'''
