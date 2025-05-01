import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pycountry_convert as pc
df = pd.read_csv("Data/owid-energy-data.csv")
df = df[["country", "iso_code", "year", "renewables_share_energy"]]

df = df[df["year"] >= 2000]
df = df.dropna(subset=["renewables_share_energy", "iso_code"])

global_trend = df.groupby("year")["renewables_share_energy"].mean().reset_index()

def map_country_to_continent(iso_code):
    try:
        country_alpha2 = pc.country_alpha3_to_country_alpha2(iso_code)
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except:
        return None

df["continent"] = df["iso_code"].apply(map_country_to_continent)
df = df.dropna(subset=["continent"])

continent_trend = df.groupby(["continent", "year"])["renewables_share_energy"].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=continent_trend, x="year", y="renewables_share_energy", hue="continent", marker="o")
plt.title("Renewable Energy Share Trends by Continent")
plt.xlabel("Year")
plt.ylabel("Renewables Share of Total Energy (%)")
plt.grid(True)
plt.legend(title="Continent")
plt.tight_layout()
plt.show()

# Global trend plot
plt.figure(figsize=(10, 5))
plt.plot(global_trend["year"], global_trend["renewables_share_energy"], marker='o', color='black')
plt.title("Global Average Renewable Energy Share")
plt.xlabel("Year")
plt.ylabel("Renewables Share of Total Energy (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
