import pandas as pd
import plotly.express as px
import os
from datetime import datetime
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('data.csv')

# 1. Top 10 states by population 2020
df['population_2020'] = df['population 2020 census'].str.replace(',', '').astype(float)
pop_fig = px.bar(
    df.nlargest(10, 'population_2020'),
    x='state',
    y='population_2020',
    title='Top 10 States by Population (2020)',
    color='region'
)

# 2. Average poverty rate by region
poverty_by_region = df.groupby('region')['% in poverty'].mean().reset_index()
poverty_fig = px.bar(
    poverty_by_region,
    x='region',
    y='% in poverty',
    title='Average Poverty Rate by Region',
    color='region'
)

# 3. Top 10 states by education level
edu_fig = px.bar(
    df.nlargest(10, '% bachelors or higher'),
    x='state',
    y='% bachelors or higher',
    title='Top 10 States by Percentage of Bachelor\'s Degree or Higher',
    color='region'
)

# 4. Regional Population Distribution Pie Chart
region_population = df.groupby('region')['population_2020'].sum().reset_index()
pie_fig = px.pie(
    region_population,
    values='population_2020',
    names='region',
    title='Population Distribution by Region (2020)',
    color='region',
    hole=0.3  # Creates a donut chart effect
)

# 5. histogram of median household income
income_hist = px.histogram(
    df,
    x='median household income ($US)',
    nbins=20,
    color='region',
    title='Distribution of Median Household Income by Region',
    labels={'median household income ($US)': 'Median Household Income ($)'},
    opacity=0.7
)

# 6. Box Plot - Income Distribution by Region
box_fig = px.box(
    df,
    x='region',
    y='median household income ($US)',
    color='region',
    title='Income Distribution by Region',
    points='outliers'
)

# 7. Linear Regression - Education vs Income
reg_fig = px.scatter(
    df,
    x='% bachelors or higher',
    y='median household income ($US)',
    trendline="ols",
    color='region',
    title='Education Level vs Median Household Income',
    labels={
        '% bachelors or higher': 'Bachelor\'s Degree or Higher (%)',
        'median household income ($US)': 'Median Household Income ($)'
    }
)

# 8. Scatter Plot - Population vs Poverty
scatter_fig = px.scatter(
    df,
    x='population_2020',
    y='% in poverty',
    color='region',
    size='population_2020',
    hover_data=['state'],
    title='Population vs Poverty Rate by State',
    labels={
        'population_2020': 'Population (2020)',
        '% in poverty': 'Poverty Rate (%)'
    }
)

# Create summary statistics table
numerical_cols = ['population_2020', 
                 '% bachelors or higher',
                 '% high school or higher',
                 '%home owners',
                 'median household income ($US)',
                 'per capita income ($US)',
                 '% in poverty',
                 'mean commute time (minutes)']

# Calculate statistics
stats_dict = {
    'Mean': df[numerical_cols].mean(),
    'Median': df[numerical_cols].median(),
    'Mode': df[numerical_cols].mode().iloc[0],
    'Std Dev': df[numerical_cols].std(),
    'Min': df[numerical_cols].min(),
    'Max': df[numerical_cols].max()
}

# Create DataFrame
stats_df = pd.DataFrame(stats_dict).round(2)
stats_df.index.name = 'Metric'

# Create table figure
table_fig = go.Figure(data=[go.Table(
    header=dict(
        values=['Metric'] + list(stats_df.columns),
        fill_color='paleturquoise',
        align='left'
    ),
    cells=dict(
        values=[stats_df.index] + [stats_df[col] for col in stats_df.columns],
        fill_color='lavender',
        align='left'
    )
)])

# Update layout
table_fig.update_layout(
    title='Summary Statistics by Category',
    width=1200,
    height=400
)



# Save population chart
pop_fig.write_image(f"population_top10_.png")

# Save poverty chart
poverty_fig.write_image(f"poverty_by_region_.png")

# Save education chart
edu_fig.write_image(f"education_top10_.png")

# Save pie chart
pie_fig.write_image(f"region_population_pie_.png")

# Save histogram
income_hist.write_image(f"income_distribution_.png")

# Save new charts
box_fig.write_image(f"income_boxplot_.png")
reg_fig.write_image(f"education_income_regression_.png")
scatter_fig.write_image(f"population_poverty_scatter_.png")

# Save table
table_fig.write_image(f"summary_statistics_.png")

# Still show interactive plots in browser
pop_fig.show()
poverty_fig.show()
edu_fig.show()
pie_fig.show()

# Display interactive plot
income_hist.show()
box_fig.show()
reg_fig.show()
scatter_fig.show()

# Display table
table_fig.show()