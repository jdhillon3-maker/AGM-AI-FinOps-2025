import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV
df = pd.read_csv('agm-cost-anon.csv')
df['UsageStartDate'] = pd.to_datetime(df['UsageStartDate'])

# Daily cost by service
daily = df.groupby(['UsageStartDate', 'ServiceCode'])['BlendedCost'].sum().reset_index()
pivot = daily.pivot(index='UsageStartDate', columns='ServiceCode', values='BlendedCost').fillna(0)

# Plot
plt.figure(figsize=(12, 6))
sns.heatmap(pivot.T, cmap="Reds", cbar_kws={'label': 'Daily Cost (£)'})
plt.title("AGM Daily Cloud Cost Heat-Map (Anonymised)")
plt.xlabel("Date")
plt.ylabel("Service")
plt.tight_layout()
plt.savefig("artefacts/finance/cost-heatmap.png", dpi=300)
print("Heat-map saved to artefacts/finance/cost-heatmap.png")
