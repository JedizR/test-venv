import matplotlib.pyplot as plt

# Data for the graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the plot
plt.plot(x, y, label='y = 2x', color='blue', marker='o')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Graph')

# Add a legend
plt.legend()

# Show the plot
plt.show()
