import pandas as pd
import csv
import numpy as np

ctoi_review_fp = 'CTOI_review_sheet.csv'
exofop = 'exofop_edited.csv'


ctoi_review_fp_df = pd.read_csv(ctoi_review_fp)
exofop_df = pd.read_csv(exofop)


exofop_false_positive_tic_ids = []
exofop_false_positive = []
ctoi_review_false_positives = []

# TIC, CTOI, DISPOSTION, NOTES, ADDITIONAL COMMENT 

ctoi_review_headers = ['TIC', 'CTOI', 'TEV Disposition', 'Notes', 'CTOI Category']
exofop_df_headers = ['TIC ID', 'CTOI', 'TFOPWG Disposition', 'Notes', 'CTOI Category']


# CTOI_Review_FP headers: TIC, CTOI, Period (exofop), Period (TEV), TEV Disposition [5]
# exofop_edited: TIC, CTOI, Transit Epoch, Period (exofop), Planet Radius, Duration, Depth, TFOPWG Disposition [8]


master_header = ['TIC ID', 'CTOI ID', 'Transit Epoch', 'Period (exofop)', 'Period (TEV)', 'Planet Radius', 'Duration',
'Depth', 'TFOPWG Disposition', 'TEV Disposition', 'Notes', 'CTOI Category']


exofop_header = ['TIC', 'CTOI', 'Transit Epoch', 'Period', 'Duration', 'Depth', 'Planet Radius', 'Notes', 'TFOPWG Disposition', 'CTOI Designation']
exofop_false_positive.append(exofop_header)




for index, row in exofop_df.iterrows():
    if row['TFOPWG Disposition'] == 'FP':
        exofop_row_values = [
            int(row['TIC ID']),
            row['CTOI'],
            row['TFOPWG Disposition']
        ]

        exofop_row_values.append('Nan')
        exofop_row_values.append('Likely FP')

#         exofop_false_positive.append(exofop_row_values)


ctoi_header = ['TIC', 'CTOI', 'Period (exofop)', 'Period (TEV)', 'Notes', 'Public comment', 'TEV Disposition', 'CTOI Designation']
ctoi_review_false_positives.append(ctoi_header)

# for index, row in ctoi_review_fp_df.iterrows():
#     if row['TEV Disposition'] == category1 or row['TEV Disposition'] == category2:
#         row_values = [
#             int(row['TIC']),
#             row['CTOI'],
#             row['TEV Disposition'],
#             row['Notes']
#         ]
#         row_values.append('Likely FP')
#         ctoi_review_false_positives.append(row_values)



ctoi_file = 'ctoi_false_postive.csv'
exofop_fp_file = 'exofop_fp_tester.csv'


# Now, merge those two file together 
# Read both csv files both from ctoi list and the exofop one

ctoi_df = pd.read_csv(ctoi_file) 
exofop_df = pd.read_csv(exofop_fp_file)

# Common headers
master_header = ['TIC', 'CTOI', 'Transit Epoch',
                 'Period (exofop)', 'Period (TEV)', 'Planet Radius', 'Duration', 'Depth', 'TFOPWG Disposition', 'TEV Disposition', 'Notes', 'CTOI Designation']

master_data = []
# Loop through each row in the exofop_data 
for _, exofop_row in exofop_df.iterrows():
    master_row = {} 

    for column in master_header:
        if column in exofop_header:
            master_row[column] = exofop_row[column]
        else:
            master_row[column] = ""
    
    # Append the master row to the master dataframe 
    master_data.append(master_row)


for _, ctoi_row in ctoi_df.iterrows():
    master_row = {}

    for column in master_header:
        if column in ctoi_header:
            master_row[column] = ctoi_row[column]
        else:
            master_row[column] = ""
    
    master_data.append(master_row)




# Now, merge these two
# merged_df = pd.merge(ctoi_df, exofop_df, on=['TIC', 'CTOI', 'Notes', 'CTOI Category'], how='inner')


# Create a new DataFrame from the master dataset 
master_df = pd.DataFrame(master_data, columns=master_header)


# Set the CTOI Designation to 'Likely FP' 
column_name = 'CTOI Designation'

master_df[column_name] = master_df[column_name].fillna('Likely FP')

# Save the master DataFrame to a new CSV file
master_df.to_csv('master1.csv', index=False)

# save the merged pandas dataframe into a csv file
# merged_df.to_csv('Mereged_false_positives.csv', index=False)

# Merging error.
#
# with open(ctoi_file, 'w', newline='') as ctoi_fp_file:
#     writer = csv.writer(ctoi_fp_file)
#     writer.writerows(ctoi_review_false_positives)


# with open(exofop_fp_file, 'w', newline='') as exofop_fp:
#     writer = csv.writer(exofop_fp)
#     writer.writerows(exofop_false_positive)





