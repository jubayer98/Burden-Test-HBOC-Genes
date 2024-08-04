# import important libraries
import pandas as pd
import matplotlib.pyplot as plt

# define the hboc_gene file path
file_path = 'HBOC_Gene_Data.csv'

# read the defined file_path
df = pd.read_csv(file_path, delimiter=';')

### ADDITIONA INFORMATION --- REF1 ###
# in-case the specific columns needs to typecast and change to numeric
# convert odds_ratio, ci_low, ci_high to numeric
# comment out the following lines of code if you need it
#df['odds_ratio'] = df['odds_ratio'].str.replace(',', '.').astype(float)
#df['ci_low'] = df['ci_low'].str.replace(',', '.').astype(float)
#df['ci_high'] = df['ci_high'].str.replace(',', '.').astype(float)

# convert gene to string
#df['gene'] = df['gene'].astype(str)

### BURDEN TEST PLOTTING - PRIORITIZE ONE SPECIFIC GENE (STK11) ###
# identify the index of the gene with the significantly higher odds ratio
high_value_index = df['odds_ratio'].idxmax()

# split data into two groups: high-value gene and other genes
high_value_gene = df.iloc[[high_value_index]]
other_genes = df.drop(index=high_value_index)

# create a figure with two subplots
fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(14, 6))

# plot for the high-value gene
ax1.plot([high_value_gene['ci_low'].values[0], high_value_gene['ci_high'].values[0]], [0, 0], color='grey', lw=1)
ax1.scatter(high_value_gene['odds_ratio'], 0, marker='^', color='black', zorder=3)
ax1.axvline(x=1, color='black', linestyle='--', lw=1)  # add vertical line at log odds ratio = 1
ax1.set_yticks([0])
ax1.set_yticklabels([high_value_gene['gene'].values[0]])
ax1.set_xlabel('Odds Ratio')
ax1.set_title('STK11') # change the gene name, in-case your's one is different

# plot for other genes
# Y-axis labels
ax2.set_yticks(range(len(other_genes)))
ax2.set_yticklabels(other_genes['gene'])

# plot horizontal lines for CI
for i in range(len(other_genes)): 
  ax2.plot([other_genes['ci_low'].iloc[i], other_genes['ci_high'].iloc[i]], [i, i], color='grey', lw=1)

# plot triangles for odds ratio
ax2.scatter(other_genes['odds_ratio'], range(len(other_genes)), marker='^', color='black', zorder=3)

# add vertical line at log odds ratio = 1
ax2.axvline(x=1, color='black', linestyle='--', lw=1)

# set labels
ax2.set_xlabel('Odds Ratio')
ax2.set_title('All affected HBOC genes') # change the label, in-case your's one is different

# save the plot as a file
plt.savefig('figure-1.png')
# display the plot
plt.show()

### BURDEN TEST PLOTTING - FOR ALL GENES TOGETHER ###
# plotting the forest plot
fig, ax = plt.subplots(figsize=(10, 6))

# Y-axis labels
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['gene'])

# plot horizontal lines for CI
for i in range(len(df)): 
  ax.plot([df['ci_low'][i], df['ci_high'][i]], [i, i], color='grey', lw=1)

# plot triangles for odds ratio
ax.scatter(df['odds_ratio'], range(len(df)), marker='^', color='black', zorder=3)

# add vertical line at odds ratio 1 for reference
ax.axvline(x=1, color='black', linestyle='--')

# set labels
ax.set_xlabel('Odds Ratio')
ax.set_title('A Set of HBOC Genes') # change the label, in-case your's one is different

# save the plot as a file
plt.savefig('figure-2.png')
# display the plot
plt.show()
