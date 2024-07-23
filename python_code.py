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

# See the first and last 5 rows of the data set
df.head()
df.tail()

# Exploratory data analysis (EDA)
df.shape #The shape function shows how many rows and columns the data set has.
df.info() #The info() function shows the data type of each column.
df.describe() #The describe() function shows summary statistics for numerical columns/quantitative data.

# Check for missing values
df.isnull().sum()

'''
Upon analyzing the missing values using the isnull().sum() function, it shows that the Price column has 4 missing values.
Because I am going to do an analysis on the Price column, I have to dig deep into why the values are missing.
'''

# Show the rows of the Price column that contain missing values
print(df[df["Price"].isnull()])

'''
Upon analyzing the nulls in the price column, it shows that the Status of the propery listing is canceled.
This means that missing price values are associated with canceled property listings.
Therefore, I can drop the 4 rows in the Price column that have nulls.
'''

# Creates a new data frame (clean_df) that contains no nulls in the Price column
clean_df = df.dropna(subset = ["Price"])

# Verify that there are no nulls in the Price column for the new data frame
clean_df.isnull().sum()

'''
For this project, I will only use the Status, Type, Original Price, Price, District, List Date, Price Date, and Days On Market variables.
Therefore, I must create a final data frame that contains only the needed columns.
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

# Creates a new data frame (final_df) that contains only the needed columns using the clean data frame
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
  x: The value for the x-axis.
  y: The value for the y-axis.
  d: The value for the data to plot.
  title: The value for the title of the graph.
  '''
  sns.scatterplot(x=x, y=y, data=d)
  plt.title(title, fontsize=20)
  plt.xlabel(x, fontsize=14)
  plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
  plt.xticks(rotation=75, ha="right")
  plt.ylabel(y, fontsize=14)
  plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
  plt.show()

# Creates a function for barplots that will make visualizations easier
def barplot(x, y, d, title):
  '''
  This function creates a barplot that shows the relationships between two variables.
  
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
The first questions I want to answer is which district and property type had the most sales.
'''

# Filter the Status column to include only sold properties
sold_properties = final_df[final_df["Status"]=="SOLD"]

# Group by District and count the number of sold properties
district_group = sold_properties.groupby("District").size().reset_index(name="Number of Sales")

# Create the barplot to see which district had the most sales
barplot("District", "Number of Sales", district_group, "Number of Sales by District")

# Group by Type and count the number of sold properties
type_group = sold_properties.groupby("Type").size().reset_index(name="Number of Sales")

# Create the barplot to see which property type had the most sales
barplot("Type", "Number of Sales", type_group, "Number of Sales by Property Type")

'''
The barplots show that the Kihei district (more than 1,400) and Condo property types (more than 2,600) had the most sales.
With this information, now I want to see how many of those Kihei sales were Condos.
'''

# Filter the sold properties to include only Condo properties that are located in Kihei
kihei_condos = sold_properties[(sold_properties["District"]=="Kihei") & (sold_properties["Type"]=="Condo")]

# Count the number of Kihei condo sales
kihei_condo_count = kihei_condos.shape[0]
print(kihei_condo_count)

'''
Of the 1,400+ properties that sold in Kihei, 1,049 of them were Condos.
The next question I want to answer is which month had the most and least listings.
'''

# Make a copy of the data frame
final_df = final_df.copy()

# Convert the List Date column to datetime format
final_df["List Date"] = pd.to_datetime(final_df["List Date"], errors="coerce")

# Verify that the List Date column is in datetime format
print(final_df["List Date"].dtype)

# Get the month from the List Date column
final_df.loc[:, "Month"] = final_df["List Date"].dt.month

# Group by Month and count the number of listings
listings_per_month = final_df.groupby("Month").size().reset_index(name="Number of Listings")

# Creates the barplot to see which month had the most and least listings
barplot("Month", "Number of Listings", listings_per_month, "Number of Listings by Month")

'''
Upon analyzing the barplot, it shows that May had the most listings (around 1,000) while August had the least listings (less than 600).
The next question I want to answer is which month had the most and least sales.
'''

# Filter the Status column to include only sold properties
sold_properties = final_df[final_df["Status"]=="SOLD"].copy()

# Group by Month and count the number of sold properties
month_group = sold_properties.groupby("Month").size().reset_index(name="Number of Sales")

# Creates the barplot to see which month had the most and least sales
barplot("Month", "Number of Sales", month_group, "Number of Sales by Month")

'''
Upon analyzing the barplot, it shows that September had the most sales (more than 600) while April had the least sales (less than 300).
The next question I want to answer is which district and property type has the most days on market.
'''
