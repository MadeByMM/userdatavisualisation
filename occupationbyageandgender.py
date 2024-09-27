import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_table("u.user.txt", sep="|")

# Group the data by occupation, age, and gender
grouped = df.groupby(['occupation', 'age', 'gender']).size().reset_index(name='count')

# Create a scatter plot
fig, ax = plt.subplots(figsize=(14, 10))  # Adjusted figure size

# Define colors for genders
colors = {'M': 'blue', 'F': 'red'}

# Plot the data
for gender in grouped['gender'].unique():
    subset = grouped[grouped['gender'] == gender]
    ax.scatter(subset['age'], subset['occupation'], s=subset['count']*10, alpha=0.5, c=colors[gender], label=gender)

# Customize the plot
ax.set_xlabel('Age')
ax.set_ylabel('Occupation')
ax.set_title('Occupation by Age and Gender')
ax.legend(title='Gender')

plt.tight_layout()
plt.show()