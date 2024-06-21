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
