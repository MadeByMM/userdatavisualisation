import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Read the data
df = pd.read_table("u.user.txt", sep="|")

# Group the data by occupation and gender
grouped = df.groupby(['occupation', 'gender']).size().unstack(fill_value=0)

# Flatten the data for plotting
occupations = grouped.index
genders = grouped.columns
data = grouped.values

# Prepare data for treemap
labels = []
sizes = []
colors = []

for i, occupation in enumerate(occupations):
    for j, gender in enumerate(genders):
        size = data[i][j]
        if size > 0:  # Only include non-zero sizes
            labels.append(f'{occupation} ({gender})')
            sizes.append(size)
            colors.append(plt.cm.Paired(j))

# Create a treemap
fig, ax = plt.subplots(figsize=(14, 10))  # Adjusted figure size
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8, ax=ax)

# Customize the plot
ax.set_title('Treemap of Occupation Distribution by Gender')
ax.axis('off')

plt.tight_layout()
plt.show()