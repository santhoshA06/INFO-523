import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Data\owid-energy-data.csv")

features = [
    'fossil_fuel_consumption',
    'hydro_consumption',
    'solar_consumption',
    'wind_consumption',
    'biofuel_consumption',
    'other_renewable_consumption',
    'renewables_consumption',
    'low_carbon_consumption'
]

X = df[features].dropna()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

df.loc[X.index, 'cluster'] = clusters

centers = pd.DataFrame(
    scaler.inverse_transform(kmeans.cluster_centers_),
    columns=features
)
print("Cluster Centers:")
print(centers, "\n")
print("Counts per cluster:")
print(df['cluster'].value_counts(), "\n")
print("Sample countries in each cluster:")
for cl in sorted(df['cluster'].dropna().unique()):
    sample = df[df['cluster'] == cl]['country'].dropna().unique()[:5]
    print(f"Cluster {int(cl)}:", ", ".join(sample))