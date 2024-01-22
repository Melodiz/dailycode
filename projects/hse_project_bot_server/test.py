import matplotlib.pyplot as plt

# Data
x = range(1, 11)
y = [5, 7, 3, 8, 4, 6, 2, 9, 5, 10]

# Create bar chart
plt.bar(x, y)

# Attach legend to the bars using numbers
for i in range(10):
    plt.text(x[i], y[i] + 0.5, str(i+1), ha='center')

# Show the plot
plt.show()
