import matplotlib.pyplot as plt

# Points and splits
points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2), (6,5)]
splits = [
    {'type': 'vline', 'val': 6, 'color': 'red', 'label': 'x=6'},
    {'type': 'hline', 'val': 4, 'xlim': (0,6), 'color': 'green', 'label': 'y=4 (x<6)'},
    {'type': 'hline', 'val': 2, 'xlim': (6,10), 'color': 'purple', 'label': 'y=2 (x>6)'}
]

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.set_title('KD-Tree Splits')
ax.grid(True)

# Plot points
x, y = zip(*points)
ax.scatter(x, y, color='blue', zorder=5, label='Points')

# Draw splits
for split in splits:
    if split['type'] == 'vline':
        ax.axvline(split['val'], color=split['color'], linestyle='--', label=split['label'])
    elif split['type'] == 'hline':
        ax.hlines(split['val'], xmin=split['xlim'][0], xmax=split['xlim'][1], 
                  colors=split['color'], linestyle='--', label=split['label'])

ax.legend()
plt.show()