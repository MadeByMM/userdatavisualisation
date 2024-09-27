import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_table("u.user.txt", sep="|")

# Extract the age column
ages = df['age']

# Plot the data as a histogram
fig, ax = plt.subplots(figsize=(10, 6))  # Adjusted figure size
counts, bins, patches = ax.hist(ages, bins=20, color='skyblue', edgecolor='black')

# Customize the plot
ax.set_xlabel('Age')
ax.set_ylabel('Number of Users')
ax.set_title('Age Distribution')

# Add the number of each age to each bar
for count, bin_edge in zip(counts, bins):
    if count > 0:  # Only annotate bars with counts
        ax.text(bin_edge + (bins[1] - bins[0]) / 2, count, str(int(count)), ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()