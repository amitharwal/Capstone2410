import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(data)

# Save the dataset to a CSV for ease of our use
dataset_path = "/mnt/data/Climate_Change_Analysis.csv"
df.to_csv(dataset_path, index=False)

# Plot 1: CO2 Emissions over time
plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["Global_CO2_Emissions"], marker="o")
plt.title("Global CO2 Emissions Over Time")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (Million Metric Tons)")
plt.grid()
plt.savefig("/mnt/data/CO2_Emissions_Over_Time.png")

# Plot 2: Temperature Anomalies over time
plt.figure(figsize=(10, 6))
plt.plot(df["Year"], df["Temperature_Anomalies"], marker="s", color="orange")
plt.title("Global Temperature Anomalies Over Time")
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.grid()
plt.savefig("/mnt/data/Temperature_Anomalies_Over_Time.png")

# Plot 3: Renewable Energy Share over time
plt.figure(figsize=(10, 6))
plt.bar(df["Year"], df["Renewable_Energy_Share"], color="green")
plt.title("Renewable Energy Share Over Time")
plt.xlabel("Year")
plt.ylabel("Renewable Energy Share (%)")
plt.grid()
plt.savefig("/mnt/data/Renewable_Energy_Share_Over_Time.png")

# Plot 4: Population vs CO2 Emissions
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["Population"], y=df["Global_CO2_Emissions"], size=df["Year"], legend=False, sizes=(100, 500))
plt.title("Population vs Global CO2 Emissions")
plt.xlabel("Population (Billion)")
plt.ylabel("CO2 Emissions (Million Metric Tons)")
plt.grid()
plt.savefig("/mnt/data/Population_vs_CO2_Emissions.png")

# Plot 5: Correlation Heatmap
plt.figure(figsize=(10, 6))
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Key Metrics")
plt.savefig("/mnt/data/Correlation_Heatmap.png")
