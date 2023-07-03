import pandas as pd
import csv
import numpy as np

ctoi_review_fp = 'CTOI_Review_FP.csv'
exofop = 'exofop_edited.csv'


ctoi_review_fp_df = pd.read_csv(ctoi_review_fp)
exofop_df = pd.read_csv(exofop)


exofop_false_positive_tic_ids = []
exofop_false_positive = []
ctoi_review_false_positives = []

# Goal: have a CSV file with the following header
# TIC, CTOI, Transit Epoch, Period (exofop), Period (TEV), Planet Radius, Duration, Depth, TFOPWG Disposition, TEV Disposition


# CTOI_Review_FP headers: TIC, CTOI, Period (exofop), Period (TEV), TEV Disposition [5]
# exofop_edited: TIC, CTOI, Transit Epoch, Period (exofop), Planet Radius, Duration, Depth, TFOPWG Disposition [8]


<<<<<<< HEAD


exofop_header = ['TIC', 'CTOI', 'Transit Epoch', 'Period', 'Duration', 'Depth', 'Planet Radius', 'Notes', 'TFOPWG Disposition', 'TOI Review']
=======
exofop_header = ['TIC', 'CTOI', 'Transit Epoch', 'Period', 'Duration',
                 'Depth', 'Planet Radius', 'Notes', 'TFOPWG Disposition', 'CTOI Designation']
>>>>>>> 81ac3364ef1c4c99166fe63b8996834c20321be4
exofop_false_positive.append(exofop_header)


for index, row in exofop_df.iterrows():
    if row['TFOPWG Disposition'] == 'FP':
        exofop_row_values = [
            int(row['TIC ID']),
            row['CTOI'],
            row['Transit Epoch (BJD)'],
            row['Period (days)'],
            row['Duration (hours)'],
            row['Depth (mmag)'],
            row['Planet Radius (R_Earth)'],
            row['Notes'],
            row['TFOPWG Disposition']
        ]

        exofop_row_values.append('Likely FP')

#         exofop_false_positive.append(exofop_row_values)


ctoi_header = ['TIC', 'CTOI', 'Period (exofop)', 'Period (TEV)',
               'Notes', 'Public comment', 'TEV Disposition', 'CTOI Designation']
ctoi_review_false_positives.append(ctoi_header)

for index, row in ctoi_review_fp_df.iterrows():
    ctoi_row_values = [
        row['TIC'],
        row['CTOI'],
        row['Period (exofop)'],
        row['Period (TEV)'],
        row['Notes'],
        row['Public comment'],
        row['TEV Disposition']
    ]
    ctoi_row_values.append('Likely FP')

    ctoi_review_false_positives.append(ctoi_row_values)


ctoi_file = 'ctoi_false_postive.csv'
exofop_fp_file = 'exofop_fp_tester.csv'


# Now, merge those two file together
# Read both csv files both from ctoi list and the exofop one

ctoi_df = pd.read_csv(ctoi_file)
exofop_df = pd.read_csv(exofop_fp_file)

# Common headers
master_header = ['TIC ID', 'CTOI ID', 'Transit Epoch',
                 'Period (exofop)', 'Period (TEV)', 'Planet Radius', 'Duration', 'Depth', 'TFOPWG Disposition', 'TEV Disposition', 'Notes', 'CTOI Category']

<<<<<<< HEAD
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


# Iterate over the ctoi_data 
for _, ctoi_row in ctoi_df.iterrows():
    master_row = {}
    
    for column in master_header:
        if column in ctoi_header:
            master_row[column] = ctoi_row[column]
        else:
            master_row[column] = ""
    
    master_data.append(master_row)


# Create a new DataFrame from the master dataset 
master_df = pd.DataFrame(master_data, columns=master_header)

# Save the master DataFrame to a new CSV file
master_df.to_csv('master1.csv', index=False)
=======
master_df = pd.DataFrame(columns=master_header)  # make the column a header

master_list = [master_header]

master = 'master_test.csv'

with open(master, 'w', newline='') as m:
    writer = csv.writer(m)
    writer.writerows(master_list)
>>>>>>> 81ac3364ef1c4c99166fe63b8996834c20321be4


# with open(ctoi_file, 'w', newline='') as ctoi_fp_file:
#     writer = csv.writer(ctoi_fp_file)
#     writer.writerows(ctoi_review_false_positives)


# with open(exofop_fp_file, 'w', newline='') as exofop_fp:
#     writer = csv.writer(exofop_fp)
#     writer.writerows(exofop_false_positive)
