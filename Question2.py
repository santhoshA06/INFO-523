# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Data/owid-energy-data.csv")

# Dictionary to map countries to continents (expand as needed)
country_to_continent = {
    'USA': 'North America', 'Canada': 'North America', 'Mexico': 'North America',
    'Brazil': 'South America', 'Argentina': 'South America', 'Colombia': 'South America',
    'Germany': 'Europe', 'France': 'Europe', 'United Kingdom': 'Europe',
    'China': 'Asia', 'India': 'Asia', 'Japan': 'Asia',
    'Australia': 'Australia', 'South Africa': 'Africa', 'Nigeria': 'Africa',
    'ASEAN (Ember)': 'Asia',  # Add missing countries if needed
}

# Function to map country to continent
def get_continent(country):
    return country_to_continent.get(country, 'Unknown')  # Default to 'Unknown' if country not found

# Apply the continent mapping to the 'country' column
df['continent'] = df['country'].apply(get_continent)

# Filter relevant columns for analysis
df_filtered = df[['country', 'continent', 'year', 'gdp', 'solar_share_energy', 'wind_share_energy', 'biofuel_consumption', 'hydro_consumption']]

# Drop rows with missing values in GDP and energy share columns
df_filtered = df_filtered.dropna(subset=['gdp', 'solar_share_energy', 'wind_share_energy', 'biofuel_consumption', 'hydro_consumption'])

# Group data by continent
continent_grouped = df_filtered.groupby('continent')

# Create scatter plots for each continent to analyze the relationship between GDP and renewable energy adoption

# Plot for Solar Energy Share
plt.figure(figsize=(14, 10))
for continent in continent_grouped:
    continent_name, continent_data = continent
    plt.scatter(continent_data['gdp'], continent_data['solar_share_energy'], label=f'{continent_name} - Solar', alpha=0.6)

plt.title('GDP vs Solar Energy Share by Continent')
plt.xlabel('GDP')
plt.ylabel('Solar Energy Share')
plt.legend()
plt.show()

# Plot for Wind Energy Share (Separate figure)
plt.figure(figsize=(14, 10))
for continent in continent_grouped:
    continent_name, continent_data = continent
    plt.scatter(continent_data['gdp'], continent_data['wind_share_energy'], label=f'{continent_name} - Wind', alpha=0.6)

plt.title('GDP vs Wind Energy Share by Continent')
plt.xlabel('GDP')
plt.ylabel('Wind Energy Share')
plt.legend()
plt.show()

# Plot for Biofuel Consumption (Separate figure)
plt.figure(figsize=(14, 10))
for continent in continent_grouped:
    continent_name, continent_data = continent
    plt.scatter(continent_data['gdp'], continent_data['biofuel_consumption'], label=f'{continent_name} - Biofuel', alpha=0.6)

plt.title('GDP vs Biofuel Consumption by Continent')
plt.xlabel('GDP')
plt.ylabel('Biofuel Consumption')
plt.legend()
plt.show()

# Plot for Hydropower Consumption (Separate figure)
plt.figure(figsize=(14, 10))
for continent in continent_grouped:
    continent_name, continent_data = continent
    plt.scatter(continent_data['gdp'], continent_data['hydro_consumption'], label=f'{continent_name} - Hydropower', alpha=0.6)

plt.title('GDP vs Hydropower Consumption by Continent')
plt.xlabel('GDP')
plt.ylabel('Hydropower Consumption')
plt.legend()
plt.show()
