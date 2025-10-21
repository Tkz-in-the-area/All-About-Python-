Lightning Strikes EDA Project

# Import libraries and packages
import pandas as pd
import numpy as np
import seaborn as sns
import datetime
from matplotlib import pyplot as plt

# Read in the 2018 data.
df = pd.read_csv('eda_structuring_with_python_dataset1.csv') 
df.head()

# Convert the `date` column to datetime.
df['date'] = pd.to_datetime(df['date']) 

# Returns (Rows, Col)
df.shape

# Check for duplicates - No dupicates found
df.drop_duplicates().shape

# Sort by number of strikes in descending order.
df.sort_values(by='number_of_strikes', ascending=False).head(10)

# Identify the locations that appear most in the dataset.
df.center_point_geom.value_counts()

# Identify the top 20 locations with most days of lightning.
df.center_point_geom.value_counts()[:20].rename_axis('unique_values').reset_index(name='counts').style.background_gradient()

# Create two new columns.
df['week'] = df.date.dt.isocalendar().week
df['weekday'] = df.date.dt.day_name()
df.head()

# Calculate the mean count of lightning strikes for each weekday.
df[['weekday','number_of_strikes']].groupby(['weekday']).mean()

# Define order of days for the plot.
weekday_order = ['Monday','Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','Sunday']

# Create boxplots of strike counts for each day of week.
g = sns.boxplot(data=df, 
            x='weekday',
            y='number_of_strikes', 
            order=weekday_order, 
            showfliers=False);
# Adjust layout spacing
plt.tight_layout(pad=1.0)
# Set Title
g.set_title('Lightning distribution per weekday (2018)');

# Import 2016–2017 data
df_2 = pd.read_csv('eda_structuring_with_python_dataset2.csv')
df_2.head()

# Convert `date` column to datetime.
df_2['date'] = pd.to_datetime(df_2['date'])

# Create a new dataframe combining 2016–2017 data with 2018 data.
union_df = pd.concat([df.drop(['weekday','week'],axis=1), df_2], ignore_index=True)
union_df.head()

# Add 3 new columns.
union_df['year'] = union_df.date.dt.year
union_df['month'] = union_df.date.dt.month
union_df['month_text'] = union_df.date.dt.month_name()
union_df.head()

# Calculate total number of strikes per year
union_df[['year','number_of_strikes']].groupby(['year']).sum()

# Calculate total lightning strikes for each month of each year.
lightning_by_month = union_df.groupby(['month_text','year']).agg(
    number_of_strikes = pd.NamedAgg(column='number_of_strikes',aggfunc=sum)).reset_index()

lightning_by_month.head()

# Calculate total lightning strikes for each year.
lightning_by_year = union_df.groupby(['year']).agg(
  year_strikes = pd.NamedAgg(column='number_of_strikes',aggfunc=sum)
).reset_index()

lightning_by_year.head()

# Combine `lightning_by_month` and `lightning_by_year` dataframes into single dataframe.
percentage_lightning = lightning_by_month.merge(lightning_by_year,on='year')
percentage_lightning.head()

# Create new `percentage_lightning_per_month` column.
percentage_lightning['percentage_lightning_per_month'] = (percentage_lightning.number_of_strikes/
                                                          percentage_lightning.year_strikes * 100.0)
percentage_lightning.head()

plt.figure(figsize=(10,6));

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Bar Chart Visualization ------------------------------------------------------
sns.barplot(
    data = percentage_lightning,
    x = 'month_text',
    y = 'percentage_lightning_per_month',
    hue = 'year',
    order = month_order );
plt.xlabel("Month");
plt.ylabel("% of lightning strikes");
# Adjust layout spacing
plt.tight_layout(pad=1.0),
plt.title("% of lightning strikes each Month (2016-2018)");

# Heat Map Visualization -------------------------------------------------------
# Ensure months are ordered correctly
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Pivot the data to create a matrix for the heatmap
heatmap_data = percentage_lightning.pivot_table(
    index='year',
    columns='month_text',
    values='percentage_lightning_per_month'
)

# Reorder the columns to match month_order
heatmap_data = heatmap_data[month_order]

# Plot the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", cbar_kws={'label': '% of lightning strikes'})
plt.xlabel("Month")
plt.ylabel("Year")
plt.title("% of lightning strikes each Month (2016–2018)")
plt.tight_layout(pad=1.0)
plt.show()

# Bubble Chart Visualization -----------------------------------------------------
# Ensure months are ordered correctly
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Convert month_text to categorical with correct order
percentage_lightning['month_text'] = pd.Categorical(
    percentage_lightning['month_text'], categories=month_order, ordered=True
)

# Sort data for consistent plotting
percentage_lightning = percentage_lightning.sort_values(['year', 'month_text'])

# Create numeric x-axis positions for months
month_to_num = {month: i for i, month in enumerate(month_order)}
percentage_lightning['month_num'] = percentage_lightning['month_text'].map(month_to_num)

# Plot bubble chart
plt.figure(figsize=(10, 6))
scatter = plt.scatter(
    x=percentage_lightning['month_num'],
    y=percentage_lightning['year'],
    s=percentage_lightning['percentage_lightning_per_month'] * 20,  # scale bubble size
    c=percentage_lightning['percentage_lightning_per_month'],
    cmap='YlGnBu',
    alpha=0.6,
    edgecolors='w',
    linewidth=0.5
)

# Customize axes
plt.xticks(ticks=range(12), labels=month_order, rotation=45)
plt.xlabel("Month")
plt.ylabel("Year")
plt.title("% of lightning strikes each Month (2016–2018)")

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('% of lightning strikes')

plt.tight_layout(pad=1.0)
plt.show()

# Line Chart Visualization -----------------------------------------------------
# Ensure months are ordered correctly
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Convert month_text to categorical with correct order
percentage_lightning['month_text'] = pd.Categorical(
    percentage_lightning['month_text'], categories=month_order, ordered=True
)

# Sort data for consistent line plotting
percentage_lightning = percentage_lightning.sort_values(['year', 'month_text'])

# Plot line chart
plt.figure(figsize=(10, 6))
sns.lineplot(
    data=percentage_lightning,
    x='month_text',
    y='percentage_lightning_per_month',
    hue='year',
    marker='o'
)

# Customize axes and layout
plt.xlabel("Month")
plt.ylabel("% of lightning strikes")
plt.title("% of lightning strikes each Month (2016–2018)")
plt.xticks(rotation=45)
plt.tight_layout(pad=1.0)
plt.show()