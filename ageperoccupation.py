import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table("u.user.txt", sep="|")

df_pivot = df.pivot_table(values=('age'), columns=("occupation"), fill_value=0, aggfunc='mean')
ax = df_pivot.plot(kind='bar', figsize=(10, 6), legend=False, zorder=3)
plt.title('Average Age per Occupation')
plt.xlabel('Occupation')
plt.ylabel('Average Age')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()

for y in range(0, int(df_pivot.values.max()) + 10, 10):
    plt.axhline(y=y, color='gray', linestyle='--', linewidth=0.5, zorder=1)

for p, occupation in zip(ax.patches, df_pivot.columns):
    ax.annotate(occupation, (p.get_x() + p.get_width() / 2., p.get_height() / 2),
                ha='center', va='center', color='white', fontsize=10, rotation=90)
    
plt.show()