rows = 5

for i in range(1, rows + 1):
    print('*' * i)



import matplotlib.pyplot as plt

# x and y values
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot the points
plt.plot(x, y)

# Add title and labels
plt.title('Simple Line Graph')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()



