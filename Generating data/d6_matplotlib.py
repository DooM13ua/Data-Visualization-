import matplotlib.pyplot as plt
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Visualize the results.
plt.hist(results, bins=range(1, die.num_sides + 2), align='left', edgecolor='black', linewidth=1.2)
plt.xlabel("Result")
plt.ylabel("Frequency of Result")
plt.title(f'Results of rolling a D{die.num_sides} {roll_num} times')
plt.xticks(range(1, die.num_sides + 1))
plt.grid(True)
# plt.savefig('d6_matplotlib.png')
plt.show()