import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_table("u.user.txt", sep="|")

# Calculate the number of males and females in each occupation
gender_counts = df.pivot_table(values='user_id', index='occupation', columns='gender', aggfunc='count', fill_value=0)

# Determine the gender dominance for each occupation
gender_counts['dominance'] = gender_counts.apply(lambda row: 'Male' if row['M'] > row['F'] else 'Female', axis=1)
gender_counts['dominance_ratio'] = gender_counts.apply(lambda row: row['M'] / (row['M'] + row['F']) if row['M'] > row['F'] else row['F'] / (row['M'] + row['F']), axis=1)

# Sort by dominance ratio
gender_counts = gender_counts.sort_values(by='dominance_ratio', ascending=False)

# Plot the occupations with the highest gender dominance
top_n = 10  # Number of top occupations to display
top_gender_counts = gender_counts.head(top_n)

ax = top_gender_counts[['M', 'F']].plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Top 10 Most Gender Dominated Occupations')
plt.xlabel('Occupation')
plt.ylabel('Number of Respondants')
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.tight_layout()

# Adding labels to each bar
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.annotate(f'{int(height)}', (x + width / 2, y + height / 2), ha='center', va='center', color='white', fontsize=10)

plt.show()