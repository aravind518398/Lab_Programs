import matplotlib.pyplot as plt

division_A = [25, 20, 21,24,20,23,24,20,23,22,24,21,22,20]
division_B = [2,15,14,12,16,20,19,11,17,18,20,20,15,23,13]
division_C = [25,35,34,32,36,30,39,31,37,38,30,1,35,40,26]
plt.figure(figsize=(10,6))
plt.boxplot([division_A,division_B, division_C], tick_labels=['Class Division A', 'Class Division B', 'Class Division C'])
plt.ylabel("Marks")
plt.grid(True)
plt.title('Box Plot of Marks for Class Division A and B'.title())
plt.show()