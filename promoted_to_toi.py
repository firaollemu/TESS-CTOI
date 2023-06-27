import pandas as pd
import csv

exofop = 'exofop_edited.csv'

exofop_df = pd.read_csv(exofop)


# Variables to store each candidate in three categories 1. PC 2. FP 3. further review
promoted_to_toi = []


# Number of rows in the exofop file
rows = len(exofop_df)

# Append the column titles to the promoted to TOI list 
column_title_for_promoted_to_toi_list = ['TIC ID', 'CTOI', 'Transit Epoch (BJD)', 'Period (days)', 'Planet Radius (R_Earth)', 'Duration (hours)', 'Depth (mmag)', 'CTOI Category']
promoted_to_toi.append(column_title_for_promoted_to_toi_list)


# Loop through each row 
for i in range(rows):
    if pd.notnull(exofop_df.loc[i, 'Promoted to TOI']):
        row_values = [exofop_df.loc[i, 'TIC ID'], exofop_df.loc[i, 'CTOI'], exofop_df.loc[i, 'Transit Epoch (BJD)'], exofop_df.loc[i, 'Period (days)'], exofop_df.loc[i, 'Planet Radius (R_Earth)'], exofop_df.loc[i, 'Duration (hours)'], exofop_df.loc[i, 'Depth (mmag)']]
        row_values.append('Promoted to TOI')
        promoted_to_toi.append(row_values)
 

# Use the CSV module to save the list of list containing the parameters for those promoted to TOIs as a CSV file

# Define the path to save the CSV file
new_tois = 'new_tois.csv'

# Write the promoted_to_toi data to the new_tois csv file
with open(new_tois, 'w', newline='') as toi_file:
    new_toi_data = csv.writer(toi_file)
    new_toi_data.writerows(promoted_to_toi)


print('Success')
# print(promoted_to_toi)
# print(len(promoted_to_toi))


# Reading specific columns
#print(exofop_df.loc[1:70, ['Promoted to TOI']])