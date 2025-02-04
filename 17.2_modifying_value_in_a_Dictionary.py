alian_0 = {'color': 'green'}
alian_0['color'] = 'yellow'

alian_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"original position: {alian_0['x_position']}")

if alian_0["speed"] == 'slow':
    x_increment = 1
elif alian_0["speed"] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alian_0['x_position'] = alian_0['x_position'] + x_increment

print(f"New Position : {alian_0['x_position']}")