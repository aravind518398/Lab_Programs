import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="year", columns="month", values="passengers")

plt.figure(figsize=(10,6))
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="magma", linewidths=0.5)
plt.xlabel("Month")
plt.ylabel("Year")
plt.title("headmap of airline passengers by month and year".title())
plt.show()
