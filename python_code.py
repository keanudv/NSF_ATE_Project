'''
Name: Keanu Valencia
Date: 06/21/2024
'''

# Import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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
df.describe() #The describe() function shows summary statistics for numerical columns.

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

# Create a new data frame (clean_df) that contains no nulls in the Price column
clean_df = df.dropna(subset=["Price"])

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

# Create a new data frame (final_df) that contains only the needed columns using the clean data frame
final_df = clean_df[columns]

# Verify that the number of columns is equal to the number of selected columns (8)
final_df.shape

# Verify that there are no nulls in the new dataframe
final_df.isnull().sum()

# Creates a function for scatterplots that allow for code reusability
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

# Creates a function for barplots that allow for code reusability
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
First off, I want to see what was the cheapest and most expensive property that sold.
To do this, I will sort the Status column to include only sold properties. Then, I will use the idxmin() and idxmax() function.
'''

# Filter the Status column to include only sold properties
sold_properties = final_df[final_df["Status"]=="SOLD"]

# Print the cheapest property that sold
cheapest_property = sold_properties.loc[sold_properties["Price"].idxmin()]
print(cheapest_property)

# Print the most expensive property that sold
most_expensive_property = sold_properties.loc[sold_properties["Price"].idxmax()]
print(most_expensive_property)

'''
The cheapest property that sold was in Napili for $2,000.
The most expensive property that sold was a single family home in Wailea/Makena for 38.5 million!
Next, I want see which district and property type had the most sales.
To do this, I will group by District and Type. Then, I will use my barplot function.
'''

# Group by District and count the number of sold properties
district_group = sold_properties.groupby("District").size().reset_index(name="Number of Sales")

# Create the barplot to see which district had the most sales
barplot("District", "Number of Sales", district_group, "Number of Sales by District")

# Group by Type and count the number of sold properties
type_group = sold_properties.groupby("Type").size().reset_index(name="Number of Sales")

# Create the barplot to see which property type had the most sales
barplot("Type", "Number of Sales", type_group, "Number of Sales by Property Type")

'''
The district with the most sales is Kihei, more than 1,400 total sales.
The property type with the most sales is Condos, more than 2,600 total sales.
With this information, now I want to see how many of those Kihei sales were Condos.
'''

# Filter the sold properties to include only Condo properties that are located in Kihei
kihei_condos = sold_properties[(sold_properties["District"]=="Kihei") & (sold_properties["Type"]=="Condo")]

# Print the number of Kihei Condo sales
kihei_condo_count = kihei_condos.shape[0]
print(kihei_condo_count)

'''
Of the 1,400 properties that sold in Kihei, 1,049 of them were Condos.
Next, I want see which month had the most and least listings.
To do this, I need to make a copy of the data frame because we need to modify the List Date column's datatype to datetime format. Then, I will group by month and use my barplot function.
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

# Create the barplot to see which month had the most and least listings
barplot("Month", "Number of Listings", listings_per_month, "Number of Listings by Month")

'''
The month with the most listings is May, around 1,000 listings.
The month with the least amount of listings is August, around 500 listings.
Next, I want to see which month had the most and least sales.
To do this, I will make a copy of the sold_properties variable, group by month, then use my barplot function.
'''

# Filter the Status column to include only sold properties
sold_properties = final_df[final_df["Status"]=="SOLD"].copy()

# Group by Month and count the number of sold properties
month_group = sold_properties.groupby("Month").size().reset_index(name="Number of Sales")

# Create the barplot to see which month had the most and least sales
barplot("Month", "Number of Sales", month_group, "Number of Sales by Month")

'''
The month with the most sales is September, around 600 sales.
The month with the least amount of sales is April, around 300 sales.
Next, I want to see which district and property type had the most days on market.
To do this, I will group by District and Type, calculate the average days on market, then use my barplot function.
'''

# Group by District and calculate the average Days On Market
ave_days_on_market = final_df.groupby("District")["Days On Market"].mean().reset_index()

# Create the barplot to see which District had the most days on market
barplot("District", "Days On Market", ave_days_on_market, "Average Days on Market by District")

# Group by Type and calculate the average Days On Market
ave_days_on_market = final_df.groupby("Type")["Days On Market"].mean().reset_index()

# Create the barplot to see which property Type had the most days on market
barplot("Type", "Days On Market", ave_days_on_market, "Average Days on Market by Property Type")

'''
The district that had the highest days on market is Olowalu, around 240 days.
The property type that had the highest days on market is business, around 180 days.
Next, I want to see which district and property type is the most affordable.
To do this, I will group by District and Type, calculate the average price, then use my barplot function.
'''

# Group by District and calculate the average Price
ave_price_by_district = final_df.groupby("District")["Price"].mean().reset_index()

# Create the barplot to see which District is the most affordable
barplot("District", "Price", ave_price_by_district, "Average Price by District")

# Group by Type and calculate the average Price
ave_price_by_type = final_df.groupby("Type")["Price"].mean().reset_index()

# Create the barplot to see which property Type is the most affordable
barplot("Type", "Price", ave_price_by_type, "Average Price by Property Type")

'''
The most affordable district is Molokai.
The most affordable property type is:
  1. Attached Ohana.
  2. Commercial-Lease Land.
  3. Commercial-Lease Unit.
  4. Cottage.
  5. House.
  6. Other.
'''
