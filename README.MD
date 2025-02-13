## About this Dataset
- Source, Structure, Relevance

### By Matus Bencek

### Where did the dataset come from?
This dataset was gathered by the CORGIS Dataset Project.

### Why do you think the dataset was gathered in the first place? 
The dataset was created to analyze U.S. population trends, including education levels, gender distribution, age demographics, and poverty rates. Key metrics include population changes, percentage of college graduates, proportion of females, age groups, and poverty indicators.

### Who is the intended audience , how might that impact the sample?
This dataset was created for students to explore population trends and correlations in the United States it seems that this has not impacted the sample as it was original collected during the census and there is all data present.

### How Many Rows and Columns Does the Dataset Have?  

- **Rows:** 51 (each representing a U.S. state, including D.C. and territories)  
- **Columns:** 22 (a mix of categorical and quantitative data)  

| **Column Name**                     | **Type**         | **Description** |
|--------------------------------------|-----------------|----------------|
| `state`                              | Categorical     | Name of the state |
| `region`                             | Categorical     | Geographic region of the state |
| `population 2010`                    | Quantitative   | Population count in 2010 |
| `population 2020 census`             | Quantitative   | Population count in 2020 |
| `population trend`                   | Categorical     | Trend classification (e.g., increasing, decreasing) |
| `% bachelors or higher`              | Quantitative   | Percentage of people with a bachelor's degree or higher |
| `% high school or higher`            | Quantitative   | Percentage of people with at least a high school diploma |
| `% home owners`                      | Quantitative   | Percentage of home ownership |
| `number of households`               | Quantitative   | Total number of households |
| `number of housing units`            | Quantitative   | Total housing units available |
| `land area (sq miles)`               | Quantitative   | Land area of the state in square miles |
| `% non-English at home`              | Quantitative   | Percentage of people speaking a non-English language at home |
| `mean commute time (minutes)`        | Quantitative   | Average commute time in minutes |
| `median household income ($US)`      | Quantitative   | Median household income in U.S. dollars |
| `per capita income ($US)`            | Quantitative   | Per capita income in U.S. dollars |
| `veterans`                           | Quantitative   | Number of veterans in the state |
| `% female`                           | Quantitative   | Percentage of the population that is female |
| `% older than 65`                    | Quantitative   | Percentage of the population older than 65 |
| `% under 18`                         | Quantitative   | Percentage of the population under 18 |
| `% under 5`                          | Quantitative   | Percentage of the population under 5 |
| `% in poverty`                       | Quantitative   | Percentage of people living in poverty |
| `poverty rate`                       | Categorical     | Classification of poverty levels |

This dataset provides a mix of demographic, economic, and geographic information useful for analyzing population trends and socio-economic conditions across U.S. states.

### A visual exploration of the columns in my dataset

#### Bar Charts

**Name**: Top 10 states by population 2020  
([image](population_top10_.png))

**Is this display useful / interesting?** : Yes  
**Interpretation**: California, Texas, and Florida dominate the population rankings, collectively accounting for about 28% of the US population. The data shows a significant concentration in these three states, with California having nearly 40 million residents. Notably, the top 10 states represent diverse regions, though the West and Southeast regions are most prominent.

**Code:**
```python
df['population_2020'] = df['population 2020 census'].str.replace(',', '').astype(float)
pop_fig = px.bar(
    df.nlargest(10, 'population_2020'),
    x='state',
    y='population_2020',
    title='Top 10 States by Population (2020)',
    color='region'
)
```

**Name**: Average poverty rate by region  
([image](poverty_by_region_.png))

**Is this display useful / interesting?** : Yes  
**Interpretation**: The Southeast region shows the highest average poverty rate (around 18%), while the Northeast has the lowest (approximately 11%). This regional disparity highlights significant economic inequality across US regions, with the Southeast facing greater economic challenges. The pattern suggests a need for targeted economic development in higher-poverty regions.

**Code:**
```python
poverty_by_region = df.groupby('region')['% in poverty'].mean().reset_index()
poverty_fig = px.bar(
    poverty_by_region,
    x='region',
    y='% in poverty',
    title='Average Poverty Rate by Region',
    color='region'
)
```

**Name**: Top 10 states by education level  
([image](education_top10_.png))

**Is this display useful / interesting?** : Yes  
**Interpretation**: The District of Columbia leads with over 52% of residents holding bachelor's degrees or higher, significantly above other states. Northeast states dominate the top rankings, suggesting stronger higher education systems or greater job markets for educated workers in this region. There's a clear regional pattern in educational attainment.

**Code:**
```python
edu_fig = px.bar(
    df.nlargest(10, '% bachelors or higher'),
    x='state',
    y='% bachelors or higher',
    title='Top 10 States by Percentage of Bachelor\'s Degree or Higher',
    color='region'
)
```

#### Pie Chart

**Name**: Regional Population Distribution  
([image](region_population_pie_png))

**Is this display useful / interesting?** : Yes  
**Interpretation**: The population distribution shows significant variation across regions. The South and West regions contain the largest share of the US population, while the Northeast has a smaller share despite its high population density. This distribution reflects historical migration patterns and economic opportunities across regions.

**Code:**
```python
region_population = df.groupby('region')['population_2020'].sum().reset_index()
pie_fig = px.pie(
    region_population,
    values='population_2020',
    names='region',
    title='Population Distribution by Region (2020)',
    color='region',
    hole=0.3  # Creates a donut chart effect
)
```

#### Histogram

**Name**: histogram of median household income  
([image](income_distribution_.png))

**Is this display useful / interesting?** : Yes  
**Interpretation**: The distribution of median household incomes shows right-skewed pattern, with most states clustering between $40,000-$60,000. Northeast states tend to have higher median incomes, while Southeast states generally fall in lower income brackets. The spread indicates significant economic inequality across states.

**Code:**
```python
income_hist = px.histogram(
    df,
    x='median household income ($US)',
    nbins=20,
    color='region',
    title='Distribution of Median Household Income by Region',
    labels={'median household income ($US)': 'Median Household Income ($)'},
    opacity=0.7
)
```

#### Box Plot

**Name**: Income Distribution by Region  
([image](income_boxplot_.png))

**Is this display useful / interesting?** : Yes  
**Interpretation**: The Northeast region shows both the highest median income and largest variation in income levels. The Southeast consistently shows lower median incomes with less variation. This visualization effectively demonstrates both regional income disparities and within-region income variation.

**Code:**
```python
box_fig = px.box(
    df,
    x='region',
    y='median household income ($US)',
    color='region',
    title='Income Distribution by Region',
    points='outliers'
)
```

#### Linear Regression

**Name**: Education vs Income  
([image](education_income_regression_.png))

**Is this display useful / interesting?** : Yes  
**Interpretation**: There is a strong positive correlation between education levels and median household income. For every percentage point increase in bachelor's degree holders, there's a corresponding increase in median household income. This relationship holds across regions, though with some regional variations.

**Code:**
```python
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
```

#### Scatter Plot

**Name**: Population vs Poverty  
([image](population_poverty_scatter_.png))

**Is this display useful / interesting?** : Yes
**Interpretation**: There's no clear correlation between state population size and poverty rates, suggesting that poverty is independent of state size. States of similar population can have widely different poverty rates, indicating that other factors (like education, industry mix, and policy) may be more important in determining poverty levels.

**Code:**
```python
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
```

### Measures of Center and Spread

([image](summary_statistics_.png))

**Code:**
```python
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
```