import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
correlation_matrix = tips.corr(numeric_only=True)

plt.figure(figsize=(10,6))
sns.heatmap(correlation_matrix, annot=True, cmap="magma", linewidths=3)
plt.title("Heatmap of correlation matrix for tips dataset".title())
plt.show()