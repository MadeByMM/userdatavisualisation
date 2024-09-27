import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_table("u.user.txt", sep="|")

# Group the data by age and gender
grouped = df.groupby(['age', 'gender']).size().unstack(fill_value=0)

# Define the colors
colors = {
	'M': '#1f77b4',  # Blue
	'F': '#ff7f0e'   # Orange
}

# Create a line chart
fig, ax = plt.subplots(figsize=(14, 10))  # Adjusted figure size
grouped.plot(kind='line', ax=ax, color=[colors[col] for col in grouped.columns])

# Customize the plot
ax.set_xlabel('Age')
ax.set_ylabel('Number of Users')
ax.set_title('Age Distribution by Gender')
ax.legend(title='Gender')

plt.tight_layout()
plt.show()