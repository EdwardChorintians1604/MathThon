import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file with relative path
df = pd.read_csv("Front_End/static/chart/timss_2023.csv")

# Filter to only country data for clarity
df_countries = df[df['Category'] == 'Country']

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(14, 8))
sns.barplot(x="Country", y="Average_Score", data=df_countries, ax=ax, palette="viridis")
ax.set_title("TIMSS 2023 Average Scores by Country")
ax.set_xlabel("Country")
ax.set_ylabel("Average Score")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("Front_End/static/chart/timss_2023_chart.png")
plt.close()
