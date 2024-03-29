import matplotlib.pyplot as plt

x_values_first_five = list(range(1, 6))
x_values_first_5000 = list(range(1, 5001))

y_values_first_five = [x**3 for x in x_values_first_five]
y_values_first_5000 = [x**3 for x in x_values_first_5000]

plt.scatter(x_values_first_five, y_values_first_five, c='blue', edgecolor='none', s=40)

plt.title("Cubes for First Five Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 6, 0, 150])

plt.savefig('cubes_first_five_plot.png', bbox_inches='tight')

plt.clf()

plt.scatter(x_values_first_5000, y_values_first_5000, c=y_values_first_5000, cmap=plt.cm.Blues,
            edgecolor='none', s=40)

plt.title("Cubes of First 500 Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 5100, 0, 1300000000])

plt.savefig('cubes_first_5000_plot.png', bbox_inches='tight')
plt.show()


