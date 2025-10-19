UNICORN COMPANIES (CSV) / STARTUP COMPANIES WITH A VALUE OF +$1 BILLION 

# Import libraries and packages
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# Load data from the csv file into a DataFrame and save in a variable
companies = pd.read_csv("Unicorn_Companies.csv")

# Display the first 10 rows of the data
companies.head(10)

# How large the dataset is / Number of Values in dataset
companies.size

# Shape of the dataset (Row, Col)
companies.shape

# Get information - Note Col Date Joined Dtype = object
companies.info()

# Get descriptive statistics
companies.describe()

# Use pd.to_datetime() to convert Date Joined column to datetime 
companies["Date Joined"] = pd.to_datetime(companies["Date Joined"])

# Use .info() to confirm/verify that the update actually took place
companies.info()

# Use .dt.year to extract year component from Date Joined column
# Add the result as a new column named Year Joined to the DataFrame
companies["Year Joined"] = companies["Date Joined"].dt.year

# Use .head() to confirm that the new column did get added
companies.head()

# Sample the data
companies_sample = companies.sample(n = 50, random_state = 42)

# Prepare data for plotting

# Create new `years_till_unicorn` column (Number of years to reach unicorn status)
companies_sample["years_till_unicorn"] = companies_sample["Year Joined"] - companies_sample["Year Founded"]

# Group the data by `Industry`. For each industry, get the max value in the `years_till_unicorn` column.
grouped = (companies_sample[["Industry", "years_till_unicorn"]]
           .groupby("Industry")
           .max()
           .sort_values(by="years_till_unicorn"))
grouped

# Create Bar Chart
plt.bar(grouped.index, grouped["years_till_unicorn"])

plt.title("Maximum years taken by Company to become unicorn per industry")

# Set x-axis label
plt.xlabel("Industry")

# Set y-axis label
plt.ylabel("Maximum number of years")

# Rotate labels on the x-axis as a way to avoid overlap in the positions of the text  
plt.xticks(rotation=45, horizontalalignment='right')

# Display the Bar Chart
plt.show()
