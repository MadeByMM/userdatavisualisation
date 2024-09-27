import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_table("u.user.txt", sep="|")

# Calculate the number of users in each occupation
occupation_counts = df['occupation'].value_counts()

# Calculate the percentage of each occupation
total_users = occupation_counts.sum()
occupation_percentages = (occupation_counts / total_users) * 100

# Group occupations with less than 3% into an "Other" category
threshold = 3
other_count = occupation_counts[occupation_percentages < threshold].sum()
filtered_occupations = occupation_counts[occupation_percentages >= threshold]
filtered_occupations['Other'] = other_count

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 10))  # Adjusted figure size
ax.pie(filtered_occupations, labels=filtered_occupations.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(filtered_occupations))))

# Customize the plot
ax.set_title('Occupation Distribution')

plt.tight_layout()
plt.show()