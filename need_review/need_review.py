from xml.sax import parseString
import pandas as pd
import csv
import numpy as np
from collections import Counter

review_sheet = 'CTOI_review_sheet.csv'
exofop = 'exofop_edited.csv'

fp = 'CTOI_Review_FP.csv'
toi = 'new_tois.csv'

review_sheet_df = pd.read_csv(review_sheet)
exofop_df = pd.read_csv(exofop)

fp_df = pd.read_csv(fp)
toi_df = pd.read_csv(toi)


review_sheet_tics = review_sheet_df['TIC'].tolist()


fp_tics = fp_df['TIC'].tolist()
toi_tics = toi_df['TIC ID'].tolist()



need_review_tics = []



need_more_review_sheet_header = ['TIC', 'CTOI', 'Period (exofop)', 'Period (TEV)', 'Notes']
need_more_review_exofop_header = ['TIC', 'CTOI', 'Period (days)', 'Transit Epoch (BJD)', 'Notes']


need_more_review_from_review_sheet = []
need_more_review_from_review_sheet.append(['TIC', 'CTOI', 'Period (exofop)', 'Period (TEV)', 'Notes'])


need_more_review_from_exofop = []
need_more_review_from_exofop.append(['TIC', 'CTOI', 'Period (days)', 'Transit Epoch (BJD)', 'Notes'])

for _, row in review_sheet_df.iterrows():
    if (row['TIC'] not in fp_tics) and (pd.isna(row['TOI'])) and (row['TIC'] not in toi_tics):
        row_values = [
            row['TIC'],
            row['CTOI'],
            row['Period (exofop)'],
            row['Period (TEV)'],
            row['Notes']
        ]

        need_more_review_from_review_sheet.append(row_values)
    


need_review_tic = []
exofop_tics = exofop_df['TIC ID'].tolist()



for _, row in exofop_df.iterrows():
    if (row['TIC ID'] not in fp_tics) and (pd.isna(row['Promoted to TOI'])) and (row['TIC ID'] not in toi_tics):
        row_values = [
            row['TIC ID'],
            row['CTOI'],
            row['Period (days)'],
            row['Transit Epoch (BJD)'],
            row['Notes']
        ]
        need_more_review_from_exofop.append(row_values)


need_more_review_from_sheet = 'need_more_review_sheet.csv'
more_review_from_exofop = 'need_more_review_from_exofop.csv'
 
need_more_review_from_sheet_DF = pd.read_csv(need_more_review_from_sheet)
more_review_from_exofop_DF = pd.read_csv(more_review_from_exofop)


more_review_sheet_tic = need_more_review_from_sheet_DF['TIC'].tolist()
more_review_exofop_tic = more_review_from_exofop_DF['TIC'].tolist()

print(f"Review sheet tics (need more review) = {len(more_review_sheet_tic)}")
print(f"Exofop tics (need more review) =  {len(more_review_exofop_tic)}")





duplicate_tics = []

for tic in more_review_sheet_tic:
    if tic in more_review_exofop_tic:
        duplicate_tics.append(tic)
    

print(f"Duplicate TICS: {len(duplicate_tics)}")
        









# with open(more_review_from_exofop, 'w', newline='') as from_exofop:
#     writer = csv.writer(from_exofop)
#     writer.writerows(need_more_review_from_exofop)



# with open(need_more_review_from_sheet, 'w', newline='') as from_sheet:
#     writer = csv.writer(from_sheet)
#     writer.writerows(need_more_review_from_review_sheet)





merged_header = ['TIC', 'CTOI', 'Period (exofop)', 'Period (TEV)', 'Transit Epoch (BJD)', 'Notes']

merged_data = []

for _, row in need_more_review_from_sheet_DF.iterrows():
    master_row = {}
    for column in merged_header:
        if column in need_more_review_sheet_header:
            master_row[column] = row[column]
        else:
            master_row[column] = ""
    
    merged_data.append(master_row)


for _, row in more_review_from_exofop_DF.iterrows():
    master_row = {}
    for column in merged_header:
        if column in need_more_review_exofop_header:
            master_row[column] = row[column] 
        else:
            master_row[column] = ""
        
    merged_data.append(master_row)


unique_merged_data = [dict(t) for t in {tuple(d.items()) for d in merged_data}]


unique_merged_df = pd.DataFrame(unique_merged_data)
unique_merged_df.to_csv('unique_merged_data.csv', index=False)

unique_merged_tics = unique_merged_df['TIC'].tolist()
print(f"Unique merged TICs: {len(unique_merged_tics)}")


print(f"Total TICs (both from review sheet and exofop) = {948 + 2088}")
print(f"Total TICs (both from review sheet and exofop)-without duplicats = {948 + 2088 - 939}")




# Function that can check if there are duplicates in the unique merged tic list
def has_duplicates(lst):
    return len(lst) != len(set(lst))


print(f"The Unique Merged TICs list contains duplicates. {has_duplicates(unique_merged_tics)}")


# Use set appraoch to get rid of duplicates from the unique merged list
unique_merged_tics_no_duplicates =list(set(unique_merged_tics))

print(f"The len of the total unique TICs without duplicates is {len(unique_merged_tics_no_duplicates)}")

# Use the Counter method from collections library to remove every duplicate item from list

elem_counts = Counter(unique_merged_tics)
unique_list = [elem for elem in unique_merged_tics if elem_counts[elem] == 1]

print(f"The length of TICs without every duplicate item = {len(unique_list)}")

unique_merged_df_NO_DUPLICATES = unique_merged_df.drop_duplicates(subset='TIC', keep='first')

unique_merged_df_NO_DUPLICATES.to_csv('need_more_review_FINAL.csv', index=False)
