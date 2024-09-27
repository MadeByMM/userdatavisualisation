import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_table("u.user.txt", sep="|")

# Read the zip code to state mapping
zip_to_state = pd.read_csv("zip_code_database.csv") 

# Ensure both zip_code columns are of the same type (string)
df['zip_code'] = df['zip_code'].astype(str)
zip_to_state['zip'] = zip_to_state['zip'].astype(str)

# Merge the user data with the zip code to state mapping
df = df.merge(zip_to_state, left_on='zip_code', right_on='zip', how='left')

# Group the data by state
state_counts = df['state'].value_counts().reset_index()
state_counts.columns = ['state', 'count']

# Create a bar chart
fig, ax = plt.subplots(figsize=(14, 8))  # Adjusted figure size
sns.barplot(x='state', y='count', data=state_counts, ax=ax, palette='viridis')

# Customize the plot
ax.set_xlabel('State')
ax.set_ylabel('Number of Users')
ax.set_title('Number of Users by State')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

plt.tight_layout()
plt.show()