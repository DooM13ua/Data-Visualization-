import pygal
from random_walk import RandomWalk

# Create a random walk instance.
rw = RandomWalk()

# Fill the walk.
rw.fill_walk()

# Visualize using pygal.

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Random Walk'
xy_chart.add('Random Walk', [(rw.x_values[i], rw.y_values[i]) for i in range(rw.num_points)])
xy_chart.render_to_file('random_walk_visual.svg')