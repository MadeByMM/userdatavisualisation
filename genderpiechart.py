import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_table("u.user.txt", sep="|")

# Calculate the number of women and men
gender_counts = df['gender'].value_counts()

# Plot the data as a pie chart
fig, ax = plt.subplots(figsize=(8, 8))  # Adjusted figure size
wedges, texts, autotexts = ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#ff9999'])

# Customize the text properties
plt.setp(autotexts, size=12, weight="bold")
ax.set_title('Distribution of Women and Men')

plt.tight_layout()
plt.show()